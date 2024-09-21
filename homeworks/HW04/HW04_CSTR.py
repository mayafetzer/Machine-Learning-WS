import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and Description
st.title("CSTR and PFR Reactor Volume Calculator for First-Order Reactions")
st.write("""
This app calculates the reactor volume for both CSTR and PFR given the feed rate, rate constant, and target conversion. 
You can also compare the performance of both reactors by observing the volume required to achieve the same conversion, 
and plot the conversion profile for the PFR along the reactor length.
""")

# Input parameters
st.sidebar.header("Input Parameters")

# Feed rate (F_A0)
FA0 = st.sidebar.number_input("Feed rate (mol/s)", min_value=0.1, max_value=100.0, value=10.0, step=0.1)

# Reaction rate constant (k)
k = st.sidebar.number_input("Reaction rate constant (1/s)", min_value=0.001, max_value=1.0, value=0.1, step=0.01)

# Conversion (X)
X = st.sidebar.slider("Conversion (X)", min_value=0.0, max_value=1.0, value=0.75, step=0.01)

# CSTR Volume Calculation
if FA0 > 0 and k > 0:
    V_CSTR = FA0 * X / (k * (1 - X))
    st.write(f"**CSTR Volume required for {X * 100}% conversion:** {V_CSTR:.2f} m³")

# PFR Volume Calculation
if FA0 > 0 and k > 0:
    V_PFR = FA0 / k * np.log(1 / (1 - X))
    st.write(f"**PFR Volume required for {X * 100}% conversion:** {V_PFR:.2f} m³")

# Compare Reactor Volumes
if V_CSTR and V_PFR:
    st.write(f"### Performance Comparison:")
    st.write(f"The required volume for CSTR is {V_CSTR:.2f} m³, whereas for PFR it is {V_PFR:.2f} m³.")
    st.write("PFR requires less volume than CSTR for the same conversion.")

# PFR Conversion Profile
st.write("### PFR Conversion Profile:")
length = np.linspace(0, V_PFR, 100)
X_PFR_profile = 1 - np.exp(-k * length / FA0)

plt.figure()
plt.plot(length, X_PFR_profile, label="PFR Conversion")
plt.xlabel("Reactor Volume (m³)")
plt.ylabel("Conversion")
plt.title("PFR Conversion Profile")
plt.grid(True)
plt.legend()
st.pyplot(plt)

# CSTR Conversion vs Volume plot
st.write("### CSTR Conversion vs Reactor Volume:")
V_CSTR_range = np.linspace(0.1, V_CSTR, 100)
X_CSTR_range = 1 - (FA0 / (k * V_CSTR_range + FA0))

plt.figure()
plt.plot(V_CSTR_range, X_CSTR_range, label="CSTR Conversion")
plt.xlabel("Reactor Volume (m³)")
plt.ylabel("Conversion")
plt.title("CSTR Conversion vs Reactor Volume")
plt.grid(True)
plt.legend()
st.pyplot(plt)
