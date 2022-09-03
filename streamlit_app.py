import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.title('My parents new healthy diner')
streamlit.header('Lunch - Menu')
streamlit.text('🥗 Steamed Jeera Rice')
streamlit.text('🥣 Dal tadka')
streamlit.text('🐔 Chicken Tandoor')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(fruits_to_show)

# Display fruity vice api data
import requests

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
# streamlit.text(fruityvice_response.json())
# flattens the json using pandas 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the json in tabular
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
