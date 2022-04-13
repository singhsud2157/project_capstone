import random

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import plotly

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

def get_mad_chart_2_o():
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

def get_mad_chart_2():
     df_list = get_dataframe_list(files_to_merge_1_list)
     df_main = merge_dataframe_list(df_list,'donor_id')
    
     df_main.apo_e4_allele.replace(['Y', 'N'], [1, 0], inplace=True)
     df_main.act_demented.replace(['No Dementia', 'Dementia'], [1, 0], inplace=True)
     df_main['apo_e4_allele'] = df_main['apo_e4_allele'].fillna(2)
     df_main['apo_e4_allele'] = df_main['apo_e4_allele'].astype(int)
     df_main['act_demented'] = df_main['act_demented'].astype(int)
    
     d_list = ['donor_id','cerad', 'braak', 'apo_e4_allele','num_tbi_w_loc', 'act_demented','ihc_at8', 'ihc_a_beta', 'a_syn_pg_per_mg']
     df_plot = df_main[d_list]
        
     fig = go.Figure(data=
     go.Parcoords(
        line = dict(color = df_plot['cerad'],
                   colorscale = 'Electric',
                   showscale = True,
                   cmin = 0,
                   cmax = 7),
        dimensions = list([
            dict(range = [0,3],
                 label = 'cerad', values = df_plot['cerad']),
            dict(range = [0,8],
                 label = 'braak', values = df_plot['braak']),
            dict(range = [0,2],
                 label = 'apo_e4_allele', values = df_plot['apo_e4_allele']),
            dict(range = [0,3],
                 visible = True,
                 label = 'num_tbi_w_loc', values = df_plot['num_tbi_w_loc']),
            dict(range = [0.000018,0.112065],
                 visible = True,
                 label = 'ihc_at8', values = df_plot['ihc_at8']),
            dict(range = [0.000157,0.088290],
                 visible = True,
                 label = 'ihc_a_beta', values = df_plot['ihc_a_beta']),
            dict(range = [0.020000,2.556488],
                 visible = True,
                 label = 'a_syn_pg_per_mg', values = df_plot['a_syn_pg_per_mg']),
            dict(range = [0,1],
                 visible = True,
                 label = 'act_demented', values = df_plot['act_demented'])])
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

     nodecolor_list= ['rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)', 'rgba(214, 39, 40, 0.8)', 
                 'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)', 'rgba(227, 119, 194, 0.8)', 'rgba(127, 127, 127, 0.8)',
                 'rgba(188, 189, 34, 0.8)', 'rgba(23, 190, 207, 0.8)', 'rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', 
                 'rgba(44, 160, 44, 0.8)']
     opacity = 0.4

     linkcolor_list = [nodecolor_list[src].replace("0.8", str(opacity)) for src in source_list]
     
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
      value = value_list,
      color = linkcolor_list  
      ))])

     fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
     return fig
