import streamlit as st
import pickle
from streamlit_option_menu import option_menu
# Change Name and Logo 
st.set_page_config(page_title="Disease Prediction")

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Adding Background Image
background_image_url = "https://th.bing.com/th/id/OIP.0afhUAkw1ojkfSWO3yQQ7wHaEK?rs=1&pid=ImgDetMain"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url({background_image_url});
background-size: cover;
background-position: conter;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top:0;
left:0;
width: 100%;
height: 100%;
background-color: rgba(0,0,0,0.7);
}}
</style>>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    "parkinsons": pickle.load(open('parkinsons_model.sav','rb')),
    "lung_cancer": pickle.load(open('lungs_disease_model.sav','rb'))   
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Parkinsons Prediction',
     'Lung Cancer Prediction']
)

def display_input(label, tooltip, key, type='text'):
    if type == 'text':
        return st.text_input(label, key=key, help=tooltip)
    elif type == 'number':
        return st.number_input(label, key=key, help=tooltip, step=1)
    
# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease")
    st.write("Enter the following details to predict Parkinson's disease: ")

    fo = display_input("MDVP:Fo(Hz)", "Enter MDVP:Fo(Hz) value", "fo", "number")
    fhi = display_input("MDVP:Fhi(Hz)", "Enter MDVP:Fhi(Hz) value", "fhi", "number")
    flo = display_input("MDVP:Flo(Hz)", "Enter MDVP:Flo(Hz) value", "flo", "number")
    Jitter_percent = display_input("MDVP:Jitter(% )", "Enter MDVP:Jitter(%) value", "Jitter_percent", "number")
    Jitter_Abs = display_input("MDVP:Jitter(Abs)", "Enter MDVP:Jitter(Abs) value", "Jitter_Abs", "number")
    RAP = display_input("MDVP:RAP", "Enter MDVP:RAP value" , "RAP", "number")
    PPQ = display_input("MDVP:PPQ", "Enter MDVP:PPQ value" , "PPQ", "number")
    DDP = display_input("Jitter:DDP", "Enter Jitter:DDP value" , "DDP", "number")
    Shimmer = display_input("MDVP:Shimmer", "Enter MDVP:Shimmer value" , "shimmer", "number")
    Shimmer_dB = display_input("MDVP:Shimmer(dB)", "Enter MDVP:Shimmer(dB) value" , "shimmer_dB", "number")
    APQ3 = display_input("Shimmer:APQ3", "Enter Shimmer:APQ3 value" , "APQ3", "number")
    APQ5 = display_input("Shimmer:APQ5", "Enter Shimmer:APQ5 value" , "APQ5", "number")
    APQ = display_input("MDVP:APQ", "Enter MDVP:APQ value" , "APQ", "number")
    DDA = display_input("Shimmer:DDA", "Enter Shimmer:DDA value" , "DDA", "number")
    NHR = display_input("NHR", "Enter NHR value" , "NHR", "number")
    HNR = display_input("HNR", "Enter HNR value" , "HNR", "number")
    RPDE = display_input("RPDE", "Enter RPDE value" , "RPDE", "number")
    DFA = display_input("DFA", "Enter DFA value" , "DFA", "number")
    spread1 = display_input("spread1", "Enter spread1 value" , "spread1", "number")
    spread2 = display_input("spread2", "Enter spread2 value" , "spread2", "number")
    D2 = display_input("D2", "Enter D2 value" , "D2", "number")
    PPE = display_input("PPE", "Enter PPE value" , "PPE", "number")

    parkinsons_diagosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, 
                                                               Jitter_Abs, RAP, PPQ, DDP, Shimmer, 
                                                               Shimmer_dB, APQ3, APQ5, APQ, DDA,
                                                                 NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagosis)

# Lung Cancer Prediction Page 
if selected == 'Lung Cancer Prediction':
    st.title("Lung Cancer")
    st.write("Enter the following details to predict lung cancer:")
    
    GENDER = display_input('Gender (1 = Male, 0 = Female)', "Enter gender of the person ",'GENDER', 'number')
    AGE = display_input('Age', "Enter age of the person",'AGE', 'number')
    SMOKING = display_input('Smoking (1 = Yes, 0 = No)', "Is the person smoking?",'SMOKING', 'number')
    YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes, 0 = No)', "Does the person have yellow fingers?",'YELLOW_FINGERS', 'number')
    ANXIETY = display_input('Anxiety (1 = Yes, 0 = No)', "Does the person have anxiety?",'ANXIETY', 'number')
    PEER_PRESSURE = display_input('Peer Pressure (1 = Yes, 0 = No)', "Is the person under peer pressure?",'PEER_PRESSURE', 'number')
    CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes, 0 = No)', "Does the person have a chronic disease?",'CHRONIC_DISEASE', 'number')
    FATIGUE = display_input('Fatigue (1 = Yes, 0 = No)', "Does the person have fatigue?",'FATIGUE', 'number')
    ALLERGY = display_input('Allergy (1 = Yes, 0 = No)', "Does the person have allergies?",'ALLERGY', 'number')
    WHEEZING = display_input('Wheezing (1 = Yes, 0 = No)', "Does the person experience wheezing?",'WHEEZING', 'number')
    ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes, 0 = No)', "Does the person consume alcohol?",'ALCOHOL_CONSUMING', 'number')
    COUGHING = display_input('Coughing (1 = Yes, 0 = No)', "Does the person cough frequently?",'COUGHING', 'number')
    SHORTNESS_OF_BREATH = display_input('Shortness of Breath (1 = Yes, 0 = No)', "Does the person experience shortness of breath?",'SHORTNESS_OF_BREATH', 'number')
    SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes, 0 = No)', "Does the person have difficulty swallowing?",'SWALLOWING_DIFFICULTY', 'number')
    CHEST_PAIN = display_input('Chest Pain (1 = Yes, 0 = No)', "Does the person experience chest pain?",'CHEST_PAIN', 'number')

    lungs_diagnosis = ''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction = models['lung_cancer'].predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
        st.success(lungs_diagnosis)


