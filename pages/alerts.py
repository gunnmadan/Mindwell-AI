import streamlit as st

def show():
    st.title("Smart Alerts and Risk Feedback")
    df = st.session_state['df']
    st.subheader("Risk Alerts Based on Health Metrics")

    poor_sleep = df[df['TotalMinutesAsleep'] <= 300]
    high_heart_rate = df[df['AverageHeartRate'] >= 90]
    highly_sedentary = df[df['SedentaryMinutes_x'] >= 1000]

    if not poor_sleep.empty:
        st.warning(f"{len(poor_sleep)} users report insufficient sleep (≤5 hours).")

    if not high_heart_rate.empty:
        st.error(f"{len(high_heart_rate)} users have elevated heart rates (≥90 bpm).")

    if not highly_sedentary.empty:
        st.warning(f"{len(highly_sedentary)} users have highly sedentary lifestyles (≥1000 minutes sitting).")

    if 'FuzzyRiskCategory' in df.columns:
        high_risk = df[df['FuzzyRiskCategory'] == 'High Risk']
        if not high_risk.empty:
            st.error(f"{len(high_risk)} users are classified as High Risk (Fuzzy Risk Analysis).")
