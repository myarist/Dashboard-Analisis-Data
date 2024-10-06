import streamlit as st

if not st.session_state.clicked_sample_data:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<div style='height: 10vh; display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)
        st.image('assets/Pertanyaan.png', width=600, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)