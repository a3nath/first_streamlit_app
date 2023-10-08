import streamlit
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.title('Snowflake healthy diner title')
streamlit.header("snowflake badge 2 header")
streamlit.text("snowflake badge 2 TEXT")
streamlit.dataframe(my_fruit_list)

