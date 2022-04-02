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

def display_scatter_chart(df, x_axis, y_axis, column_list):
     if x_axis and y_axis:
        scatter_fig = plt.figure(figsize=(6,4))
        scatter_ax = scatter_fig.add_subplot(111)

        malignant_df = df[df["target"] == "malignant"]
        benign_df = df[df["target"] == "benign"]

        malignant_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="tomato", alpha=0.6, ax=scatter_ax, label="Malignant")
        benign_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                            title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label="Benign")