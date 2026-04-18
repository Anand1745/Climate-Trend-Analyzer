import sys, os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd
from src.kpi.kpi_engine import generate_kpis
from src.reporting.pdf_report import generate_report

st.set_page_config(layout="wide")

df = pd.read_csv("data/processed/cleaned.csv", parse_dates=['date'])

# Sidebar filter
df['year'] = df['date'].dt.year
year = st.sidebar.selectbox("Year", ["All"] + sorted(df['year'].unique()))

if year != "All":
    df = df[df['year'] == year]

st.title("🌍 Climate Intelligence Dashboard")

kpis = generate_kpis(df)

cols = st.columns(4)
for i,(k,v) in enumerate(kpis.items()):
    cols[i].metric(k, round(v,2))

tab1, tab2, tab3 = st.tabs(["Trend","Anomaly","Forecast"])

with tab1:
    st.line_chart(df.set_index('date')['temperature'])

with tab2:
    st.dataframe(df[df['anomaly']==True].tail(20))

with tab3:
    forecast = pd.read_csv("outputs/forecast.csv", parse_dates=['date'])

    combined = pd.concat([
        df[['date','temperature']].rename(columns={'temperature':'value'}),
        forecast.rename(columns={'forecast':'value'})
    ])

    st.line_chart(combined.set_index('date'))

if st.button("Generate Report"):
    generate_report(kpis)
    st.success("Report Generated")