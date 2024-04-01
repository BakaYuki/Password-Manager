from dbconn import *
from emailsender import *
from register import get_user_by_email, hash_password
from ceaser import *
import random

def reset_password():
    if 'a' not in st.session_state:
        st.session_state.a = 0
        st.session_state.sentcode = False
        st.session_state.verify = False
        
    st.subheader("Reset Password")
    email = st.text_input("Email")
    if st.button("Send Reset Code"):
        code = str(random.randint(1000,9999))
        user = get_user_by_email(email)
        if user:
            pw = hash_password(str(code))
            cur.execute("UPDATE users SET password = %s WHERE id = %s",
                (pw,user[0]))
            conn.commit()            
            send_email(email,code)
            st.session_state.sentcode = True
            st.session_state.code = code
            st.success("Reset code sent successfully!")
        else:
            st.warning("Email not found. Please enter a valid email.")
    # if st.button("Go back to Login"):
    #     st.session_state.initial = True
    #     http://localhost:8501
    if st.markdown("[Go back to Login](http://localhost:8501)"):
        st.session_state.initial = True
        
    if st.session_state.sentcode== True and st.session_state.verify == False:
        check = st.text_input("Enter the code sent to your email")
        if st.button("Submit"):
            if check == st.session_state.code:
                st.success("Code verified!")
                st.session_state.verify = True
            else:
                st.error("Invalid code. Please try again.")
    if st.session_state.verify==True and st.session_state.sentcode==True:
        new_password = st.text_input("New Password", type="password")
        if st.button("Reset Password"):
            new_password = hash_password(new_password)
            cur.execute("UPDATE users SET password = %s WHERE email = %s",
                (new_password,email))
            conn.commit()
            st.success("Password reset successful!")
            st.session_state.verify = False
            st.session_state.sentcode = False
    
if __name__ == '__main__':

    header()
    reset_password()