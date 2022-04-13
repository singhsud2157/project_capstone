import streamlit as st

def get_model_form():
    st.markdown(""" <style> .font {
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Brain Dementia Prediction Model</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload File(csv)")
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        #col, buff, buff2 = st.columns([1,1,4])
        st.subheader("Enter Values: ")
        cerad=st.text_input(label='cerad: ') #Collect user feedback
        braak=st.text_input(label='braak: ') #Collect user feedback
        ihc_tau2_ffpe=st.text_input(label='ihc_tau2_ffpe: ') #Collect user feedback
        ihc_at8_ffpe =st.text_input(label='ihc_at8_ffpe: ') #Collect user feedback
        ihc_at8=st.text_input(label='ihc_at8: ') #Collect user feedback
        ihc_a_beta_ffpe=st.text_input(label='ihc_a_beta_ffpe: ') #Collect user feedback
        ihc_a_beta=st.text_input(label='ihc_a_beta: ') #Collect user feedback
        ihc_gfap_ffpe=st.text_input(label='ihc_gfap_ffpe: ') #Collect user feedback
        ptau_ng_per_mg=st.text_input(label='ptau_ng_per_mg: ') #Collect user feedback
        vegf_pg_per_mg=st.text_input(label='vegf_pg_per_mg: ') #Collect user feedback
        ab42_over_ab40_ratio=st.text_input(label='ab42_over_ab40_ratio: ') #Collect user feedback
        ptau_over_tau_ratio=st.text_input(label='ptau_over_tau_ratio: ') #Collect user 
        a_syn_pg_per_mg=st.text_input(label='a_syn_pg_per_mg: ') #Collect user feedback
        mcp_1_pg_per_mg=st.text_input(label='mcp_1_pg_per_mg: ') #Collect user feedback
        #buff, col, buff2 = st.columns([1,1,4])
        ab42_pg_per_mg=st.text_input(label='ab42_pg_per_mg: ') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Dimentia')