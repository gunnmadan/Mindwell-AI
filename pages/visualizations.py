import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Data Visualizations")
    df = st.session_state['df']

    st.subheader("Sleep Duration Distribution")
    plt.figure(figsize=(6,4))
    sns.histplot(df['TotalMinutesAsleep'] / 60, bins=20, kde=True, color='skyblue')
    plt.xlabel('Sleep Duration (hours)')
    plt.ylabel('Count')
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("Average Heart Rate Distribution")
    plt.figure(figsize=(6,4))
    sns.histplot(df['AverageHeartRate'], bins=20, kde=True, color='lightcoral')
    plt.xlabel('Average Heart Rate (bpm)')
    plt.ylabel('Count')
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("Sedentary Minutes Distribution")
    plt.figure(figsize=(6,4))
    sns.histplot(df['SedentaryMinutes_x'], bins=20, kde=True, color='plum')
    plt.xlabel('Sedentary Minutes')
    plt.ylabel('Count')
    plt.grid(True)
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("Feature Correlation Matrix")
    selected_features = [
        'TotalMinutesAsleep', 
        'TotalSteps', 
        'Calories', 
        'SedentaryMinutes_x', 
        'VeryActiveMinutes_x', 
        'AverageHeartRate'
    ]
    corr_matrix = df[selected_features].corr()

    plt.figure(figsize=(8,6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Feature Correlation Matrix')
    st.pyplot(plt.gcf())
    plt.clf()
