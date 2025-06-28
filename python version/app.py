import streamlit as st
from utils import get_tiingo_client,fetch_stock_data , calc_returns_and_cagr

st.title("Buy and hold")
st.text("Buy-and-hold means you invest a fixed amount in a stock on the start date and hold it without trading until the end date. The return depends solely on how the stock’s price changes over that period — no timing or rebalancing involved.")

st.markdown(
    f"""
    <span style="background-color:#007bff; color:white; padding:3px 8px; border-radius:10px; font-size:90%;">Compound annual growth rate</span>
    <span style="margin-left: 10px;">Overall percentage gain or loss over the period.</span>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <span style="background-color:#007bff; color:white; padding:3px 8px; border-radius:10px; font-size:90%;">Total Return</span>
    <span style="margin-left: 10px;">Average yearly growth rate of the investment.</span>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <span style="background-color:#007bff; color:white; padding:3px 8px; border-radius:10px; font-size:90%;">Portfolio Values</span>
    <span style="margin-left: 10px;">Daily value of your portfolio over time.</span>
    """,
    unsafe_allow_html=True
)

st.divider()

with st.sidebar.form("input_form",clear_on_submit=False):
    ticker_input = st.text_input("Enter the stock ticker")
    ticker = ticker_input.strip();

    start_date = st.date_input("enter the start date")
    end_date = st.date_input("enter the end date")

    capital = st.number_input("Enter the capital in USD")

    submitted = st.form_submit_button("Generate heatmap")


client = get_tiingo_client()
try:
    if ticker and submitted:

        df = fetch_stock_data(client , ticker , start_date , end_date)
        total_return_percent , cagr , total_returns = calc_returns_and_cagr(df,capital)
        total_return = capital + (total_return_percent*capital)
        st.write(f"If you had bought {ticker} for {capital} US dollars....")
        st.write(f"Your total return would be : {total_return} USD")
        st.write(f"Your compound annual growth rate would be : {cagr *100} %")
        st.write("Your portfolio's growth, plotted")
        st.line_chart(total_returns)

        



except Exception as e:
        st.error(f"Error fetching or processing data: {e}")    
    
    