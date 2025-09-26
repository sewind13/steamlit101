import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Title ---
st.title("Charts in Streamlit")

# --- Generate Sample Data ---
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# --- Area Chart ---
st.subheader("Area Chart")
st.area_chart(chart_data)

# --- Bar Chart ---
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# --- Line Chart ---
st.subheader("Line Chart")
st.line_chart(chart_data)

# --- Scatter Plot ---
st.subheader("Scatter Plot")
scatter_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['x', 'y']
)
st.write("Scatter plot of random points:")
st.scatter_chart(scatter_data)

# Map selecttion (displaying random points on a map)
st.subheader("Map with Random Points")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

# --- Pyplot Chart ---
st.subheader("Matplotlib Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(chart_data['a'], label='a')
ax.plot(chart_data['b'], label='b')
ax.plot(chart_data['c'], label='c')
ax.set_title('Line Plot from Matplotlib')
ax.legend()
st.pyplot(fig)