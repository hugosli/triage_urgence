import streamlit as st

option = st.selectbox(
    "Sélectionnez le problème :",
    ("cardio-circulatoire", "Infection", "Abdominal", "Genito-urinaire"),
)
card = st.number_input("Entrez votre fréquence cardiaque :", step = 1)
tension = st.number_input("Entrez votre tension artérielle systolique:", step = 1)
temp = st.number_input("Entrez votre température :", step = 1)
perte_connaissance = st.radio("Avez-vous perdu connaissance ?", ["Oui", "Non"])

res = 5

if card > 130 or card < 50 :
    res = 3

if tension <= 70:
    res = 2
if tension <= 90 and card >= 100:
    res = 2

if perte_connaissance == "Oui":
    res = 1





st.title("Le triage du patient est : " + str(res))
