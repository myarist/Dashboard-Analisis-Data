import streamlit as st
from streamlit_js_eval import streamlit_js_eval

from functions import *

st.markdown(
    """
    <style>
    .css-18e3th9 {
        padding-top: 0rem;
        padding-bottom: 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
        padding-right: 1rem;
        padding-bottom: 3.5rem;
        padding-left: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

if st.session_state.selected_dataset == None:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Mengenal Data.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    def buka_sidebar():
        st.session_state.sidebar_status = 'expanded'
    
    tombol_placeholder = st.empty()

    lebar_layar = streamlit_js_eval(js_expressions='screen.width')
    time.sleep(2)

    if lebar_layar < 767:
        with tombol_placeholder.container():
            col4, col5, col6 = st.columns([1, 1, 1])
            col5.button("Pilih Dataset", on_click=buka_sidebar, use_container_width=True)

else:
    placeholder = st.container()
    deskripsi_data()

    with placeholder.container():
        baca_data()