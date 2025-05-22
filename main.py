import streamlit as st
from source.load_user_data import load_user_data, get_all_names, get_image
from PIL import Image


# Sicherstellen, dass auch vor der Nutzerauswahl schon ein Wert im SessionState ist
if "current_user" not in st.session_state:
    st.session_state.current_user = "None"

file_path = "data/person_db.json"
user_data = load_user_data(file_path)
name_list = get_all_names(user_data)

st.title("EKG App")

# st.set_page_config(
#     page_title="EKG App",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

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