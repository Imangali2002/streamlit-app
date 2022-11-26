import streamlit as st
import requests
from io import BytesIO
import plotly.express as px
import numpy
import pandas as pd

st.set_page_config(layout="wide")

st.title("Map")

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
    
#     st.write(uploaded_file.name)

#     bytes_data = uploaded_file.getvalue()

#     with open('static/csv/test.csv', 'rb') as f:
#         st.download_button('Download File', f, file_name='test.csv')

# st.write("You have entered", st.session_state["my_input"])



uploaded_files = st.file_uploader("Choose a tiff files", accept_multiple_files=True)
for uploaded_file in uploaded_files:

    file = BytesIO(uploaded_file.getvalue())
    file = {'file': ("tif", file)}

    r = requests.post('http://127.0.0.1:8000/uploadfile', files=file)
    st.text(r.status_code)
    st.text(r.text)
    col1, col2 = st.columns([7, 3])
    with col1:
        st.image('static/images/083122.jpg')
    with col2:
        random_x = [100, 2000, 550]
        names = ['A', 'B', 'C']
        
        fig = px.pie(values=random_x, names=names)
        st.plotly_chart(fig)
    
    st.write()

