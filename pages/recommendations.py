import streamlit as st

def show():
    st.title("Personalized Health Recommendations")

    df = st.session_state['df']

    st.subheader("Overall Risk Breakdown")
    st.write(df["RiskCategory"].value_counts())

    st.subheader("Detailed Recommendations")

    for idx, row in df.iterrows():
        st.write(f"User ID {row['Id']}: {row['RiskCategory']}")
        if row["RiskCategory"] == "Low Risk":
            st.write("Maintain your healthy lifestyle! Focus on regular sleep, balanced diet, and daily movement.")
        elif row["RiskCategory"] == "Medium Risk":
            st.write("⚠️ Pay attention to your sleep quality and physical activity. Mindfulness and moderate exercise are recommended.")
        elif row["RiskCategory"] == "High Risk":
            st.write("Consider consulting a healthcare professional. Prioritize managing stress, improving sleep hygiene, and reducing sedentary behavior.")

        st.write("---")
