import streamlit as st
#title
st.title('streamlit demo')

#markdown
st.markdown(""" 
  This is a demo app showcasing a few of Streamlit's features.

Streamlit is a powerful Python library for creating web apps. It is easy to use and has a wide range of features, including:

* **Interactive widgets:** Streamlit makes it easy to create interactive widgets, such as sliders, dropdown menus, and radio buttons.
* **Charts and graphs:** Streamlit can generate a variety of charts and graphs, including line charts, bar charts, and pie charts.
* **Data display:** Streamlit can display data in a variety of ways, including tables, lists, and maps.
* **Deployment:** Streamlit apps can be deployed to Heroku with a single command.
"""          )

#slider
slider_value = st.slider('select a number:', 0, 100)
st.write(f"You selected: {slider_value}")

#Dropdown menu

dropdown_value = st.selectbox('Choose a color:', ['red', 'green'])
st.write(f"you selected : {dropdown_value}")

# Radio Buttons
radio_button_value = st.radio('Select a language:', ['English', 'spanish'])
st.write(f"You selected: {radio_button_value}")

#text area
text = st.text_area('enter some text:')
if text:
    st.write(f'You entered : {text}')

#Button
button_click = st.button('click mee')
if button_click:
    st.write(f"you clicked it")

#chart
data = {'x':[1,2,3,4,5], 'y':[7,8,9,10,12]}
st.bar_chart(data)

#map
map_data = [
    {'name': 'New York', 'lat':40.7128, 'lon': -74.0060}
]
st.map(map_data)