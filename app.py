import streamlit as st
import pandas as pd
import pages.visualizations as visual
import pages.alerts as alerts
import pages.home as home
import pages.recommendations as recs 

df = pd.read_csv('clean_dataset.csv')
st.session_state['df'] = df
st.sidebar.title("MindWell Navigation")
page = st.sidebar.radio("Go to", ["Home", "Visualizations", "Alerts", "Recommendations"])

st.session_state['df'] = df

if page == "Home":
    import pages.home as home
    home.show()

elif page == "Visualizations":
    import pages.visualizations as visual
    visual.show()

elif page == "Alerts":
    import pages.alerts as alerts
    alerts.show()

elif page == "Recommendations":
    import pages.recommendations as recs
    recs.show()