import streamlit as st
from streamlit import session_state

import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state['todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("ToDo App")
st.subheader("This is my first web app")
st. write("This is my first Python web app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "Enter a Todo", placeholder="Add todo here.....", on_change=add_todo, key = 'todo')


st.session_state

