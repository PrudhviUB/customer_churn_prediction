import streamlit as st
import json
import requests

st.title('Bank Customer Churn Prediction')


with open('input_options.json') as f:
    side_bar_options = json.load(f)
    options = {}
    for key, value in side_bar_options.items():
        if key in ['HasCrCard','IsActiveMember','Geography', 'Gender']:
            options[key] = st.sidebar.selectbox(key, value)
        else:
            min_val, max_val = value
            current_value = (min_val + max_val)/2
            options[key] = st.sidebar.slider(key, min_val, max_val, value=current_value)


st.write(options)

if st.button('Predict'): 
    print('IN button')

    payload = json.dumps({'inputs': options})
    response = requests.post(
        url=f"http://138.197.99.205:5001/invocations",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    
    prediction = response.json().get('predictions')[0]
    if prediction < 0.5:
        pred = "We’ve lost one of this kind; let's figure out how to keep the next :("
    else:
        pred = "Wohoo! The Customer staying with us!!"
    st.write(f'{pred}')