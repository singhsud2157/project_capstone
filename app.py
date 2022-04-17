from cmath import e
import streamlit as st
from streamlit_option_menu import option_menu
from helper.about import abount_main, about_project
from helper.contact import contact_main
from helper.select_data import get_file_list, get_data_frame
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from helper.altair_chart import *
from helper.medical_chart import *
from helper.model_form import *

def main():
    st.set_page_config(layout="wide")
    #st.title("Capstone project")
    # with st.sidebar:
    #     selected = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #         icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #         menu_icon="cast", default_index=0)
    
    # choose = option_menu(None, ["About", "Data", "Chart", "Prediction", "Contact"], 
    #     #icons=['house', 'kanban', 'camera fill', 'book', 'book','person lines fill'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal")

#     selected = option_menu(None, ["About", "Data",  "Charts", "Prediction","Settings"], 
#         icons=['house', 'cloud-upload','house','house', 'gear'], 
#         menu_icon="cast", default_index=0, orientation="horizontal",
#         styles={
#         "container": {"padding": "5!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "orange"},
#     }
# )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    with st.sidebar:
        choose = option_menu("Aging, Dementia, and TBI Study", ["About Team", "Study Findings", "Data",  "Data Exploration","Visual Exploration", "Dementia Prediction", "Feedback/Queries"],
                         icons=['house', 'kanban', 'camera fill', 'book','book', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "orange"},
    }
    )
    
    if choose == 'About Team':
        abount_main()
    elif choose == 'Study Findings':
        about_project()
    elif choose == 'Data':
        list =get_file_list()
        add_selectbox = st.sidebar.selectbox("Select the data file",list)
        df = get_data_frame(add_selectbox)
        #st.dataframe(df)
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination()
        gb.configure_side_bar()
        gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
        gridOptions = gb.build()

        AgGrid(df, height=800,gridOptions=gridOptions,  enable_enterprise_modules=False)
    elif choose == 'Data Exploration':
        st.title("Data Exploration")
        file_list =get_file_list()
        select_file_name_list = st.multiselect("Select the file:", options=file_list, default=file_list[0])
        if select_file_name_list :
            merge_df = get_merge_dataframe(select_file_name_list)
            if merge_df.empty:
                st.error('Wrong selection of files')
            else:
                non_floats = []
                try:
                    for col in merge_df:
                        if (merge_df[col].dtypes != "float64") and (merge_df[col].dtypes != "int64"):
                            non_floats.append(col)
                    if(len(non_floats) >0):
                        merge_df = merge_df.drop(columns=non_floats)
                except Exception as e:
                    print('error', e)
                column_list = merge_df.columns
                x_axis = st.selectbox("Choose a variable for the x-axis:", column_list, index=0)
                y_axis = st.selectbox("Choose a variable for the y-axis:", column_list, index=1)
                graph = visualize_chart_data(merge_df, x_axis, y_axis, column_list)
                st.write(graph)
    elif choose == 'Visual Exploration':
        chart_list = ['parallel_chart', 'Brain_Braak_Dimentia','Braak_pTau_Dementia','Cerad_Aβ_Dementia']
        chart_selectbox = st.sidebar.selectbox("Select the chart",chart_list)
        if chart_selectbox == 'parallel_chart':
            st.plotly_chart(get_med_chart_1(), use_container_width=True)
        elif chart_selectbox == 'Brain_Braak_Dimentia':
            st.plotly_chart(get_med_sanky_chart_1(), use_container_width=True)
            st.write("The above Sankey diagram depicts the relationship between brain region, Braak stage and dementia status. " +
                     "The left column shows the four brain regions, the middle column shows the 7 Braak stage number. "+ 
                     "The right column shows the two dementia status. The width of each arrow between columns and the height of each bar of the column are based on the quantity."+
                     "We can observe that samples are evenly distributed among 4 brain regions. Very few samples have Braak stage of 0." +
                     "More samples have Braak stage of 3 than any other stage. Most samples with Braak stage of 5 or 6 have dementia " +
                     "and most samples with Braak stage of 1 , 2 or 3 have no dementia. Almost half of the samples with Braak stage of 4 have dementia."
                    )
            st.write("If you want to know more about Braak stage, please read our blog post.")
        elif chart_selectbox == 'Braak_pTau_Dementia':
            st.plotly_chart(get_med_sanky_chart_2(), use_container_width=True)
            st.write("We used AT8 IHC level to represent pTau protein level in the brain tissues. AT8 IHC and pTau are strongly correlated " +
                     "(Pearson correlation coefficient is 0.68). We scaled the AT8 IHC reading to values between 0 and 1," +
                     "then evenly divide the range to 5 bins. So the Bin 1 represents the range between 0.0 and 0.20. " + 
                     "Bin 5 represents the range between 0.81 and 1.0.We can observe that later Braak stages are associated with higher pTau levels. "+
                     "2/3 of the samples with Braak Stage 6 have pTau protein level 2 and above while 1/6 of the samples with Braak Stage 1 have pTau protein level 2 and above." +
                     "More samples with higher pTau protein level have dementia. 38% of the samples with pTau protein level 1 " +
                     "have dementia while 86% of the samples with pTau level 5 have deme")
            st.write("If you want to know more about Braak stage, AT8 IHC and pTau protein, please read our blog post.")
        elif chart_selectbox == 'Cerad_Aβ_Dementia':
            st.plotly_chart(get_med_sanky_chart_3(), use_container_width=True)
            st.write("We used Aβ IHC level to represent Aβ protein level in the brain tissues. We scaled the Aβ IHC reading to values between 0 and 1, " +
                     "then evenly divide the range to 5 bins. So the Bin 1 represents the range between 0.0 and 0.20. Bin 5 represents the range between 0.81 and 1.0. "+
                     "We can observe that higher CERAD scores are associated with higher Aβ protein levels. 51% of the samples with CERAD score 3 "+
                     "have Aβ protein level 2 and above while only 3% of the samples with CERAD score 0 have Aβ protein level 2. " +
                     "There is no clear correlation of Aβ protein level and dementia from this chart as almost half of the samples of various Aβ protein level have dementia.")
            st.write("If you want to know more about CERAD score , Aβ protein, please read our blog post.")
    elif choose == 'Dementia Prediction':
        get_model_form()
    elif choose == 'Feedback/Queries':
        contact_main()
    
if __name__ == '__main__':
    main()
        