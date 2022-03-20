import plotly.graph_objects as go
import pandas as pd
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