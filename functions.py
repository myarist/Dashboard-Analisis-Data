import os
import pandas as pd
import streamlit as st
import time
import plotly.express as px

@st.fragment
def login():
    col1, col2, col3 = st.columns([1, 1.3, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Login.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns([1, 1, 1])
    if col2.button("Mari Kita Mulai", use_container_width=True):
        st.session_state.logged_in = True
        col2.empty()
        col5.empty()
        time.sleep(1)
        st.rerun()

def logout():
    st.session_state.logged_in = False
    st.session_state.chat1 = False
    st.rerun()

def stream_data_fast(teks):
    for char in teks:
        yield char
        time.sleep(0.001)

def stream_data_medium(teks):
    for char in teks:
        yield char
        time.sleep(0.01)

def stream_data_slow(teks):
    for char in teks:
        yield char
        time.sleep(0.1)

def set_state(i):
    st.session_state.stage = i

@st.fragment
def baca_data(filter_kolom=False, selected_columns=None):
    if st.session_state.dataset:
        df = pd.read_csv(os.path.join('data', st.session_state.dataset), encoding='ISO-8859-1')

        if filter_kolom and selected_columns:
            df_filtered = df[st.session_state.selected_columns]  
        else:
            df_filtered = df

        st.dataframe(df_filtered, use_container_width=True)
    else:
        df = None

    return df

@st.fragment
def deskripsi_data():
    data = st.session_state.dataset

    if data:
        tab1, tab2, tab3 = st.tabs([f"Apa itu data {data}?", "Bagaimana struktur datasetnya?", "Dari mana sumbernya?"])

        with tab1:
            if data == "bike_sharing.csv":
                st.write("Dataset ini berasal dari sistem bike sharing atau berbagi sepeda di kota Washington, D.C., Amerika Serikat, yang bernama Capital Bikeshare. Sistem ini memungkinkan orang untuk menyewa sepeda dari satu stasiun dan mengembalikannya di stasiun lain yang tersebar di seluruh kota. Data ini dikumpulkan selama dua tahun, yaitu tahun 2011 dan 2012.")
                st.write("Data ini sangat berguna untuk memahami bagaimana orang menggunakan sistem berbagi sepeda. Dengan menganalisis data ini, kita bisa mendapatkan informasi penting, seperti:")
                st.write("- **Pola Penggunaan:** Kapan orang paling banyak menyewa sepeda? Apakah di pagi hari saat berangkat kerja, di sore hari saat pulang kerja, atau di akhir pekan saat liburan?")
                st.write("- **Pengaruh Cuaca**: Apakah cuaca memengaruhi jumlah penyewa? Apakah orang lebih suka bersepeda saat cuaca cerah? Bagaimana jika hujan atau bersalju?")
                st.write("- **Pengaruh Musim**: Apakah jumlah penyewa berbeda di setiap musim? Mungkin lebih banyak orang bersepeda di musim panas daripada di musim dingin.")
                st.write("- **Perencanaan Sumber Daya**: Dengan mengetahui pola penggunaan, operator bike sharing dapat merencanakan jumlah sepeda yang dibutuhkan di setiap stasiun dan kapan harus melakukan perawatan.")     
            if data == "air_quality.csv":
                st.write("Dataset ini menyediakan data yang kaya tentang kualitas udara dan kondisi cuaca di Beijing. Masing-masing dataset berisi 35.064 baris dan 18 kolom, yang merekam kualitas udara dan kondisi cuaca di stasiun Aotizhongxin, Beijing, Tiongkok, dari 1 Maret 2013 hingga 28 Februari 2017. Data ini dapat digunakan untuk berbagai tujuan, seperti:")
                st.write("- **Analisis Kualitas Udara**: Mengidentifikasi pola dan tren dalam polusi udara.")
                st.write("- **Pemodelan Prediksi**: Membangun model untuk memprediksi kualitas udara di masa depan.")
                st.write("- **Studi Kesehatan Masyarakat**: Menganalisis hubungan antara polusi udara dan kesehatan masyarakat.")
                st.write("- **Perencanaan Kota**: Mengembangkan strategi untuk mengurangi polusi udara dan meningkatkan kualitas hidup di perkotaan.")
            if data == "e_commerce.csv":
                st.write("Dataset ini merupakan data publik e-commerce dari Olist, sebuah toko besar di marketplace Brazil. Dataset ini mencakup informasi lebih dari 100 ribu pesanan yang terjadi antara tahun 2016 hingga 2018 di berbagai marketplace. Data tersebut memberikan gambaran dari berbagai dimensi, seperti status pesanan, harga, metode pembayaran, performa pengiriman, lokasi pelanggan, atribut produk, hingga ulasan pelanggan. Data ini dapat digunakan untuk berbagai tujuan, seperti:")
                st.write("- **Analisis Perilaku Konsumen**: Memahami preferensi dan pola pembelian pelanggan, serta faktor-faktor yang memengaruhi kepuasan mereka.")
                st.write("- **Analisis Kinerja Penjualan**: Mengevaluasi kinerja penjual dan produk, menganalisis tren penjualan, dan memprediksi permintaan.")
                st.write("- **Analisis Logistik dan Pengiriman**: Mengevaluasi efisiensi pengiriman, menganalisis dampak lokasi terhadap waktu pengiriman, dan mengidentifikasi area untuk perbaikan.")
                st.write("- **Analisis Pemasaran**: Mengembangkan strategi pemasaran yang tepat sasaran, menganalisis efektivitas kampanye, dan mengidentifikasi peluang pasar.")
                st.write("- **Analisis Teks**: Menganalisis ulasan pelanggan untuk mendapatkan wawasan tentang produk dan layanan.")
                st.write("- **Pengembangan Model Prediktif**: Membangun model untuk memprediksi penjualan, permintaan produk, dan churn pelanggan.")
                st.write("- **Klasterisasi**: Mengelompokkan pelanggan berdasarkan karakteristik dan perilaku pembelian mereka.")
        with tab2:
            st.write(f"Baik, mari kita liat struktur dari data **{data}**.")
            if data == "bike_sharing.csv":
                st.write("- **instant**: Nomor urut data.")
                st.write("- **dteday**: Tanggal pencatatan data.")
                st.write("- **season**: Musim (1: semi, 2: panas, 3: gugur, 4: dingin).")
                st.write("- **yr**: Tahun (0: 2011, 1: 2012).")
                st.write("- **mnth**: Bulan (1 hingga 12).")
                st.write("- **hr**: Jam (0 hingga 23).")
                st.write("- **holiday**: Apakah hari itu hari libur (1) atau bukan (0).")
                st.write("- **weekday**: Hari dalam seminggu (0: Minggu, 1: Senin, dst.).")
                st.write("- **workingday**: Apakah hari itu hari kerja (1) atau bukan (0).")
                st.write("- **weathersit**: Kondisi cuaca (1: Cerah, 2: Berkabut, 3: Hujan Ringan, 4: Hujan Deras)")
                st.write("- **temp**: Suhu dalam Celcius (dinormalisasi).")
                st.write("- **atemp**: Suhu yang dirasakan dalam Celcius (dinormalisasi).")
                st.write("- **hum**: Kelembapan (dinormalisasi).")
                st.write("- **windspeed**: Kecepatan angin (dinormalisasi).")
                st.write("- **casual**: Jumlah pengguna kasual (tidak terdaftar).")
                st.write("- **registered**: Jumlah pengguna terdaftar.")
                st.write("- **cnt**: Total jumlah sepeda yang disewa (casual + registered).")
            if data == "air_quality.csv":
                st.write("- **no**: Nomor indeks unik untuk setiap jam.")
                st.write("- **year**: Tahun pengamatan (2013-2017).")
                st.write("- **month**: Bulan pengamatan (1-12).")
                st.write("- **day**: Hari dalam bulan (1-31).")
                st.write("- **hour**: Jam dalam hari (0-23).")
                st.write("- **PM2.5**: Konsentrasi partikulat halus (PM2.5) dalam mikrogram per meter kubik (μg/m³).")
                st.write("- **PM10**: Konsentrasi partikulat kasar (PM10) dalam μg/m³.")
                st.write("- **SO2**: Konsentrasi sulfur dioksida (SO2) dalam μg/m³.")
                st.write("- **NO2**: Konsentrasi nitrogen dioksida (NO2) dalam μg/m³.")
                st.write("- **CO**: Konsentrasi karbon monoksida (CO) dalam μg/m³.")
                st.write("- **O3**: Konsentrasi ozon (O3) dalam μg/m³.")
                st.write("- **TEMP**: Suhu udara dalam derajat Celcius (°C).")
                st.write("- **PRES**: Tekanan udara dalam hektopascal (hPa).")
                st.write("- **DEWP**: Titik embun dalam °C.")
                st.write("- **RAIN**: Curah hujan dalam milimeter (mm).")
                st.write("- **wd**: Arah angin.")
                st.write("- **WSPM**: Kecepatan angin dalam meter per detik (m/s).")
                st.write("- **station**: Nama stasiun pemantauan (dalam dataset ini hanya ada satu stasiun: Aotizhongxin)")
            if data == "e_commerce.csv":
                st.write("Dataset ini terdiri dari beberapa file CSV yang saling terkait:")
                st.write("- **olist_customers_dataset.csv**: Informasi tentang pelanggan, termasuk lokasi mereka.")
                st.write("- **olist_geolocation_dataset.csv**: Memetakan kode pos Brazil ke koordinat geografis (latitude dan longitude).")
                st.write("- **olist_order_items_dataset.csv**: Rincian item dalam setiap pesanan, seperti ID produk, kuantitas, dan harga.")
                st.write("- **olist_order_payments_dataset.csv**: Informasi pembayaran untuk setiap pesanan, termasuk metode pembayaran dan jumlah pembayaran.")
                st.write("- **olist_order_reviews_dataset.csv**: Ulasan yang diberikan oleh pelanggan untuk produk dan penjual.")
                st.write("- **olist_orders_dataset.csv**: Informasi umum tentang pesanan, seperti tanggal pembelian, status pesanan, dan tanggal pengiriman.")
                st.write("- **olist_products_dataset.csv**: Atribut produk, seperti kategori produk, dimensi, dan berat.")
                st.write("- **olist_sellers_dataset.csv**: Informasi tentang penjual, termasuk lokasi mereka.")
                st.write("- **product_category_name_translation.csv**: Terjemahan nama kategori produk dari bahasa Portugis ke bahasa Inggris.")
        with tab3:
            st.write(f"Sumber dari dari dataset **{data}**")
            if data == "bike_sharing.csv":
                st.write("http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset")
            if data == "air_quality.csv":
                st.write("https://github.com/marceloreis/HTI")
            if data == "e_commerce.csv":
                st.write("https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")

@st.fragment
def create_visualization(df, viz_type, x_col=None, y_col=None, color_col=None):
    if viz_type == "Histogram":
        fig = px.histogram(df, x=x_col, color=color_col)
    elif viz_type == "Scatter Plot":
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col)
    elif viz_type == "Bar Chart":
        fig = px.bar(df, x=x_col, y=y_col, color=color_col)
    elif viz_type == "Line Chart":
        fig = px.line(df, x=x_col, y=y_col, color=color_col)
    else:
        st.warning("Tipe visualisasi tidak valid.")
        return

    st.plotly_chart(fig, use_container_width=True)

