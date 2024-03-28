import streamlit as st

st.sidebar.title("Menu")
menu = st.sidebar.empty()
menu = st.sidebar.selectbox("Select Option", ["Register", "Login"])
while True:
    if menu == "Register":
        pass

    elif menu == "Login":
        st.write("her")
        menu.empty()
        break