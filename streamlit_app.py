import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("User Management System")

# Section to Create a New User
st.header("Create a New User")
name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Create User"):
    if name and email:
        response = requests.post(f"{API_URL}/users/", json={"name": name, "email": email})
        if response.status_code == 200:
            st.success("User created successfully")
        else:
            st.error("Error creating user")

# Section to Read Users
st.header("Read Users")
if st.button("Get All Users"):
    response = requests.get(f"{API_URL}/users/")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            st.write(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    else:
        st.error("Error fetching users")

# Section to Update a User
st.header("Update a User")
user_id = st.number_input("User ID to Update", min_value=1, step=1)
new_name = st.text_input("New Name")
new_email = st.text_input("New Email")

if st.button("Update User"):
    if user_id and new_name and new_email:
        response = requests.put(f"{API_URL}/users/{user_id}", json={"name": new_name, "email": new_email})
        if response.status_code == 200:
            st.success("User updated successfully")
        else:
            st.error("Error updating user")

# Section to Delete a User
st.header("Delete a User")
delete_user_id = st.number_input("User ID to Delete", min_value=1, step=1)

if st.button("Delete User"):
    if delete_user_id:
        response = requests.delete(f"{API_URL}/users/{delete_user_id}")
        if response.status_code == 200:
            st.success("User deleted successfully")
        else:
            st.error("Error deleting user")
