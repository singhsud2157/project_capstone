import streamlit as st
from streamlit_option_menu import option_menu
from helper.about import abount_main
from helper.contact import contact_main
from helper.select_data import get_file_list, get_data_frame
from helper.display_data import display_main
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from helper.altair_chart import show_altair

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
    
    with st.sidebar:
        choose = option_menu("Capstone", ["About", "Project Planning", "Data", "Chart", "Prediction", "Contact"],
                         icons=['house', 'kanban', 'camera fill', 'book', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "orange"},
    }
    )
    
    if choose == 'About':
        abount_main()
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
    
    elif choose == 'Chart':
        # list =get_file_list()
        # add_selectbox = st.sidebar.selectbox("### Select the data file :",list)
        # df = get_data_frame(add_selectbox)
        # st.bar_chart(df)
        #display_main(df) 
        st.altair_chart(show_altair())
    elif choose == 'Contact':
        contact_main()
    
if __name__ == '__main__':
    main()
        