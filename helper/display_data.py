import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

def display_main(dataframe):

    st.markdown("## Brain Dataset Analysi capstones")   ## Main Title

################# Scatter Chart Logic #################

    st.sidebar.markdown("### Scatter Chart: Explore Relationship Between Measurements :")

    #measurements = dataframe.drop(labels=["target"], axis=1).co
    # lumns.tolist()
    measurements = dataframe.columns.tolist()
    x_axis = st.sidebar.selectbox("X-Axis", measurements)
    y_axis = st.sidebar.selectbox("Y-Axis", measurements, index=1)
    
    if x_axis and y_axis:
        scatter_fig = plt.figure(figsize=(6,4))

        scatter_ax = scatter_fig.add_subplot(111)

        # malignant_df = dataframe[dataframe["target"] == x_axis]
        # benign_df = dataframe[dataframe["target"] == y_axis]
        malignant_df = dataframe[dataframe[x_axis]]
        benign_df = dataframe[dataframe[y_axis]]

        malignant_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="tomato", alpha=0.6, ax=scatter_ax, label="Malignant")
        benign_df.plot.scatter(x=x_axis, y=y_axis, s=120, c="dodgerblue", alpha=0.6, ax=scatter_ax,
                           title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()), label="Benign");




########## Bar Chart Logic ##################

    st.sidebar.markdown("### Bar Chart: Average Measurements Per Tumor Type : ")

    avg_dataframe = dataframe.groupby("target").mean()
    bar_axis = st.sidebar.multiselect(label="Average Measures per Tumor Type Bar Chart",
                                  options=measurements,
                                  default=["mean radius","mean texture", "mean perimeter", "area error"])

    if bar_axis:
        bar_fig = plt.figure(figsize=(6,4))
        bar_ax = bar_fig.add_subplot(111)
        sub_avg_dataframe = avg_dataframe[bar_axis]
        sub_avg_dataframe.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");

    else:
        bar_fig = plt.figure(figsize=(6,4))
        bar_ax = bar_fig.add_subplot(111)
        sub_avg_dataframe = avg_dataframe[["mean radius", "mean texture", "mean perimeter", "area error"]]
        sub_avg_dataframe.plot.bar(alpha=0.8, ax=bar_ax, title="Average Measurements per Tumor Type");

################# Histogram Logic ########################

    st.sidebar.markdown("### Histogram: Explore Distribution of Measurements : ")

    hist_axis = st.sidebar.multiselect(label="Histogram Ingredient", options=measurements, default=["mean radius", "mean texture"])
    bins = st.sidebar.radio(label="Bins :", options=[10,20,30,40,50], index=4)

    if hist_axis:
        hist_fig = plt.figure(figsize=(6,4))
        hist_ax = hist_fig.add_subplot(111)
        sub_dataframe = dataframe[hist_axis]
        sub_dataframe.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");
    else:
        hist_fig = plt.figure(figsize=(6,4))
        hist_ax = hist_fig.add_subplot(111)
        sub_dataframe = dataframe[["mean radius", "mean texture"]]
        sub_dataframe.plot.hist(bins=bins, alpha=0.7, ax=hist_ax, title="Distribution of Measurements");

#################### Hexbin Chart Logic ##################################

    st.sidebar.markdown("### Hexbin Chart: Explore Concentration of Measurements :")
    hexbin_x_axis = st.sidebar.selectbox("Hexbin-X-Axis", measurements, index=0)
    hexbin_y_axis = st.sidebar.selectbox("Hexbin-Y-Axis", measurements, index=1)

    if hexbin_x_axis and hexbin_y_axis:
        hexbin_fig = plt.figure(figsize=(6,4))
        hexbin_ax = hexbin_fig.add_subplot(111)

        dataframe.plot.hexbin(x=hexbin_x_axis, y=hexbin_y_axis,
                                 reduce_C_function=np.mean,
                                 gridsize=25,
                                 #cmap="Greens",
                                 ax=hexbin_ax, title="Concentration of Measurements");

##################### Layout Application ##################

    container1 = st.container()
    col1, col2 = st.columns(2)

    with container1:
        with col1:
            scatter_fig
        with col2:
            bar_fig


    container2 = st.container()
    col3, col4 = st.columns(2)

    with container2:
        with col3:
            hist_fig
        with col4:
            hexbin_fig
