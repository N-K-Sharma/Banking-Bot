import streamlit as st
from strands_agent import banking_agent

# ✅ Must be the first Streamlit command
st.set_page_config(page_title="🏦 BankingBot", page_icon="💰", layout="centered")

st.title("🏦 BankingBot - Your Banking Assistant")
st.write("Ask me anything about banking, loans, EMI, or financial tips!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# User input
user_input = st.text_input(
    "Enter your banking query:",
    placeholder="e.g., Calculate EMI for ₹500000 loan at 8% interest for 60 months"
)

# Button action
if st.button("Ask BankingBot"):
    if user_input.strip():
        # ✅ Direct call to agent
        response = banking_agent(user_input)
        st.session_state["history"].append((user_input, response))
    else:
        st.warning("Please enter a query.")

# Display chat history
for q, r in st.session_state["history"]:
    st.markdown(f"**You:** {q}")
    st.markdown(f"**BankingBot:** {r}")