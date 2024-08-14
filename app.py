import streamlit as st
from nl4dv import NL4DV
import pandas as pd

nl4dv_instance = None
dependency_parser_config = {"name": "spacy", "model": "en_core_web_sm", "parser": None}

def init_nl4dv(data_url):
    global nl4dv_instance
    
    nl4dv_instance = NL4DV(data_url)
    data = pd.read_csv(data_url)
    preview = data.head(5)
    preview

option = st.selectbox(
    "Choose a dataset",
    ("Cars", "Movies", "Sales"),
)

if option=='Cars':
    init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/cars-w-year.csv')
elif option=='Movies':
    init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/movies-w-year.csv')
elif option=='Sales':
    init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/superstore.csv')

def process_query():
    nl4dv_response = nl4dv_instance.analyze_query(st.session_state.query, dialog=False)
    st.session_state.vl_spec = nl4dv_response['visList'][0]['vlSpec']        
    st.session_state.nl4dv_response = nl4dv_response

query = st.text_input("Query", "", on_change=process_query, key='query')

if 'vl_spec' in st.session_state:
    st.vega_lite_chart(None,st.session_state.vl_spec)
    "attributeMap"
    st.session_state.nl4dv_response['attributeMap']
    "taskMap"
    st.session_state.nl4dv_response['taskMap']
    "visList"
    st.session_state.nl4dv_response['visList']