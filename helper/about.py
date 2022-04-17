#from turtle import width
import streamlit as st 
import pandas as pd
from  PIL import Image
import image_data
import os
import base64

logo = Image.open('image_data/uofm.png')
chen = Image.open('image_data/chen.PNG')
himank = Image.open('image_data/himank.PNG')
sudeep = Image.open('image_data/sudeep.PNG')



def abount_main1():
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:25px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Chen Xu</p>', unsafe_allow_html=True)
        st.image(chen)
    with col2: 
        st.write("Hi, I am Chen Xu. I have worked for an insurance company for about 20 years. Ever since I took a Machine Learning Course on Coursera taught by Andrew Ng in 2018, I have been excited about data science. I want to take on real-world data challenges, use data to improve outcomes and achieve goals.  After 20 months of study with the MADS program, I have already started to  apply  skills learned  in ways that help organizations become more effective, strategic, ethical, and successful.")
    

def abount_main():
    st.subheader("Who we are?")
    st.write("This is team **Yamanaka**. We are a group of masters students from University of Michigan completing our masters in applied data science. " +
             "Over the course of our close to 2 years of study, we have learned machine learning, data mining, NLP, visual exploration and many more that data scientist need. " +
             "We have been given an opportunity to apply all our learnings to our final capstone project and this site is an outcome of over 500 hrs spent collectively by " +
             "this team on this project. Read more about who we are as individuals.")
    col1, mid, col2 = st.columns([2,1,20])
    with col1:               # To display the header text using css style
        st.image(chen, width=160)
        
    with col2:
        st.write("Hi, I am **Chen Xu**. I have worked for an insurance company for about 20 years. " + 
                 "Ever since I took a Machine Learning Course on Coursera taught by Andrew Ng in 2018, " + 
                 "I have been excited about data science. I want to take on real-world data challenges, "+
                 "use data to improve outcomes and achieve goals.  After 20 months of study with the MADS program, "+
                 "I have already started to  apply  skills learned  in ways that help organizations become more effective, strategic, ethical, and successful.")
        
    col1, mid, col2 = st.columns([2,1,20])
    with col1:               # To display the header text using css style
        st.image(himank, width=160)
        
    with col2:
        st.write("Hi, I am **Himank**. I have 7 years of experience in Healthcare strategy consulting, sales and " + 
                "marketing analytics, brand insights and primary market research. I hail from northern " + 
                "part of India. As an individual, I am always fueled by curiosity and motivated by " + 
                "learning. I completed my undergraduate degree in computer science and started my " + 
                "professional journey in analytics. I work with data on day-to-day basis to generate " + 
                "insights that can improve life of patients. However, I always felt that my analysis can " + 
                "be even better if I have had data science knowledge in depth. This led me to upskill " + 
                "and apply for MADS course. Now, after ~2 years of completing this masters degree, I " + 
                "feel this was one of the best decisions I took till date. Along with work and education, I " + 
                "contribute to my capacity to make this society a better place by teaching kids in rural " + 
                "parts of India. ")
        
    col1, mid, col2 = st.columns([2,1,20])
    
    with col1:               # To display the header text using css style
        st.image(sudeep, width=160)
        
    with col2:
        st.write("Hi, I am **Sudeep Singh**.  I have been working as a Java Enterprise Architect and have been in the life insurance industry for the past 20 years. " +
                 "Joining the MADS program was inspired by my son. Education is very important to me and I want to pass the love and commitment of learning down to him." +
                 "By pursuing the Data Science field, I have been challenged to expand my knowledge and skills in new areas.")
        
def about_project():
    # Opening file from file path
    file_pdf = 'helper/capstone-blogpost.pdf'
    with open(file_pdf, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="800" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)