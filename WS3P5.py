import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate y (vapor composition) from Raoult's Law using x (liquid composition)
def calculate_vle(x, alpha):
    return (alpha * x) / (1 + (alpha - 1) * x)

# Iterative function for flash distillation calculation
def flash_distillation(f, zf, alpha, max_iterations=100, tolerance=1e-6):
    x_old = zf  # Initial guess for liquid phase composition (start with feed composition)
    for iteration in range(max_iterations):
        y = calculate_vle(x_old, alpha)  # Vapor phase composition
        x_new = zf / (1 + f * (y - x_old))  # New liquid phase composition
        if abs(x_new - x_old) < tolerance:
            break  # Convergence reached
        x_old = x_new
    return x_new, y

# Streamlit app interface
st.title("Flash Distillation Calculator using Raoult's Law (Binary Mixture)")

# Input section for flash distillation
st.header("Input Data for Flash Distillation")

alpha = st.number_input("Relative Volatility (α)", value=2.0)
zf = st.number_input("Feed Mole Fraction of Component A (zF)", value=0.5, min_value=0.0, max_value=1.0)
f = st.number_input("Vapor Fraction (F)", value=0.5, min_value=0.0, max_value=1.0)

# Perform the iterative calculation
x_liquid, y_vapor = flash_distillation(f, zf, alpha)

# Display the results
st.header("Results")
st.write(f"Liquid Phase Composition (x): {x_liquid:.4f}")
st.write(f"Vapor Phase Composition (y): {y_vapor:.4f}")

# Plot the phase diagram with iterative points
st.header("Phase Diagram")

# Generate data for equilibrium curve
x_eq = np.linspace(0, 1, 500)
y_eq = calculate_vle(x_eq, alpha)

# Plot equilibrium curve and iterative steps
fig, ax = plt.subplots()
ax.plot(x_eq, y_eq, label="Equilibrium Curve", color='blue')

# Plot the feed point
ax.plot([zf], [zf], 'ro', label="Feed Composition (zF)")

# Plot iterative steps for flash distillation
ax.plot([x_liquid, zf], [y_vapor, zf], 'g--', label="Iterative Process", marker='o')

# Add labels and title
ax.set_xlabel("Liquid Phase Mole Fraction (x)")
ax.set_ylabel("Vapor Phase Mole Fraction (y)")
ax.set_title("Vapor-Liquid Equilibrium Diagram with Iterative Flash Distillation")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Add explanation
st.write("""
This flash distillation diagram shows the iterative process for determining the vapor and liquid phase compositions using Raoult's Law for a binary mixture. The equilibrium curve represents the relationship between the vapor and liquid phase compositions at equilibrium.
""")
