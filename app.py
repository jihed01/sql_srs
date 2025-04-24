import streamlit as st
import pandas as pd
import duckdb
st.write("""   SQL SRS Spaced Repetition SQL Practice""")

option = st.selectbox(

    "What would you like to review?",
    ("JOINS", "GROUP BY", "WINDOWS FUNCTIONS"),
)

st.write("You selected:", option)

#create data
data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)
st.write(df)

query = st.text_area("faites entrer votre query")

st.write(duckdb.sql(query).df())