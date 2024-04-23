#Importtamos las librerias necesarias
import pandas as pd
import streamlit as st
import numpy as np


st.title('Uber pickups in NYC')
date_col = 'date/time'
data_url = 'uber-raw-data-sep14.csv'

@st.cache_data
def load_data(nrows):

    data = pd.read_csv(data_url, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[date_col] = pd.to_datetime(data[date_col])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

#some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[date_col].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)