import streamlit as st
import math

# Function to calculate LMTD
def calculate_lmtd(t_hot_in, t_hot_out, t_cold_in, t_cold_out):
    delta_t1 = t_hot_in - t_cold_out
    delta_t2 = t_hot_out - t_cold_in

    if delta_t1 == delta_t2:
        return delta_t1  # Special case when delta_t1 == delta_t2 (LMTD is just delta T)
    else:
        return (delta_t1 - delta_t2) / math.log(delta_t1 / delta_t2)

# Function to calculate heat duty (Q)
def calculate_heat_duty(heat_transfer_coefficient, area, lmtd):
    return heat_transfer_coefficient * area * lmtd

# Title of the app
st.title("Heat Exchanger Performance Calculator")

# Input fields for temperatures
st.header("Input Temperatures")
t_hot_in = st.number_input("Hot fluid inlet temperature (°C)", value=150.0)
t_hot_out = st.number_input("Hot fluid outlet temperature (°C)", value=100.0)
t_cold_in = st.number_input("Cold fluid inlet temperature (°C)", value=20.0)
t_cold_out = st.number_input("Cold fluid outlet temperature (°C)", value=80.0)

# Input fields for heat transfer coefficient and area
st.header("Heat Exchanger Specifications")
heat_transfer_coefficient = st.number_input("Heat transfer coefficient (W/m²·K)", value=500.0)
area = st.number_input("Heat exchanger area (m²)", value=10.0)

# Calculate LMTD
lmtd = calculate_lmtd(t_hot_in, t_hot_out, t_cold_in, t_cold_out)

# Calculate Heat Duty (Q)
heat_duty = calculate_heat_duty(heat_transfer_coefficient, area, lmtd)

# Display results
st.header("Results")
st.write(f"Log Mean Temperature Difference (LMTD): {lmtd:.2f} °C")
st.write(f"Heat Duty (Q): {heat_duty:.2f} W")

# Add a conclusion or notes
st.write("This calculator helps you estimate the performance of a heat exchanger based on fluid temperatures and heat exchanger specifications.")
