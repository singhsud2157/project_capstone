import plotly.graph_objects as go
import pandas as pd
import numpy as np
import random
import plotly.express as px
from plotly.offline import plot
from helper.load_data import *

files_to_merge_1_list = ['DonorInformation.csv', 'ProteinAndPathologyQuantifications.csv']

def get_med_chart_1():
    df_list = get_dataframe_list(files_to_merge_1_list)
    df_main = merge_dataframe_list(df_list,'donor_id')
    d_list = ['ptau_ng_per_mg','ab42_pg_per_mg','ab40_pg_per_mg','ihc_at8','braak', 'sex']
    df_plot = df_main[d_list]
    df_plot.sex.replace(['M', 'F'], [1, 0], inplace=True)
    #print(df_plot.head(5))
    #print(df_plot.max().to_frame().T)
    #print(df_plot.min().to_frame().T)
    fig = px.parallel_coordinates(df_plot, color="ptau_ng_per_mg", labels=d_list, color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
    fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
    return fig

def get_mad_chart_2():
    df_list = get_dataframe_list(files_to_merge_1_list)
    df_main = merge_dataframe_list(df_list,'donor_id')
    d_list = ['ptau_ng_per_mg','ab42_pg_per_mg','ab40_pg_per_mg','ihc_at8','braak', 'sex']
    df_plot = df_main[d_list]
    df_plot.sex.replace(['M', 'F'], [1, 0], inplace=True)
    print(df_plot.head(5))
    
    fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = df_plot['ptau_ng_per_mg'],
                   colorscale = 'Electric',
                   showscale = True,
                   cmin = -4000,
                   cmax = -100),
        dimensions = list([
            dict(range = [0,7],
                 label = "ptau_ng_per_mg", values = df_plot['ptau_ng_per_mg']),
            dict(range = [0,700],
                 label = 'ab42_pg_per_mg', values = df_plot['ab42_pg_per_mg']),
            dict(range = [0,1000],
                 label = 'ab40_pg_per_mg', values = df_plot['ab40_pg_per_mg']),
            dict(range = [0,2],
                 label = 'ihc_at8', values = df_plot['ihc_at8']),
            dict(range = [0,6],
                 visible = True,
                 label = 'braak', values = df_plot['braak']),
            dict(range = [0,1],
                 label = 'sex', values = df_plot['sex'])])
    )
)
    return fig

def get_mad_chart_3():
     metrics_df = get_data_frame('ProteinAndPathologyQuantifications.csv')
     donor_df = get_data_frame('DonorInformation.csv')  
     d1=donor_df["age"][donor_df['age']=="90-94"]
     for i in range(0, len(d1.index)):
          donor_df.loc[d1.index[i], 'age'] = random.randint(90, 94)

     d2=donor_df["age"][donor_df['age']=="95-99"]
     for i in range(0, len(d2.index)):
          donor_df.loc[d2.index[i], 'age'] = random.randint(95, 99)

     d3=donor_df["age"][donor_df['age']=="100+"]
     for i in range(0, len(d3.index)):
          donor_df.loc[d3.index[i], 'age'] = random.randint(100, 105)

     donor_df['age'] = donor_df['age'].astype(int) 

     metrics_donor_df = pd.merge(metrics_df, donor_df,  how='left', left_on='donor_name', right_on = 'name')
     
     region_braak= metrics_donor_df.groupby(['structure_acronym', 'braak'])['donor_name'].aggregate(np.ma.count)
     region_braak_df =pd.DataFrame(region_braak)
     region_braak_df.reset_index(inplace=True)
     region_braak_df['structure_acronym']=  region_braak_df['structure_acronym'].map({'FWM': 0, 'HIP': 1, 'PCx':2, 'TCx':3})
     region_braak_df['braak'] = region_braak_df['braak']+4

     source_list = list(region_braak_df['structure_acronym'])
     target_list = list(region_braak_df['braak'])
     value_list =list(region_braak_df['donor_name'])

     braak_dementia= metrics_donor_df.groupby(['braak', 'act_demented'])['donor_name'].aggregate(np.ma.count)
     braak_dementia_df =pd.DataFrame(braak_dementia)
     braak_dementia_df.reset_index(inplace=True)
     braak_dementia_df['act_demented']=  braak_dementia_df['act_demented'].map({'Dementia': 1, 'No Dementia': 0})
     braak_dementia_df['braak'] = braak_dementia_df['braak']+4
     braak_dementia_df['act_demented'] = braak_dementia_df['act_demented']+11
  

     source_list =source_list + list(braak_dementia_df['braak'])
     target_list = target_list+ list(braak_dementia_df['act_demented'])
     value_list = value_list+ list(braak_dementia_df['donor_name'])


     fig = go.Figure(data=[go.Sankey(
     node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ['FWM', 'HIP', 'PCx', 'TCx', '0', '1','2','3', '4', '5', '6', 'No Dementia', 'Dementia'],
        x = [0.001, 0.001,0.001, 0.001, 0.5, 0.5, 0.5, 0.5,0.5, 0.5, 0.5, 0.999, 0.999 ],
        y=[0.001, 0.33, 0.66, 0.999, 0.99, 0.83, 0.66, 0.49, 0.32, 0.15, 0.001, 0.1, 0.8],
      color = "blue"
    ),
    link = dict(
      source = source_list, 
      target = target_list,
      value = value_list
      ))])

     fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
     return fig