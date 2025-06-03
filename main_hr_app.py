import streamlit as st
from source.load_user_data import load_user_data, get_all_names, get_image
from PIL import Image
import pandas as pd
from plotly import express as px
import plotly.graph_objects as go
from source.functions_hr_plot import analyse_heart_rate, plot_analysed_hr, calculate_time_per_zone


# Sicherstellen, dass auch vor der Nutzerauswahl schon ein Wert im SessionState ist
if "current_user" not in st.session_state:
    st.session_state.current_user = "None"

FILE_PATH = "data/person_db.json"
FILE_PATH_HR = "data/activity.csv"
user_data = load_user_data(FILE_PATH)
name_list = get_all_names(user_data)

st.title("EKG App")

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

st.write("Bitte wählen Sie eine Versuchsperson aus der Liste aus.")

# Eine Auswahlbox für die Versuchsperson
st.session_state["current_user"] = st.selectbox(
    'Versuchsperson',
    options =  name_list, key="sbVersuchsperson")

st.write("Aktuelle Versuchsperson:", st.session_state["current_user"])

image = Image.open("data\pictures\js.jpg")
st.image(get_image(st.session_state.current_user), caption = st.session_state.current_user)

st.write("## Herzfrequenzdaten analysieren")
max_hr = st.number_input("Geben Sie Ihre maximale Herzfrequenz ein:", min_value=100, max_value=240, value=200)
fig1 = plot_analysed_hr(analyse_heart_rate(FILE_PATH_HR, max_hr), max_hr)
st.plotly_chart(fig1)

st.write("## Zeit in den Herzfrequenzzonen")
st.plotly_chart(calculate_time_per_zone(analyse_heart_rate(FILE_PATH_HR, max_hr)))