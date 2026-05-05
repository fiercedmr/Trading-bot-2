import streamlit as st
from paper_engine import trade_log, capital

st.title("🚀 Trading Bot Dashboard")

st.metric("Capital", f"₹{capital:.2f}")

if trade_log:
    st.line_chart(trade_log)
else:
    st.write("No trades yet")
