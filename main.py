import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="BiS Checker",
    page_icon="crossed_swords",
    layout="wide",
)
df = pd.read_csv("./tome_raid.csv", header=0)
st.title("Raid Gear BiS Checker")
st.subheader("Check = Raid Gear")
st.markdown("[Code available here](https://github.com/Cyntaelis/Raid_Gear_Checker/)", unsafe_allow_html=True)
st.dataframe(df)

