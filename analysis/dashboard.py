import streamlit as st

from functions import *

if 'clicked_button_data' not in st.session_state:
    st.session_state.clicked_button_data = False 

st.session_state.filtered_dataset = False
data_dashboard = baca_data()

if st.session_state.selected_dataset == None:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Dashboard.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:

    nama_data = st.session_state.selected_dataset

    if nama_data == "bike_sharing.csv":
    
        # Metric

        data_dashboard['dteday'] = pd.to_datetime(data_dashboard['dteday']) # type: ignore

        daily_avg_temp = data_dashboard.groupby('dteday')['temp'].mean() # type: ignore
        daily_max_hum = data_dashboard.groupby('dteday')['hum'].max() # type: ignore
        daily_avg_windspeed = data_dashboard.groupby('dteday')['windspeed'].mean() # type: ignore
        daily_avg_casual = data_dashboard.groupby('dteday')['casual'].mean() # type: ignore

        delta_temp = daily_avg_temp.diff().iloc[-1]
        delta_hum = daily_max_hum.diff().iloc[-1]
        delta_windspeed = daily_avg_windspeed.diff().iloc[-1]
        delta_casual = daily_avg_casual.diff().iloc[-1]

        avg_temp = daily_avg_temp.iloc[-1]
        max_hum = daily_max_hum.iloc[-1]
        avg_windspeed = daily_avg_windspeed.iloc[-1]
        avg_casual = daily_avg_casual.iloc[-1]

        col1, col2, col3, col4 = st.columns(4)

        with col1.container(border=True):
            st.metric("Rata-Rata Suhu (°C)", f"{avg_temp:.2f}", delta=f"{delta_temp:.2f} °C", delta_color="normal") 

        with col2.container(border=True):
            st.metric("Kelembapan Maksimum (%)", f"{max_hum:.2f}", delta=f"{delta_hum:.2f} %") 

        with col3.container(border=True):
            st.metric("Rata-Rata Kecepatan Angin (km/h)", f"{avg_windspeed:.2f}", delta=f"{delta_windspeed:.2f} km/h") 

        with col4.container(border=True):
            st.metric("Rata-Rata Pengguna Casual", f"{avg_casual:.2f}", delta=f"{delta_casual:.2f}") 

        fig = px.line(data_dashboard,
                    x="dteday", 
                    y="cnt", 
                    color="yr", 
                    title="Tren Jumlah Peminjaman Sepeda",
                    color_discrete_sequence=["#7375b6", "#39a1b1"]) 

        st.plotly_chart(fig)



        # Hitung rata-rata penyewaan per musim
        avg_rentals_per_season = data_dashboard.groupby("season")["cnt"].mean() # type: ignore

        # Buat bar chart
        st.bar_chart(avg_rentals_per_season)



        daily_rentals = data_dashboard.groupby('dteday')['cnt'].sum() # type: ignore
        st.area_chart(daily_rentals)


        hourly_avg = data_dashboard.groupby('hr')['cnt'].mean() # type: ignore
        st.bar_chart(hourly_avg)


        st.line_chart(data_dashboard[['temp', 'cnt']]) # type: ignore


        st.scatter_chart(data_dashboard[['temp', 'cnt']]) # type: ignore


        import plotly.express as px
        fig = px.scatter(data_dashboard, x='temp', y='cnt', color='hum', size='windspeed', hover_data=['temp', 'cnt', 'hum'])
        st.plotly_chart(fig)
