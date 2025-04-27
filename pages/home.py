import streamlit as st
import pandas as pd

def show():
    st.title("MindWell: Enhancing Therapeutic Interventions Through Technology")
    st.markdown("Welcome to MindWell, your personal mental health companion powered by real-world data.")

    st.subheader("Daily Check-In")
    mood_today = st.radio("How are you feeling today?", ["Great", "Okay", "Stressed", "Anxious"])
    if st.button("Submit Mood"):
        st.success(f"Mood '{mood_today}' logged.")

    df = st.session_state['df']

    st.subheader("Snapshot from Sleep Health Data")
    st.write("Average Sleep Duration:", round(df["TotalMinutesAsleep"].mean() / 60, 2), "hours")  # converting minutes to hours
    st.write("Average Heart Rate:", round(df["AverageHeartRate"].mean(), 2), "bpm")
    st.write("Average Sedentary Minutes:", round(df["SedentaryMinutes_x"].mean(), 2), "minutes")
