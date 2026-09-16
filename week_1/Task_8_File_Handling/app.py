from pathlib import Path

import streamlit as st


file_path = Path(__file__).parent / "introduction.txt"

st.set_page_config(page_title="File Handling")
st.title("Task 8 - Basic File Handling")
st.write("Write a short introduction to a text file and read it back.")

name = st.text_input("Name", "Ayush")
college = st.text_input(
    "College",
    "Prestige Institute of Engineering, Management & Research, Indore",
)
branch = st.text_input("Branch", "B.Tech CSE (IoT)")
statement = st.text_area(
    "Learning statement",
    "I am learning Python fundamentals for Data Analytics.",
)

if st.button("Write and Read File", type="primary"):
    introduction = (
        f"Name: {name}\n"
        f"College: {college}\n"
        f"Branch: {branch}\n"
        f"{statement}\n"
    )

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(introduction)

    with open(file_path, "r", encoding="utf-8") as file:
        file_contents = file.read()

    st.success(f"File saved: {file_path.name}")
    st.subheader("File Contents")
    st.code(file_contents)

elif file_path.exists():
    st.subheader("Current File Contents")
    with open(file_path, "r", encoding="utf-8") as file:
        st.code(file.read())
else:
    st.info("Fill in the details and click the button to create the file.")
