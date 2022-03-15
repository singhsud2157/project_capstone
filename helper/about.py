from turtle import width
import streamlit as st 
import pandas as pd
from  PIL import Image
import image_data
import os

logo = Image.open('image_data/uofm.png')


def abount_main():
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Project</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        st.image(logo, width=130)
    st.write("Chen Xu, Himank Kansal & Sudeep Singh")    
    