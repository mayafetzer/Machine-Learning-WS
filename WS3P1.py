import streamlit as st
import matplotlib.pyplot as plt

# Set up the title of the app
st.title("Household Budgeting App")

# Income Section
st.header("Income")
salary = st.number_input("Salary ($)", min_value=0.0, value=0.0)
investment_income = st.number_input("Investment Income ($)", min_value=0.0, value=0.0)
other_income = st.number_input("Other Income ($)", min_value=0.0, value=0.0)

# Total income calculation
total_income = salary + investment_income + other_income
st.write(f"**Total Income**: ${total_income:.2f}")

# Expenses Section
st.header("Expenses")
housing = st.number_input("Housing (Rent/Mortgage) ($)", min_value=0.0, value=0.0)
utilities = st.number_input("Utilities ($)", min_value=0.0, value=0.0)
groceries = st.number_input("Groceries ($)", min_value=0.0, value=0.0)
transportation = st.number_input("Transportation ($)", min_value=0.0, value=0.0)
entertainment = st.number_input("Entertainment ($)", min_value=0.0, value=0.0)
savings = st.number_input("Savings/Investments ($)", min_value=0.0, value=0.0)
other_expenses = st.number_input("Other Expenses ($)", min_value=0.0, value=0.0)

# Total expense calculation
total_expenses = housing + utilities + groceries + transportation + entertainment + savings + other_expenses
st.write(f"**Total Expenses**: ${total_expenses:.2f}")

# Calculate Net Savings
net_savings = total_income - total_expenses
if net_savings >= 0:
    st.success(f"**Net Savings**: ${net_savings:.2f}")
else:
    st.error(f"**Net Savings (Deficit)**: ${net_savings:.2f}")

# Display budget distribution pie chart
st.header("Budget Distribution")
categories = ["Housing", "Utilities", "Groceries", "Transportation", "Entertainment", "Savings", "Other Expenses"]
values = [housing, utilities, groceries, transportation, entertainment, savings, other_expenses]

if total_expenses > 0:
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures the pie is drawn as a circle.

    # Display the pie chart
    st.pyplot(fig)
else:
    st.write("No expenses to display the pie chart.")
