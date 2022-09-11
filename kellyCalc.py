import streamlit as st

st.header("Kelly Calculator")

frac = st.slider('Fraction', min_value = float(0), max_value=float(1), value = float(0.25), step= 0.25, help=("Suggest 0.25 to bein giwht. Kelly 1.0 is hardcore risk level"))
bookOdds = st.number_input('Bookmaker Odds: ', min_value=float(1.0), help="Use Decimal Odds")
fairOdds = st.number_input('Fair Odds: ', min_value=(1.0), help="Use Decimal Odds")
bankRoll = st.number_input('Bankroll: ')

if bankRoll != 0:
    stake = bankRoll * frac * (((1/fairOdds)*bookOdds)-1)/(bookOdds-1)
else:
    stake = 0

if stake > 0:
    st.subheader("Suggested Stake")
    st.text(f"The optimal stake for this bet is {stake:.2f}")
elif stake <0:
    st.subheader("Suggested Stake")
    st.text(f"This is not a value bet.")
else:
    st.subheader("Awaiting inputs...")