from dbconn import *
import hashlib
from register import *
from login1 import *



def main():
    header()
    if 'initial' not in st.session_state:
        st.session_state.initial = True
        st.session_state.logged_in = False
    
    if st.session_state.initial==True:
        login_panel()
    else:
        register()
    
    # if 'logged_in' not in st.session_state:
    #     st.session_state.logged_in = False
    #     login()
    # else:
    #     login_panel()  

if __name__ == '__main__':
    main()