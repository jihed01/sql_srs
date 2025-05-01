#pylint: disable=missing-module-docstring
import duckdb
import streamlit as st

st.write("""SQL SRS Spaced Repetition SQL Practice""")

#la connection a notre BD
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GROUP BY", "window_functions"),
        index=None,
        placeholder="Select one of the themes",
    )

    st.write("You selected:", theme)
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'").df()
    st.write(exercise)

# la reponse que la personne doit taper
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
#
# if query:
#     result = duckdb.query(query).df()
#     st.dataframe(result)
#
#     try:
#         result = result[solution_tab.columns]
#     except KeyError as e:
#         st.write("some columns are missing")
#     st.dataframe(result.compare(solution_tab))
#
#
# tab1, tab2 = st.tabs(["Tables", "Solution"])
#
# with tab1:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("table: Expected")
#     st.dataframe(solution_tab)
#
# with tab2:
#     st.write(ANSWER_STR)
