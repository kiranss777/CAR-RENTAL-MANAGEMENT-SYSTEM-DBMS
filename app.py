import streamlit as st
import mysql.connector
from create import create
from database import create_table
from delete import delete
from read import read
from update import update
#from query import query

def main():
    st.title("PES1UG20CS212 CAR SHOWROOM DATABASE")
    menu = ["Add Details", "View Details", "Edit Details", "Remove Details"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add Details":
        st.subheader("Enter Details:")
        create()

    elif choice == "View Details":
        st.subheader("View Details:")
        read()

    elif choice == "Edit Details":
        #st.subheader("Edited Details:")
        update()

    elif choice == "Remove Details":
        st.subheader("Delete Details:")
        delete()

    else:
        st.subheader("About Train")


if __name__ == '__main__':
    main()