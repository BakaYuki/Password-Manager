from dbconn import *
import hashlib

def get_user_by_username(username):
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    return user

# Function to add a new user
def add_user(username, password):
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password))
    conn.commit()

#Hashing Function for password ( one way hash )
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    st.subheader("Register New User")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    new_password = hash_password(new_password)
    if st.button("Register"):
        if get_user_by_username(new_username):
            st.warning("User already exists. Please choose another username.")
        else:
            add_user(new_username, new_password)
            st.success("User registered successfully!")
    # st.markdown("[Go back to Login](http://localhost:8501/)")
    if st.button("Go back to Login"):
        st.session_state.initial = True
    
    
if __name__ == '__main__':
    header()
    register()