import streamlit as st
import requests

# Give the Name of the Application
st.title('Prediction Churn of Customer')

# Create Submit Form
with st.form(key='form_parameters'):
    g = st.sidebar.selectbox(label='Gender', options=['Female', 'Male'])
    s = st.sidebar.selectbox(label='SeniorCitizen', options=[0,1])
    p = st.sidebar.selectbox(label='Partner', options=['No', 'Yes'])
    d = st.sidebar.selectbox(label='Dependents', options=['No', 'Yes'])
    t = st.number_input('Tenure', min_value=0, step=1, max_value=73)
    ps = st.sidebar.selectbox(label='PhoneService', options=['No', 'Yes'])
    ml = st.sidebar.selectbox(label='MultipleLines', options=['No phone service','No','Yes'])
    ins = st.sidebar.selectbox(label='InternetService', options=['No','DSL','Fiber optic'])
    ons = st.sidebar.selectbox(label='OnlineSecurity', options=['No internet service','No','Yes'])
    onb = st.sidebar.selectbox(label='OnlineBackup', options=['No internet service','No','Yes'])
    dp = st.sidebar.selectbox(label='DeviceProtection', options=['No internet service','No','Yes'])
    ts = st.sidebar.selectbox(label='TechSupport', options=['No internet service','No','Yes'])
    stv = st.sidebar.selectbox(label='StreamingTV', options=['No internet service','No','Yes'])
    sm = st.sidebar.selectbox(label='StreamingMovies', options=['No internet service','No','Yes'])
    con = st.sidebar.selectbox(label='Contract', options=['Month-to-month','One year','Two year'])
    pb = st.sidebar.selectbox(label='PaperlessBilling', options=['No', 'Yes'])
    pm = st.sidebar.selectbox(label='PaymentMethod', options=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    mc = st.number_input('MonthlyCharges', min_value=18.25, step=0.05,max_value=118.75)
    tc = st.number_input('TotalCharges', min_value=18.8, step=0.02,max_value=8684.8)

    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'https://churn-fadhilsadeli.koyeb.app/predict'
    param = {'gender': g,
    'SeniorCitizen': s,
    'Partner': p,
    'Dependents': d,
    'tenure': t,
    'PhoneService': ps,
    'MultipleLines': ml,
    'InternetService': ins,
    'OnlineSecurity': ons,
    'OnlineBackup': onb,
    'DeviceProtection': dp,
    'TechSupport': ts,
    'StreamingTV': stv,
    'StreamingMovies':sm,
    'Contract': con,
    'PaperlessBilling': pb,
    'PaymentMethod': pm,
    'MonthlyCharges': mc,
    'TotalCharges': tc}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)
