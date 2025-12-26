import streamlit as st
import pickle

st.set_page_config(page_title="Student App", layout="centered")

st.title("🎓 Student Management App")

# Load PKL file
def load_data():
    try:
        with open("students.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Save PKL file
def save_data(data):
    with open("students.pkl", "wb") as file:
        pickle.dump(data, file)

students = load_data()

menu = st.sidebar.selectbox(
    "Menu",
    ["View Students", "Add Student"]
)

# ---------------- VIEW STUDENTS ----------------
if menu == "View Students":
    st.subheader("📋 Student Records")

    if students:
        for s in students:
            st.write(
                f"**Roll:** {s['roll']} | "
                f"**Name:** {s['name']} | "
                f"**Marks:** {s['marks']}"
            )
    else:
        st.warning("No student data found")

# ---------------- ADD STUDENT ----------------
elif menu == "Add Student":
    st.subheader("➕ Add New Student")

    roll = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")
    marks = st.number_input("Marks", min_value=0, max_value=100, step=1)

    if st.button("Save Student"):
        new_student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }
        students.append(new_student)
        save_data(students)
        st.success("Student added successfully ✅")
