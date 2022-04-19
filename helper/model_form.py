import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
import pickle

form_list_lables = ['cerad', 'braak', 'ihc_tau2_ffpe', 'ihc_at8_ffpe', 'ihc_at8', 'ihc_a_beta_ffpe', 'ihc_a_beta', 'ihc_gfap_ffpe', 'ptau_ng_per_mg'
                    ,'vegf_pg_per_mg', 'ab42_over_ab40_ratio','ptau_over_tau_ratio', 'a_syn_pg_per_mg', 'mcp_1_pg_per_mg','ab42_pg_per_mg']

def get_model_form():
    pickle_n = open('helper/normalizar.pkl', 'rb') 
    normalizer = pickle.load(pickle_n)
    
    pickle_c = open('helper/classifier.pkl', 'rb') 
    classifier = pickle.load(pickle_c)
    
    st.markdown(""" <style> .font {
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Brain Dementia Prediction Model</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload File(csv)", type =["csv"])
    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)
        
        #check the csv validation
        df_norm = normalizer.transform(uploaded_df)
        prediction = classifier.predict_proba(df_norm)
        output='{0:.{1}f}'.format(prediction[0][1], 2)
        output = (float(output) * 100)
        output_string = "Chances of getting Dementia is "+str(output)+"%"
        st.markdown(f'<h1 style="font-family:sans-serif;color:Blue;font-size:20px;">{output_string}</h1>', unsafe_allow_html=True)
    with st.form(key='dimentia_form', clear_on_submit=True): 
        st.subheader("Enter Values: ")
        col1, col2, col3 = st.columns([5,5,5])
        with col1:
            cerad=st.selectbox(label='CERAD Score: ', options=('0','1','2','3'), key='1')
            ihc_at8_ffpe =st.text_input(label='IHC AT8 Immunreactivity (FFPE): ', key='2')
            ihc_a_beta=st.text_input(label='IHC Amyloid Beta: ', key='3')
            vegf_pg_per_mg=st.text_input(label='Vascular endothelial growth factor (per mg): ', key='4')
            ab42_over_ab40_ratio=st.text_input(label='Alpha-synuclein (per mg): ', key='5')
        with col2:
            braak= st.selectbox(label='Braak Stage: ', options=('0','1','2','3', '4','5','6'), key='6')
            ihc_at8=st.text_input(label='IHC AT8 Immunreactivity: ', key='7')
            ihc_gfap_ffpe=st.text_input(label='IHC GFAP Immunreactivity (FFPE): ', key='8')
            ptau_over_tau_ratio=st.text_input(label='Ratio of ABeta40 to Abeta42: ', key='9') 
            a_syn_pg_per_mg=st.text_input(label='Monocyte Chemotactic Protein 1: ', key='10')
        with col3:
            ihc_tau2_ffpe=st.text_input(label='IHC Tau Protien (FFPE): ', key='11')
            ihc_a_beta_ffpe=st.text_input(label='IHC Amyloid Beta (FFPE): ', key='12')
            ptau_ng_per_mg=st.text_input(label='Phosphorylated Tau: ', key='13')
            mcp_1_pg_per_mg=st.text_input(label='Ratio of Phosphorylated Tau to all Tau: ', key='14')
            ab42_pg_per_mg=st.text_input(label='Beta-amyloid 1-42: ', key='15')
            
        submitted = st.form_submit_button('Submit')
        if submitted:
            #st.write(dimentia_form)
            validation_form = False
            form_list_values = []
            form_list_values.append(float(cerad))
            form_list_values.append(float(braak))
           
            if ihc_tau2_ffpe.strip() and (0 < float(ihc_tau2_ffpe) < 1):
                form_list_values.append(float(ihc_tau2_ffpe))
            else:
                validation_form = True
                st.error("IHC Tau Protien (FFPE) should be in between 0 and 1")
            
            if ihc_at8_ffpe.strip() and (0 < float(ihc_at8_ffpe) < 1):
                form_list_values.append(float(ihc_at8_ffpe))
            else:
                validation_form = True
                st.error("IHC AT8 Immunreactivity (FFPE) should be in between 0 and 1")
                        
            if ihc_at8.strip() and (0 < float(ihc_at8) < 1):
                form_list_values.append(float(ihc_at8))
            else:
                validation_form = True
                st.error("IHC AT8 Immunreactivity should be in between 0 and 1")
            
            if ihc_a_beta_ffpe.strip() and (0 < float(ihc_a_beta_ffpe) < 1):
                form_list_values.append(float(ihc_a_beta_ffpe))
            else:
                validation_form = True
                st.error("IHC Amyloid Beta (FFPE) should be in between 0 and 1")
            
            if ihc_a_beta.strip() and (0 < float(ihc_a_beta) < 1):
                form_list_values.append(float(ihc_a_beta))
            else:
                validation_form = True
                st.error("IHC Amyloid Beta should be in between 0 and 1")
            
            if ihc_gfap_ffpe.strip() and (0 < float(ihc_gfap_ffpe) < 1):
                form_list_values.append(float(ihc_gfap_ffpe))
            else:
                validation_form = True
                st.error("IHC GFAP Immunreactivity (FFPE) should be in between 0 and 1")
            
            if ptau_ng_per_mg.strip() and (0 < float(ptau_ng_per_mg) < 7):
                form_list_values.append(float(ptau_ng_per_mg))
            else:
                validation_form = True
                st.error("Phosphorylated Tau should be in between 0 and 7")
            
            if vegf_pg_per_mg.strip() and (0 < float(vegf_pg_per_mg) < 9):
                form_list_values.append(float(vegf_pg_per_mg))
            else:
                validation_form = True
                st.error("Vascular endothelial growth factor (per mg) should be in between 0 and 9")
            
            if ab42_over_ab40_ratio.strip() and (0 < float(ab42_over_ab40_ratio) < 1000):
                form_list_values.append(float(ab42_over_ab40_ratio))
            else:
                validation_form = True
                st.error("Ratio of ABeta40 to Abeta42 should be in between 0 and 1000")
            
            if ptau_over_tau_ratio.strip() and (0 < float(ptau_over_tau_ratio) < 7):
                form_list_values.append(float(ptau_over_tau_ratio))
            else:
                validation_form = True
                st.error("Ratio of phosphorylated tau to all tau should be in between 0 and 7")

            if a_syn_pg_per_mg.strip() and (0 < float(a_syn_pg_per_mg) < 3):
                form_list_values.append(float(a_syn_pg_per_mg))
            else:
                validation_form = True
                st.error("Alpha-synuclein (per mg) should be in between 0 and 3")
            
            if mcp_1_pg_per_mg.strip() and (0 < float(mcp_1_pg_per_mg) < 262):
                form_list_values.append(float(mcp_1_pg_per_mg))
            else:
                validation_form = True
                st.error("Monocyte chemotactic protein 1 should be in between 0 and 262")
            
            if ab42_pg_per_mg.strip() and (0 < float(ab42_pg_per_mg) < 652):
                form_list_values.append(float(ab42_pg_per_mg))
            else:
                validation_form = True
                st.error("Beta-Amyloid 1-42 should be in between 0 and 652")
            
            if not validation_form:
                df_model = pd.DataFrame(columns = form_list_lables)
                df_model.loc[len(df_model)] = form_list_values
                df_norm = normalizer.transform(df_model)
                prediction = classifier.predict_proba(df_norm)
                
                output='{0:.{1}f}'.format(prediction[0][1], 2)
                output = (float(output) * 100)
                output_string = "Chances of getting Dementia is "+str(output)+"%"
                st.markdown(f'<h1 style="font-family:sans-serif;color:Blue;font-size:20px;">{output_string}</h1>', unsafe_allow_html=True)
            else:
                st.error('Please enter the correct data!!!')
            