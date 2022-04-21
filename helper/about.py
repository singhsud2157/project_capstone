#from turtle import width
import streamlit as st 
import pandas as pd
from  PIL import Image
import image_data
import os
import base64

chen = Image.open('image_data/chen.PNG')
himank = Image.open('image_data/himank.PNG')
sudeep = Image.open('image_data/sudeep.PNG')
christina = Image.open('image_data/christina.PNG')


def abount_main():
    #st.subheader("Who we are?")
    st.markdown(f'<h1 style="font-family:sans-serif;color:black;font-size:25px;">{"About Team"}</1>', unsafe_allow_html=True)    
    team_story = """This is team <b>Yamanaka</b>. We are a group of masters students from University of Michigan completing our masters in applied data science. 
             Over the course of our close to 2 years of study, we have learned machine learning, data mining, NLP, visual exploration and many more that data scientist need. 
             We have been given an opportunity to apply all our learnings to our final capstone project and this site is an outcome of over 500 hrs spent collectively by 
             this team on this project. We would like to thanks Christina for facilitating such a positive learning environment!. Thank you so much for your time and patience. 
             You definitively love to teach and guide. You make things very simple and human. Read more about who we are as individuals."""
    
    st.markdown(f'<p style="font-family:sans-serif;color:black;font-size:14px;">{team_story}</p>', unsafe_allow_html=True)    
    
    col1, mid, col2 = st.columns([3,1,15])
    with col1:               # To display the header text using css style
        st.image(chen, width=160)
        
    with col2:
        chen_story = """Hi, I am <b>Chen Xu</b>. I have worked for an insurance company for about 20 years. 
                 Ever since I took a Machine Learning Course on Coursera taught by Andrew Ng in 2018, 
                 I have been excited about data science. I want to take on real-world data challenges, 
                 use data to improve outcomes and achieve goals.  After 20 months of study with the MADS program, 
                 I have already started to  apply  skills learned  in ways that help organizations become more effective, strategic, ethical, and successful."""
        st.markdown(f'<p style="font-family:sans-serif;color:black;font-size:14px;">{chen_story}</p>', unsafe_allow_html=True)    
    
    col1, mid, col2 = st.columns([3,1,15])
    with col1:               # To display the header text using css style
        st.image(himank, width=160)
        
    with col2:
        himank_story = """Hi, I am <b>Himank Kansal</b>. I have 7 years of experience in Healthcare strategy consulting, sales and 
                        marketing analytics, brand insights and primary market research. I hail from northern 
                        part of India. As an individual, I am always fueled by curiosity and motivated by learning. 
                        I completed my undergraduate degree in computer science and started my professional journey in analytics. 
                        I work with data on day-to-day basis to generate insights that can improve life of patients. 
                        However, I always felt that my analysis can be even better if I have had data science knowledge in depth. 
                        This led me to upskill and apply for MADS course. Now, after ~2 years of completing this masters degree, 
                        I feel this was one of the best decisions I took till date. Along with work and education, 
                        I contribute to my capacity to make this society a better place by teaching kids in rural parts of India. """
        st.markdown(f'<p style="font-family:sans-serif;color:black;font-size:14px;">{himank_story}</p>', unsafe_allow_html=True)
            
    col1, mid, col2 = st.columns([3,1,15])
    
    with col1:               
        st.image(sudeep, width=160)
        
    with col2:
        sudeep_story = """Hi, I am <b>Sudeep Singh</b>.  I have been working as a Java Enterprise Architect and have been in the life insurance industry for the past 20 years. 
                        Joining the MADS program was inspired by my son. Education is very important to me and I want to pass the love and commitment of learning down to him.
                        By pursuing the Data Science field, I have been challenged to expand my knowledge and skills in new areas."""
        st.markdown(f'<p style="font-family:sans-serif;color:black;font-size:14px;">{sudeep_story}</p>', unsafe_allow_html=True)
    
    col1, mid, col2 = st.columns([3,1,15])
    with col1:               
        st.image(christina, width=160)
        
    with col2:
        christina_story = """I am <b>Cristina Garbacea</b>. I am a PhD student in Computer Science and Engineering at University of Michigan Ann Arbor. My advisor is Prof. 
                        Qiaozhu Mei, and I am part of the Foreseer group. My research interests primarily lie in machine learning and deep learning for natural language processing 
                        and its applications. I spent Summer 2018 and Fall 2020 interning with Google Deepmind in London, UK.
                        Before coming to Michigan, I completed my MSc degree in Artificial Intelligence at University of Amsterdam, The Netherlands, 
                        where I was part of the ILPS research group. During this period I interned twice at Microsoft Research, first in Cambridge, UK (2014) 
                        and then in Redmond, USA (2016). I have a double Bachelor degree in Computer Science & Electrical Engineering and Computers from 
                        Transilvania University of Brasov, Romania.
                        You can check my LinkedIn, DBLP or Google Scholar profiles. I am glad to hear from you at garbacea@umich.edu.."""
        st.markdown(f'<p style="font-family:sans-serif;color:black;font-size:14px;">{christina_story}</p>', unsafe_allow_html=True)

def about_project():
    # Opening file from file path
    print('here')
    file_pdf = 'helper/capstone-blogpost.pdf'
    with open(file_pdf, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="900" height="800" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    