import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Initialize session state to store data
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

# 2. Function to add a new expense
def add_expense(date, category, amount, description):
    new_data = [[date, category, amount, description]]
    new_expense = pd.DataFrame(new_data, columns=['Date', 'Category', 'Amount', 'Description'])
    # Combine the new data with existing data
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

# 3. Main User Interface
st.title("💰 Finance Tracker")

# Sidebar for adding data
with st.sidebar:
    st.header("Add New Entry")
    date_val = st.date_input("Date")
    cat_val = st.selectbox("Category", ["Food", "Bills", "Transport", "Entertainment", "Other"])
    amt_val = st.number_input("Amount", min_value=0.0)
    desc_val = st.text_input("Description")
    
    if st.button("Add Expense"):
        add_expense(date_val, cat_val, amt_val, desc_val)
        st.success("Added!")

# Display the Table
st.subheader("Expense Log")
st.dataframe(st.session_state.expenses, use_container_width=True)

# Simple Visual
if not st.session_state.expenses.empty:
    st.subheader("Spending by Category")
    chart_data = st.session_state.expenses.groupby('Category')['Amount'].sum()
    st.bar_chart(chart_data)