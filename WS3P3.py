import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
WATER_DENSITY = 997  # kg/m^3 (Density of water at 25°C)
WATER_VISCOSITY = 0.001  # Pa·s (Viscosity of water at 25°C)

# Function to calculate Reynolds number
def calculate_reynolds_number(flow_rate, diameter, density, viscosity):
    velocity = (4 * flow_rate) / (np.pi * diameter ** 2)
    reynolds_number = (density * velocity * diameter) / viscosity
    return reynolds_number, velocity

# Function to calculate pressure drop using Darcy-Weisbach equation
def calculate_pressure_drop(reynolds_number, length, diameter, velocity, density):
    if reynolds_number < 2000:
        friction_factor = 64 / reynolds_number  # Laminar flow
    else:
        friction_factor = 0.079 / (reynolds_number ** 0.25)  # Turbulent flow approximation
    pressure_drop = friction_factor * (length / diameter) * (0.5 * density * velocity ** 2)
    return pressure_drop

# Streamlit app interface
st.title("Reynolds Number and Pressure Drop Calculator")

# Input section for fluid properties
st.header("Fluid Properties")
density = st.number_input("Fluid Density (kg/m³)", value=WATER_DENSITY)
viscosity = st.number_input("Fluid Viscosity (Pa·s)", value=WATER_VISCOSITY)
flow_rate = st.number_input("Flow Rate (m³/s)", value=0.01)

# Input section for pipe dimensions
st.header("Pipe Dimensions")
diameter = st.number_input("Pipe Diameter (m)", value=0.1)
length = st.number_input("Pipe Length (m)", value=10)

# Calculate Reynolds number and velocity
reynolds_number, velocity = calculate_reynolds_number(flow_rate, diameter, density, viscosity)

# Display Reynolds number and flow regime
st.header("Results")
st.write(f"Reynolds Number: {reynolds_number:.2f}")

if reynolds_number < 2000:
    st.write("Flow Regime: Laminar")
elif 2000 <= reynolds_number <= 4000:
    st.write("Flow Regime: Transitional")
else:
    st.write("Flow Regime: Turbulent")

# Pressure drop calculation
pressure_drop = calculate_pressure_drop(reynolds_number, length, diameter, velocity, density)
st.write(f"Pressure Drop: {pressure_drop:.2f} Pa")

# Graph: Relationship between velocity and Reynolds number
st.header("Graph: Velocity vs Reynolds Number")

# Generate data for graph
flow_rates = np.linspace(0.001, 0.05, 100)  # Various flow rates in m³/s
reynolds_numbers = []
velocities = []

for q in flow_rates:
    re_num, vel = calculate_reynolds_number(q, diameter, density, viscosity)
    reynolds_numbers.append(re_num)
    velocities.append(vel)

# Plot velocity vs Reynolds number
fig, ax = plt.subplots()
ax.plot(velocities, reynolds_numbers, label="Reynolds Number")
ax.axhline(2000, color='green', linestyle='--', label="Laminar-Turbulent Threshold")
ax.axhline(4000, color='red', linestyle='--', label="Turbulent Flow Start")
ax.set_xlabel("Flow Velocity (m/s)")
ax.set_ylabel("Reynolds Number")
ax.set_title("Relationship between Velocity and Reynolds Number")
ax.legend()

# Show the plot in Streamlit
st.pyplot(fig)

# Graph: Relationship between pressure drop and Reynolds number
st.header("Graph: Pressure Drop vs Reynolds Number")

pressure_drops = []

for re_num, vel in zip(reynolds_numbers, velocities):
    pressure_drop = calculate_pressure_drop(re_num, length, diameter, vel, density)
    pressure_drops.append(pressure_drop)

# Plot pressure drop vs Reynolds number
fig2, ax2 = plt.subplots()
ax2.plot(reynolds_numbers, pressure_drops, label="Pressure Drop", color='orange')
ax2.set_xlabel("Reynolds Number")
ax2.set_ylabel("Pressure Drop (Pa)")
ax2.set_title("Relationship between Reynolds Number and Pressure Drop")
ax2.legend()

# Show the plot in Streamlit
st.pyplot(fig2)

