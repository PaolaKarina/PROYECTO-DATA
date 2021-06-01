  
import streamlit as st
from PIL import Image
import src.funcioncitas as pk
import plotly.express as px
import pandas as pd
from streamlit_folium import folium_static
import folium
import codecs
import streamlit.components.v1 as components


st.write("""
# Mi súper app 
Con Jake el perro y Finn el humano lo pasaremos guay 🚀
""")

df1 = pk.data1()
st.dataframe(df1)