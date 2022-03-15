from logging import exception
import streamlit as st
from os import listdir
import data_files
import pandas as pd

path_to_dir = 'data_files'

@st.cache
def get_file_list():
    filenames_list = listdir(path_to_dir)
    csv_files_list = list(filter(lambda f: f.endswith('.csv'), filenames_list))
    return csv_files_list

@st.cache
def get_data_frame(filename):
    file_path = path_to_dir + '/' + filename
    df = pd.read_csv(file_path)
    return df
