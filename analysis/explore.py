import streamlit as st

from functions import *

if "selected_columns" not in st.session_state:
    st.session_state.selected_columns = []
if "back_selected_columns" not in st.session_state:
    st.session_state.back_selected_columns = []

if "fitur1_status" not in st.session_state:
    st.session_state.fitur1_status = False
if "back_fitur1_status" not in st.session_state:
    st.session_state.back_fitur1_status = False
if "fitur2_status" not in st.session_state:
    st.session_state.fitur2_status = False
if "back_fitur2_status" not in st.session_state:
    st.session_state.back_fitur2_status = False
if "fitur3_status" not in st.session_state:
    st.session_state.fitur3_status = False
if "fitur4_status" not in st.session_state:
    st.session_state.fitur4_status = False
if "fitur5_status" not in st.session_state:
    st.session_state.fitur5_status = False

if 'viz_type' not in st.session_state:
    st.session_state.viz_type = None
if 'x_col' not in st.session_state:
    st.session_state.x_col = None
if 'y_col' not in st.session_state:
    st.session_state.y_col = None
if 'color_col' not in st.session_state:
    st.session_state.color_col = None

if not st.session_state.fitur1_status and not st.session_state.fitur3_status:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Eksplorasi Data.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.fitur2_status:
    st.session_state.filtered_dataset = True
else:
    st.session_state.filtered_dataset = False

df = pd.read_csv(os.path.join('data', st.session_state.selected_dataset), encoding='ISO-8859-1')
data_explore = baca_data()

expander_fitur = st.sidebar.container(border=True)


# Fitur 1 - Showing

if expander_fitur.toggle("Tampilkan Dataset", value=st.session_state.fitur1_status):
    st.session_state.fitur1_status = True
    st.dataframe(data_explore, use_container_width=True)
else:
    st.session_state.fitur1_status = False
    
if st.session_state.fitur1_status != st.session_state.back_fitur1_status:
    st.session_state.back_fitur1_status = st.session_state.fitur1_status
    st.rerun()


# Fitur 2 - Filtering

if expander_fitur.toggle("Filter Kolom Tertentu", value=st.session_state.fitur2_status):

    if st.session_state.selected_dataset:
        st.session_state.selected_columns = expander_fitur.multiselect(
            "Pilih Kolom",
            df.columns.tolist(),
            default=st.session_state.back_selected_columns,
            key=None,
            placeholder="Silakan pilih kolom...",
        )
    
        if st.session_state.selected_columns != st.session_state.back_selected_columns:
            st.session_state.fitur2_status = True
            st.session_state.back_selected_columns = st.session_state.selected_columns
            st.rerun()
else:
    st.session_state.fitur2_status = False
    st.session_state.selected_columns = df.columns.tolist()

if st.session_state.fitur2_status != st.session_state.back_fitur2_status:
    st.session_state.back_fitur2_status = st.session_state.fitur2_status
    st.session_state.back_selected_columns = []
    st.rerun()

# fitur3 = expander_fitur.toggle("Tampilkan Visualisasi", value=st.session_state.fitur3_status))
# st.session_state.fitur3_status = fitur3
# if fitur3:
#     if st.session_state.selected_dataset:

#         viz_type = expander_fitur.selectbox("Pilih Tipe Visualisasi", 
#                                             ["Histogram", "Scatter Plot", "Bar Chart", "Line Chart"], 
#                                             index= None if st.session_state.viz_type == "" else ["Histogram", "Scatter Plot", "Bar Chart", "Line Chart"].index(st.session_state.viz_type if st.session_state.viz_type != "" else st.session_state.back_viz_type), # type: ignore
#                                             placeholder="Silakan tipe visualisasi...")
#         st.session_state.viz_type = viz_type

#         if viz_type == "Histogram":
#             if st.session_state.x_col != "" and st.session_state.x_col in df.columns.tolist():
#                 x_col_index = df.columns.tolist().index(st.session_state.x_col) # type: ignore
#             elif st.session_state.back_x_col != "" and st.session_state.back_x_col in df.columns.tolist():
#                 x_col_index = df.columns.tolist().index(st.session_state.back_x_col) # type: ignore
#             else:
#                 x_col_index = None

#             x_col = expander_fitur.selectbox("Pilih Kolom untuk Histogram", 
#                                                 df.columns, 
#                                                 index=x_col_index,
#                                                 placeholder="Silakan pilih kolom...")
#             st.session_state.x_col = x_col

#             if st.session_state.color_col != "" and st.session_state.color_col in df.columns.tolist():
#                 color_col_index = ([None] + df.columns.tolist()).index(st.session_state.color_col)
#             elif st.session_state.back_color_col != "":
#                 color_col_index = ([None] + df.columns.tolist()).index(st.session_state.back_color_col)
#             else:
#                 color_col_index = None

#             color_col = expander_fitur.selectbox("Pilih Kolom untuk Warna (Opsional)",
#                                                     df.columns.tolist(),
#                                                     index=color_col_index,
#                                                     placeholder="Silakan pilih kolom...")
#             st.session_state.color_col = color_col

#             if x_col != None and color_col != None:
#                 create_visualization(df, viz_type, x_col=x_col, color_col=color_col)

#         elif viz_type == "Scatter Plot":
#             x_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu X", df.columns)
#             y_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu Y", df.columns)
#             color_col = expander_fitur.selectbox("Pilih Kolom untuk Warna (Opsional)", [None] + df.columns.tolist())
#             create_visualization(df, viz_type, x_col=x_col, y_col=y_col, color_col=color_col)

#         elif viz_type == "Bar Chart":
#             x_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu X (Kategori)", df.columns)
#             y_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu Y (Nilai)", df.columns)
#             color_col = expander_fitur.selectbox("Pilih Kolom untuk Warna (Opsional)", [None] + df.columns.tolist())
#             create_visualization(df, viz_type, x_col=x_col, y_col=y_col, color_col=color_col)

#         elif viz_type == "Line Chart":
#             x_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu X (Waktu)", df.columns)
#             y_col = expander_fitur.selectbox("Pilih Kolom untuk Sumbu Y (Nilai)", df.columns)
#             color_col = expander_fitur.selectbox("Pilih Kolom untuk Warna (Opsional)", [None] + df.columns.tolist())
#             create_visualization(df, viz_type, x_col=x_col, y_col=y_col, color_col=color_col)

#         else:
#             st.warning("Tipe visualisasi tidak valid.")

# fitur4 = expander_fitur.toggle("Fitur 4", value=st.session_state.fitur4_status))
# st.session_state.fitur4_status = fitur4
# fitur5 = expander_fitur.toggle("Fitur 5", value=st.session_state.fitur5_status))
# st.session_state.fitur5_status = fitur5