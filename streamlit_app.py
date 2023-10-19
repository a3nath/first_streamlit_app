import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.title('Snowflake healthy diner title')
streamlit.header("snowflake badge 2 header")
streamlit.text("snowflake badge 2 TEXT")
streamlit.dataframe(my_fruit_list)
                                           
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/mango")
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header('Fruityyive Advice')
try:
  fruit_choice = streamlit.text_input('What fruit')
  if not fruit_choice:
    print("not a choice")
    streamlit.error("Please select a fruit choice")
  else:
    print("else")
    back_from_function = get_fruityvice_data(fruit_choice)
    print(back_from_function)
    streamlit.dataframe(back_from_function)

except URLERROR as e:
  streamlit.error()
  

streamlit.header('the fruit load list contains:')
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()

if streamlit.button('Get fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values('from streamlit')")
      return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('what fruit to add')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
