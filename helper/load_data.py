from logging import exception
from os import listdir
from functools import reduce
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from plotly.offline import plot


path_to_dir = 'data_files'

def get_file_list():
    filenames_list = listdir(path_to_dir)
    csv_files_list = list(filter(lambda f: f.endswith('.csv'), filenames_list))
    return csv_files_list

def get_column_name(filename):
    column_list = []
    df = get_data_frame(filename)
    column_list = df.columns
    return column_list

def get_data_frame(filename):
    file_path = path_to_dir + '/' + filename
    df = pd.read_csv(file_path)
    return df

def get_dataframe_list(filename_list):
    df_list = []
    for filename in filename_list:
        df_list.append(get_data_frame(filename))
    return df_list
        
def merge_two_dataframe(df1, df2, merge_on):
    df = pd.merge(df1,df2, on = merge_on)
    print(df.head(5))
    return df

def merge_dataframe_list(df_list, merge_on)    :
    return reduce(lambda x,y: pd.merge(x,y, on=merge_on, how='outer'), df_list)
    
def get_merge_dataframe(file_name_list):
    df_list  = get_dataframe_list(file_name_list)
    main_list = []
    for df in df_list:
        list_a = df.columns.values.tolist()
        main_list.append(list_a)
    common_element_list = [ele[0] for ele in zip(*main_list) if len(set(ele)) == 1]
#   print(common_element_list)
    df_merge = pd.DataFrame()
    if len(common_element_list) > 0:
        df_merge = merge_dataframe_list(df_list, common_element_list[0]) 
    return df_merge