import streamlit as st

from functions import *

st.set_page_config(page_title="Dashboard Analisis Data", page_icon='assets/Logo.png',layout="wide")
st.logo('assets/Logo + Text H.png', icon_image='assets/Logo + Text H.png')

st.markdown(
    """
    <style>
        body {
            overflow-x: hidden;
            overflow-y: hidden; 
        }

        

        .stSidebarNav [data-testid="stSidebarNav"] {
            height: 200px;
            padding-top: 1rem;
            position: sticky;  /* Jadikan navigasi sticky */
            top: 0; /* Tempelkan navigasi ke atas */
            z-index: 100; /* Pastikan navigasi berada di atas elemen lain */
        }

        [data-testid="stSidebarNav"] li {
            margin-bottom: 5px; 
        }

        .stElementContainer[data-testid="stElementContainer"] hr {
            margin: 2em 0;
        }

        [data-testid="stSidebarUserContent"] {
            padding-top: 0rem;
        }

        .stSelectbox [data-testid="stWidgetLabel"] {
            margin-top: -10px;
        }

        .stSelectbox [data-testid="stMarkdownContainer"] {
            padding-left: 5px;
            color: rgba(250, 250, 250, 0.6);
        }

        .stMultiSelect [data-testid="stWidgetLabel"] {
            margin-top: -10px;
        }

        .stMultiSelect [data-testid="stMarkdownContainer"] {
            padding-left: 5px;
            color: rgba(250, 250, 250, 0.6);
        }

        # .block-container {
        #     padding-top: 3rem;
        #     padding-bottom: 0rem;
        #     padding-left: 3rem;
        #     padding-right: 3rem;
        # }

        /**** Tabs ****/
        
        .stTabs [data-baseweb="tab-list"] {
            display: flex;
            justify-content: left;
            gap: 20px;
            width: 100%;
        }

        .stTabs [data-baseweb="tab"] {
            flex: 1; 
            height: 50px;
            border-radius: 4px 4px 0px 0px;
            gap: 1px;
            padding-top: 10px;
            padding-bottom: 10px;
            text-align: center;
            position: relative; 
            font-size: 18px; /* Perbesar ukuran font */
            font-weight: 600; /* Tebalkan font */
        }

        .stTabs [data-baseweb="tab"]:focus,
        .stTabs [data-baseweb="tab"]:active,
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            outline: none;
        }

        .stTabs [data-baseweb="tab"]:after {
            content: ""; 
            display: block;
            height: 2px; 
            background-color: #007bff; 
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            transform: scaleX(0);
            transition: transform 0.3s ease; 
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"]:after {
            transform: scaleX(1); 
            background-image: linear-gradient(to right, #7375b6, #39a1b1);
            box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            animation: glowing-underline 2s ease-in-out infinite;
        }

        @keyframes glowing-underline {
            0% {
                box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            }
            50% {
                box-shadow: 0 0 30px rgba(57, 161, 177, 1); 
            }
            100% {
                box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            }
        }

        # [data-baseweb="select"] {
        #     margin-top: -30px;
        # }

        [data-testid="stSidebarNavSeparator"] {
            display: none !important;
        }

        [data-testid="stSidebarNavLink"] { /* Style dasar */
            display: flex;
            align-items: center;
            padding: 5px; 
            border-radius: 8px;
            padding-left: 5px;
            transition: all 0.3s ease;
        }

        [data-testid="stSidebarNavLink"][aria-current="page"] {
            background-color: #2b2b2d !important;
        }

        [data-testid="stSidebarNavLink"] span:nth-child(1) {
            margin-left: 5px;
            margin-right: 10px;
            font-weight: 500;
            font-size: 20px;
        }

        .element-container:has(iframe[height="0"]) {
            display: none;
        }

        /**** Button ****/

        .stButton > button {
            background-image: linear-gradient(to right, #7375b6, #39a1b1);
            color: white;
            font-size: 16px;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            animation: glowing 2s ease-in-out infinite; /* Tambahkan animasi */
        }

        @keyframes glowing {
            0% {
                box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            }
            50% {
                box-shadow: 0 0 30px rgba(57, 161, 177, 1);
            }
            100% {
                box-shadow: 0 0 10px rgba(57, 161, 177, 0.5);
            }
        }


        /**** Check Box ****/

        [data-testid="stCheckbox"] label > div:first-child > div { 
            background-image: linear-gradient(to right, #39a1b1, #7375b6);
            box-shadow: 0 0 10px rgba(57, 161, 177, 0.8); 
            border-radius: 4px; 
            transition: box-shadow 0.3s ease; 
        }

        [data-testid="stCheckbox"]:hover label > div:first-child > div {
            box-shadow: 0 0 30px rgba(57, 161, 177, 0.7); 
        }

        @keyframes glowing-checkbox {
            0% {
                box-shadow: 0 0 40px rgba(57, 161, 177, 1),
                            inset 0 0 20px rgba(255, 255, 255, 0.3);
            }
            50% {
                box-shadow: 0 0 60px rgba(57, 161, 177, 1),
                            inset 0 0 30px rgba(255, 255, 255, 0.5);
            }
            100% {
                box-shadow: 0 0 40px rgba(57, 161, 177, 1),
                            inset 0 0 20px rgba(255, 255, 255, 0.3);
            }
        }

        [data-testid="stCheckbox"] [data-testid="stMarkdownContainer"] p { 
            color: rgba(250, 250, 250, 0.6);
            transition: color 0.3s ease;
            font-size: 14px;
        }

        [data-testid="stCheckbox"] input:checked + div [data-testid="stMarkdownContainer"] p {
            color: #ffffff;
            font-weight: bold;
        }
    </style>
    """, 
    unsafe_allow_html=True)

if 'dataset' not in st.session_state:
    st.session_state.dataset = None 
if 'selected_dataset' not in st.session_state:
    st.session_state.selected_dataset = None 
if 'initial_dataset' not in st.session_state:
    st.session_state.initial_dataset = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.initial_dataset = None
if (st.session_state.dataset is None) or (st.session_state.dataset != st.session_state.initial_dataset):
    st.session_state.initial_dataset = st.session_state.dataset
    st.session_state.back_selected_columns = []
    st.session_state.back_viz_type = None
    st.session_state.back_x_col = None
    st.session_state.back_y_col = None
    st.session_state.back_color_col = None

login_page  = st.Page(login, title="Log in")
logout_page = st.Page(logout, title="Tutup", icon=":material/logout:")

gather      = st.Page("analysis/gather.py", title="Mengenal Data", icon=":material/description:")
eda         = st.Page("analysis/eda.py", title="Mengeksplorasi Data", icon=":material/bubble_chart:")
questions   = st.Page("analysis/questions.py", title="Menjawab Pertanyaan", icon=":material/live_help:")
advanced    = st.Page("analysis/advanced.py", title="Melakukan Analisis Lanjutan", icon=":material/monitoring:")

if st.session_state.logged_in:
    
    pg = st.navigation(
        [
            gather,
            eda,
            questions,
            advanced,
        ]
    )

    st.sidebar.divider()

    expander_data = st.sidebar.expander("Pilih Data", expanded = True)
    dataset_files = [file for file in os.listdir('data') if file.endswith('.csv')]
    if 'selected_dataset' in st.session_state and st.session_state.selected_dataset in dataset_files:
        selected_index = dataset_files.index(st.session_state.selected_dataset) # type: ignore
    else:
        selected_index = None

    st.session_state.dataset = expander_data.selectbox(
        "Pilih Salah Satu Data", 
        dataset_files, 
        index=selected_index,
        placeholder="Silakan pilih dataset..."
    )
    
    if pg != eda:
        st.session_state.back_viz_type = st.session_state.viz_type
        st.session_state.back_x_col = st.session_state.x_col
        st.session_state.back_y_col = st.session_state.y_col
        st.session_state.back_color_col = st.session_state.color_col

    st.session_state.selected_dataset = st.session_state.dataset
else:
    pg = st.navigation([login_page])

pg.run()