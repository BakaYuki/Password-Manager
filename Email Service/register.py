from dbconn import *
import hashlib

#Checking for username 
def get_user_by_username(username):
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    return user

#Checking for email
def get_user_by_email(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    return user

# Function to add a new user
def add_user(username, password,name,email):
    cur.execute("INSERT INTO users (username, password, name, email) VALUES (%s, %s,%s,%s)",
                (username, password,name,email))
    conn.commit()

#Hashing Function for password ( one way hash )
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    st.subheader("Register New User")
    new_name = st.text_input("Name")
    new_email = st.text_input("Email")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    new_password = hash_password(new_password)
    
    #Encryption of data
    if st.button("Register"):
        if get_user_by_username(new_username):
            st.warning("User already exists. Please choose another username.")
        elif get_user_by_email(new_email):
            st.warning("Email already exists. Please choose another email.")
        else:
            add_user(new_username, new_password,new_name,new_email)
            st.success("User registered successfully!")
    # st.markdown("[Go back to Login](http://localhost:8501/)")
    if st.button("Go back to Login"):
        st.session_state.initial = True
    
    
if __name__ == '__main__':
    header()
    register()