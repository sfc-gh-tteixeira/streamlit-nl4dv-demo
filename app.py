import streamlit as st
from nl4dv import NL4DV
import pandas as pd


@st.cache_resource
def init_nl4dv(data_url):
    return NL4DV(data_url), pd.read_csv(data_url)


"""
# :speak_no_evil: NL4DV Demo

[NL4DV](https://github.com/nl4dv/nl4dv) is a Python library that takes a natural language query
about a given dataset and outputs a structured JSON object containing data attributes, analytic
tasks, and visualizations ([Vega-Lite](https://vega.github.io/vega-lite/) specifications).
Below is a demo showing it in action.
"""

""

option = st.selectbox(
    "Choose a dataset",
    ("Cars", "Movies", "Sales"),
)

if option=='Cars':
    nl4dv_instance, data = init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/cars-w-year.csv')
elif option=='Movies':
    nl4dv_instance, data = init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/movies-w-year.csv')
elif option=='Sales':
    nl4dv_instance, data = init_nl4dv('https://raw.githubusercontent.com/nl4dv/nl4dv/master/examples/assets/data/superstore.csv')

data

query = st.text_input("Say what you want to plot")

# Some spacing
""
""
""

if query:
    nl4dv_response = nl4dv_instance.analyze_query(query)

    """
    ## Result
    """

    for viz in nl4dv_response['visList']:
        st.vega_lite_chart(None, viz['vlSpec'])

    if not nl4dv_response['visList']:
        st.info("""
            No results. _Try something else!_
            """, icon=":material/info:")

    # Some spacing
    ""
    ""
    ""

    with st.expander(":gray[Debug info for nerds]"):
        "##### attributeMap"
        nl4dv_response['attributeMap']

        ""

        "##### taskMap"
        nl4dv_response['taskMap']

        ""

        "##### visList"
        nl4dv_response['visList']
