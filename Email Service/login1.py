from dbconn import *
from register import *

def add_password(user_id, website, username, password):
    
    cur.execute("INSERT INTO passwords (user_id, website, username, password) VALUES (%s, %s, %s, %s)",
                (user_id, website, username, password))
    conn.commit()

def get_passwords_by_user_id(user_id):

    cur.execute("SELECT * FROM passwords WHERE user_id = %s", (user_id,))
    passwords = cur.fetchall()
    return passwords

def update_password(id,user_id, website, new_username, new_password):
   
    cur.execute("UPDATE passwords SET username = %s, password = %s WHERE user_id = %s AND id = %s",
                (new_username, new_password, user_id, id))
    conn.commit()

def display_password(password):
    id = password[0]
    username_key = id + 100
    password_key = id + 1000
    del_key = id + 10000
    website = password[2]
    username = password[3]
    old_password = password[4]
    

    #Decryption to show useful data
    website = decrypt_data(website)
    username = decrypt_data(username)
    old_password = decrypt_data(old_password)

    
    st.subheader(f'Website: {website}')
    new_username = st.text_input(f"New Username: ", value=username,key=username_key)
    new_password = st.text_input(f"New Password: ", type="password", value=old_password,key=password_key)
    
    if st.button(f"Update Password for {website}",key=id):
        website = encryptor.encrypt(website)
        new_username = encryptor.encrypt(new_username)
        new_password = encryptor.encrypt(new_password)
        
        update_password(id,st.session_state.user[0], website, new_username, new_password)
        st.success(f"Password for {website} updated successfully!")

    if st.button(f"Delete Password for {website}",key=del_key):
        cur.execute("DELETE FROM passwords WHERE id = %s", (id,))
        conn.commit()
        st.success(f"Password for {website} deleted successfully!")
        
def login():
    
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    password = hash_password(password)
    st.markdown("Forgot your password? [Reset here](http://localhost:8502)")
    
    if st.button("Login"):
        user = get_user_by_username(username)
        if user:
            if password == user[2]:
                st.success("Login successful!")
                st.write(f"Welcome, {username}!")
                st.session_state.logged_in = True
                st.session_state.user = user
            else:
                st.session_state.logged_in = False
                st.error("Invalid password. Please try again.")
        else:
            st.error("User does not exist. Please register.")

    st.subheader("OR ")
    if st.button(r"$\textsf{\large Create Account}$"):
        st.session_state.initial = False
    
def login_panel():
    if st.session_state.get('logged_in',True):

        #For the first time initialization to be set to open Add Pasword
        if 'selected_option' not in st.session_state:
            st.session_state.selected_option = "Add Password"

        # Define buttons for different options
        option_buttons = {
            "Add Password": st.sidebar.button("Add Password"),
            "View Passwords": st.sidebar.button("View Passwords"),
            "Logout": st.sidebar.button("Logout")
        }

        # Determine which button was clicked
        clicked_button = None
        for option, button in option_buttons.items():
            if button:
                clicked_button = option
                break

        # Update selected_option based on the clicked button
        if clicked_button:
            st.session_state.selected_option = clicked_button

        # Display selected option
        st.sidebar.write("Selected Option:", st.session_state.selected_option)

        # Display Add Password and View Passwords options after successful login
        if st.session_state.selected_option == "Add Password":
            # st.subheader("Add New Password")
            website = st.text_input("Website")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Add"):
                
                #Encrypting the data now
                website = encrypt_data(website)
                print(website)
                username = encrypt_data(username)
                password = encrypt_data(password)
                
                # Decode the data before storing it in the database i.e. removing b''
                website = website.decode()
                username = username.decode()
                password = password.decode()
                
                #Adding the password to the database
                add_password(st.session_state.user[0], website, username, password)
                st.success("Password added successfully!")
                
        elif st.session_state.selected_option == "View Passwords":
            # st.subheader("View Passwords")
            passwords = get_passwords_by_user_id(st.session_state.user[0])
            
            if passwords:
                for password in passwords:
                    # st.write(f"0: {password[0]}     Website: {password[2]}, Username: {password[3]}, Password: {password[4]}")
                    display_password(password)
            else:
                st.write("No passwords stored yet.")
        
        elif st.session_state.selected_option == "Logout":
            st.session_state.logged_in = False
            st.success("Logout successful!")

        else:
            st.error("Invalid password. Please try again.")
    else:
        login()
