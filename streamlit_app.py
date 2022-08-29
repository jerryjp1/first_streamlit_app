import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])

# Display the table on the page.

streamlit.title('My parents new healthy diner')
streamlit.header('Lunch - Menu')
streamlit.text('🥗 Steamed Jeera Rice')
streamlit.text('🥣 Dal tadka')
streamlit.text('🐔 Chicken Tandoor')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
