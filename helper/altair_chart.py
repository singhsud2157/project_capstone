import streamlit as st
import altair as alt
import pandas as pd
import data_files
import matplotlib.pyplot as plt

def visualize_chart_data(df, x_axis, y_axis, column_list):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color=x_axis
    ).properties(
    width=500,
    height=500
    ).interactive()
    return graph