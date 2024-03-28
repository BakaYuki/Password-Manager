import streamlit as st
import psycopg2

# Dummy admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Database connection parameters
DB_NAME = "password_manager"
DB_USER = "postgres"
DB_PASSWORD = "root"
DB_HOST = "localhost"  # Update this if your database is hosted elsewhere
DB_PORT = "5432"  # Default PostgreSQL port

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

def header():
    header_col, image_col = st.columns([3,1])
    # st.header("Password Manager",divider='rainbow')
    # st.image("images/lock.png",width=10)
    
    #Placing Header in first column taking 3/4 space
    with header_col:
        st.header("Password Manager",divider='rainbow')
    
    #Placing Image in second column taking 1/4 space
    with image_col:
        st.image("images/locknobg.jpg",width=100)
