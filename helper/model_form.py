import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
import pickle

form_list_lables = ['cerad', 'braak', 'ihc_tau2_ffpe', 'ihc_at8_ffpe', 'ihc_at8', 'ihc_a_beta_ffpe', 'ihc_a_beta', 'ihc_gfap_ffpe', 'ptau_ng_per_mg'
                    ,'vegf_pg_per_mg', 'ab42_over_ab40_ratio','ptau_over_tau_ratio', 'a_syn_pg_per_mg', 'mcp_1_pg_per_mg','ab42_pg_per_mg']

def get_model_form():
    st.markdown(""" <style> .font {
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Brain Dementia Prediction Model</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload File(csv)", type =["csv"])
    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)
        #creeate aaray of values and norm.transform(array) then use the output for prediction
        pickle_in = open('helper/model.pkl', 'rb') 
        classifier = pickle.load(pickle_in)
        prediction = classifier.predict_proba(uploaded_df)
     
        output='{0:.{1}f}'.format(prediction[0][1], 2)
        output = (float(output) * 100)
        output_string = "Chances of getting Dementia is **"+str(output)+"%**"
        st.write(output_string)
    with st.form(key='dimentia_form',clear_on_submit=True): 
        st.subheader("Enter Values: ")
        col1, col2, col3 = st.columns([5,5,5])
        with col1:
            cerad=st.text_input(label='cerad: ', key='1') #Collect user feedback
            ihc_at8_ffpe =st.text_input(label='ihc_at8_ffpe: ', key='2') #Collect user feedback
            ihc_a_beta=st.text_input(label='ihc_a_beta: ', key='3') #Collect user feedback
            vegf_pg_per_mg=st.text_input(label='vegf_pg_per_mg: ', key='4') #Collect user feedback
            ab42_over_ab40_ratio=st.text_input(label='ab42_over_ab40_ratio: ', key='5') #Collect user feedback
        with col2:
            braak=st.text_input(label='braak: ', key='6') #Collect user 
            ihc_at8=st.text_input(label='ihc_at8: ', key='7') #Collect user feedback
            ihc_gfap_ffpe=st.text_input(label='ihc_gfap_ffpe: ', key='8') #Collect user feedback
            ptau_over_tau_ratio=st.text_input(label='ptau_over_tau_ratio: ', key='9') #Collect user 
            a_syn_pg_per_mg=st.text_input(label='a_syn_pg_per_mg: ', key='10') #Collect user feedback
        with col3:
            ihc_tau2_ffpe=st.text_input(label='ihc_tau2_ffpe: ', key='11') #Collect user feedback
            ihc_a_beta_ffpe=st.text_input(label='ihc_a_beta_ffpe: ', key='12') #Collect user feedback
            ptau_ng_per_mg=st.text_input(label='ptau_ng_per_mg: ', key='13') #Collect user feedback
            mcp_1_pg_per_mg=st.text_input(label='mcp_1_pg_per_mg: ', key='14') #Collect user feedback
            ab42_pg_per_mg=st.text_input(label='ab42_pg_per_mg: ', key='15') #Collect user feedback
            
        submitted = st.form_submit_button('Submit')
        if submitted:
            #st.write(dimentia_form)
            form_list_values = []
            form_list_values.append(float(cerad))
            form_list_values.append(float(braak))
            form_list_values.append(float(ihc_tau2_ffpe))
            form_list_values.append(float(ihc_at8_ffpe))
            form_list_values.append(float(ihc_at8))
            form_list_values.append(float(ihc_a_beta_ffpe))
            form_list_values.append(float(ihc_a_beta))
            form_list_values.append(float(ihc_gfap_ffpe))
            form_list_values.append(float(ptau_ng_per_mg))
            form_list_values.append(float(vegf_pg_per_mg))
            form_list_values.append(float(ab42_over_ab40_ratio))
            form_list_values.append(float(ptau_over_tau_ratio))
            form_list_values.append(float(a_syn_pg_per_mg))
            form_list_values.append(float(mcp_1_pg_per_mg))
            form_list_values.append(float(ab42_pg_per_mg))
            #form_list_values1 = [3,6,0.013154,0.012725,0.000078,0.01158,0.013552,0.731336,0.457328,0.17,400.831725,0.30181,0.070626,41.73,100.00085]
            #print(form_list_values)
            df_model = pd.DataFrame(columns = form_list_lables)
            df_model.loc[len(df_model)] = form_list_values
            
            pickle_in = open('helper/model.pkl', 'rb') 
            classifier = pickle.load(pickle_in)
            prediction = classifier.predict_proba(df_model)
            
            output='{0:.{1}f}'.format(prediction[0][1], 2)
            output = (float(output) * 100)
            output_string = "Chances of getting Dementia is **"+str(output)+"%**"
            st.write(output_string)