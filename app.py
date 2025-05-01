# pylint: disable=missing-module-docstring
import os
import logging
import duckdb
import streamlit as st

if "data" not in os.listdir():
    print("creating data folder")
    logging.error(os.listdir())
    logging.error("creating data folder")

if "exercise_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    #subprocess.run(["python","init_db.py"])

st.write("SQL SRS Spaced Repetition SQL Practice")

# la connection a notre BD
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    # choix de l'exercice
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "GROUP BY", "window_functions"),
        index=None,
        placeholder="Select one of the themes",
    )

    st.write("You selected:", theme)
    exercise = (
        con.execute(f"SELECT * FROM memory_state WHERE theme ='{theme}'")
        .df()
        .sort_values("last_reviewed")
        .reset_index()
    )
    st.write(exercise)

    # recuperation de la solution de l'exercice
    exercises_name = exercise.loc[0, "exercises_name"]
    with open(f"answers/{exercises_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()


# LA QUERY TAPEE PAR LA PERSONNE
st.header("Faites entrer votre query")
query = st.text_area(label="votre code sql ici", key="user input")


# RESULTAT DE LA QUERY TAPEE PAR LA PERSONNE
if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
    except KeyError as e:
        st.write("some columns are missing")
    # st.dataframe(result.compare(solution_df))


tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    exercise_tables = exercise.loc[0, "tables"]
    # st.write(exercise_tables)

    # on veut afficher les tables
    for table in exercise_tables:
        st.write(f" Table: {table}")
        # il faut recuperer la table car jusque la beverages et item_food sont des str pas des tables
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)

#     st.write("table: Expected")
#     st.dataframe(solution_tab)

with tab2:
    st.write(answer)
