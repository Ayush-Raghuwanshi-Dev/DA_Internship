import streamlit as st


st.set_page_config(page_title="Student Records")
st.title("Student Record Management System")
st.write("Add, view, search, and delete student records.")

if "students" not in st.session_state:
    st.session_state.students = []

with st.sidebar:
    st.header("Add Student")
    with st.form("student_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120, value=21, step=1)
        branch = st.text_input("Branch", "B.Tech CSE (IoT)")
        college = st.text_input(
            "College",
            "Prestige Institute of Engineering, Management & Research, Indore",
        )
        marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.1)
        add_submitted = st.form_submit_button("Add Student", type="primary")

    if add_submitted:
        if not name.strip():
            st.error("Please enter a student name.")
        else:
            st.session_state.students.append(
                {
                    "name": name.strip(),
                    "age": age,
                    "branch": branch.strip(),
                    "college": college.strip(),
                    "marks": marks,
                }
            )
            st.success("Student added successfully.")

students = st.session_state.students

st.header("Student Records")
if students:
    st.dataframe(students, use_container_width=True, hide_index=True)
else:
    st.info("No student records found.")

st.header("Search Student")
search_name = st.text_input("Enter a name to search")
if st.button("Search"):
    matches = [
        student for student in students
        if student["name"].lower() == search_name.strip().lower()
    ]
    if matches:
        st.success("Student found.")
        st.dataframe(matches, use_container_width=True, hide_index=True)
    else:
        st.warning("Student not found.")

st.header("Delete Student")
delete_name = st.text_input("Enter a name to delete")
if st.button("Delete"):
    for index, student in enumerate(students):
        if student["name"].lower() == delete_name.strip().lower():
            st.session_state.students.pop(index)
            st.success("Student deleted successfully.")
            st.rerun()
    else:
        st.warning("Student not found.")
