import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data
import data_files


def show_altair():
    
    airports = pd.read_csv("data_files/airports.csv")
    flights_airport = pd.read_csv("data_files/flights-airport.csv")
        
    states = alt.topo_feature(data.us_10m.url, feature="states")
    # Create mouseover selection
    select_city = alt.selection_single(
        on="mouseover", nearest=True, fields=["origin"], empty="none"
    )
    # Define which attributes to lookup from airports.csv
    lookup_data = alt.LookupData(
        airports, key="iata", fields=["state", "latitude", "longitude"]
    )
    background = alt.Chart(states).mark_geoshape(
        fill="lightgray",
        stroke="white"
    ).properties(
        width=750,
        height=500
    ).project("albersUsa")
    connections = alt.Chart(flights_airport).mark_rule(opacity=0.35).encode(
        latitude="latitude:Q",
        longitude="longitude:Q",
        latitude2="lat2:Q",
        longitude2="lon2:Q"
    ).transform_lookup(
        lookup="origin",
        from_=lookup_data
    ).transform_lookup(
        lookup="destination",
        from_=lookup_data,
        as_=["state", "lat2", "lon2"]
    ).transform_filter(
        select_city
    )
    
    points = alt.Chart(flights_airport).mark_circle().encode(
        latitude="latitude:Q",
        longitude="longitude:Q",
        size=alt.Size("routes:Q", scale=alt.Scale(range=[0, 1000]), legend=None),
        order=alt.Order("routes:Q", sort="descending"),
        tooltip=["origin:N", "routes:Q"]
    ).transform_aggregate(
        routes="count()",
        groupby=["origin"]
    ).transform_lookup(
        lookup="origin",
        from_=lookup_data
    ).transform_filter(
        (alt.datum.state != "PR") & (alt.datum.state != "VI")
    ).add_selection(
        select_city
    )
    
    return (background + connections + points).configure_view(stroke=None)