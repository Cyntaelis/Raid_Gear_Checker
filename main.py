import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("./tome_raid.csv", header=0)

st.title("Raid Gear BiS Checker")
st.dataframe(df)
