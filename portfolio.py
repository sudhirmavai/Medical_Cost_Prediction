import streamlit as st
st.header("Check your medical cost")
#st.image(image1.jpg)
st.number_input('Enter your age',18,64)
st.radio('Select your sex',['male','Female'])
st.number_input('Enter your BMI(Body per mass)',16,54)
st.write("")
st.multiselect('Count of your children',['0','1','2','3','4','5'])
st.selectbox('Do you smoke',['Yes','No'])
st.multiselect('Enter your region',['Northwest','Southwest'])
st.button('Calculate my medical Insorance cost')

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image1.jpg')