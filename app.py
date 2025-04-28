import streamlit as st
import pandas as pd
import duckdb
import io


st.write("""   SQL SRS Spaced Repetition SQL Practice""")

with st.sidebar:
    option = st.selectbox(

        "What would you like to review?",
        ("JOINS", "GROUP BY", "WINDOWS FUNCTIONS"),
    )

    st.write("You selected:", option)


#LA QUERY TAPEE PAR LA PERSONNE
query = st.text_area("faites entrer votre query")

# vraie question
# DATA
csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

# la réponse que la personne doit taper
answer_str = """
        SELECT *
        FROM beverages
        CROSS JOIN food_items 
        """

# le resultat attendu
solution_tab = duckdb.sql(answer_str).df()



#RESULTAT DE LA QUERY TAPEE PAR LA PERSONNE
st.write(duckdb.sql(query).df())

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("table: Expected")
    st.dataframe(solution_tab)

with tab2:
    st.write(answer_str)

