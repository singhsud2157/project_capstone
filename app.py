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
        chart_list = ['parallel_chart', 'sanky1','sanky2','sanky3']
        chart_selectbox = st.sidebar.selectbox("Select the chart",chart_list)
        if chart_selectbox == 'parallel_chart':
            st.plotly_chart(get_med_chart_1(), use_container_width=True)
        elif chart_selectbox == 'sanky1':
            st.plotly_chart(get_med_sanky_chart_1(), use_container_width=True)
        elif chart_selectbox == 'sanky2':
            st.plotly_chart(get_med_sanky_chart_2(), use_container_width=True)
        elif chart_selectbox == 'sanky3':
            st.plotly_chart(get_med_sanky_chart_3(), use_container_width=True)
    elif choose == 'Dementia Prediction':
        get_model_form()
    elif choose == 'Feedback/Queries':
        contact_main()
    
if __name__ == '__main__':
    main()
        