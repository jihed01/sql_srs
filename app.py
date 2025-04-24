import streamlit as st
import pandas as pd
import duckdb

#create data
data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)
st.write(df)

query = st.text_area("faites entrer votre query")

st.write(duckdb.sql(query).df())