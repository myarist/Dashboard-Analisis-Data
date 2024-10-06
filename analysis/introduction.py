import streamlit as st
from streamlit_js_eval import streamlit_js_eval # type: ignore

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

if 'clicked_sample_data' not in st.session_state:
    st.session_state.clicked_sample_data = False 

st.session_state.filtered_dataset = False
data_intro = baca_data()

if not st.session_state.clicked_sample_data:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Mengenal Data.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

else:
    placeholder = st.container()
    deskripsi_data()

    with placeholder.container():
        st.dataframe(data_intro, use_container_width=True)