#pylint: disable=missing-module-docstring
import io
import duckdb
import pandas as pd
import streamlit as st

st.write("""SQL SRS Spaced Repetition SQL Practice""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("JOINS", "GROUP BY", "WINDOWS FUNCTIONS"),
    )

    st.write("You selected:", option)
# DATA
CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

# la r√©ponse que la personne doit taper
ANSWER_STR = """
SELECT *
FROM beverages
CROSS JOIN food_items 
"""

# le resultat attendu
solution_tab = duckdb.sql(ANSWER_STR).df()


# LA QUERY TAPEE PAR LA PERSONNE
st.header("faites entrer votre query")
query = st.text_area(label="votre code sql ici", key="user input")

# RESULTAT DE LA QUERY TAPEE PAR LA PERSONNE
# st.write(duckdb.sql(query).df())

if query:
    result = duckdb.query(query).df()
    st.dataframe(result)

    try:
        result = result[solution_tab.columns]
    except KeyError as e:
        st.write("some columns are missing")
    st.dataframe(result.compare(solution_tab))


tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("table: Expected")
    st.dataframe(solution_tab)

with tab2:
    st.write(ANSWER_STR)
