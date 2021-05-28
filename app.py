import streamlit as st
import requests
import datetime
import time
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
This front queries the Le Wagon taxi fare model API
Please input the following below to get a predicted taxi fare.
''')

url = 'https://taxifare.lewagon.ai/predict'
pickup_date = st.date_input('Pickup date', datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('Pickup time', datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'
pickup_longitude = st.number_input('Pickup longitude', value=40.76)
pickup_latitude = st.number_input('Pickup latitude', value=-73.98)
dropoff_longitude = st.number_input('Dropoff longitude', value=40.64)
dropoff_latitude = st.number_input('Dropoff latitude', value=-73.78)
passenger_count = st.number_input('Passenger count', value=1)

params = dict(
    pickup_datetime=pickup_datetime, 
    pickup_longitude=pickup_longitude,
    pickup_latitude=pickup_latitude,
    dropoff_longitude=dropoff_longitude,
    dropoff_latitude=dropoff_latitude,
    passenger_count=passenger_count
    )

response = requests.get(url, params=params)
data = round(response.json()['prediction'], 2)
f'Predicted price : ${data}'

token = "pk.eyJ1IjoiemFwamFuaWNlIiwiYSI6ImNrcDd1dWh3eTA0Mm8yd3Z5NGNrNHZ6eG0ifQ.fRooy_nFj7QFb6ISqYvr_w"

dictionary = {'lat': [pickup_latitude, dropoff_latitude], 'lon': [pickup_longitude, dropoff_longitude]}
map_data = pd.DataFrame.from_dict(dictionary)

st.map(map_data)