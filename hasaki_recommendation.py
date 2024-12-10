import streamlit as st

st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: Arial, sans-serif;
    }
    p {
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #2c5423;  
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 14px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;  
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;

    }
    .centered-button-container {
        display: flex;
        justify-content: center;  
        align-items: center;      
    }
    <style>
        .css-1d391kg { 
            color: #FF6347;  
        }
        .css-1d391kg:hover {
            color: #008080;  
        }        
    </style>
    </style>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([1, 4])
col1.image("hasaki.png")
col2.markdown(''' <h1 style='text-align: center; color: #4CAF50;'>Hasaki<br> Recommendation System </h1> ''', unsafe_allow_html=True)

with st.sidebar:
    container = st.container(border=True)
    container.markdown(''':orange[GVHD:]<br>
                       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:blue[Khuất Thùy Phương]''', unsafe_allow_html=True)
    # container.divider()
    container.markdown(''':orange[HVTH:]<br>
                       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:blue[Trần Phương Mai]<br>
                       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:blue[Vũ Trung Kiên]
                       ''', unsafe_allow_html=True)
    container.markdown(''':orange[12/2024]''', unsafe_allow_html=True)

pages = {
    "About project": [ 
        st.Page("home.py", title="About project", icon="🏚️"),
    ],
    "Content based model": [
        st.Page("content_based_info.py", title="Built model",icon="✨"),
        st.Page("content_based_model.py", title="Deploy",icon="✨"),
    ],
    "Collaborative model": [
        st.Page("collaborative_info.py", title="Built model",icon="✨"),
        st.Page("collaborative_model.py", title="Deploy",icon="✨"),
    ],
}

pg = st.navigation(pages)
pg.run()









