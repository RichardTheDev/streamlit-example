import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit as st
import bcrypt

#
# def check_credentials():
#     # Hardcoded credentials for demonstration purposes
#     st.image("logo.svg")
#     PASSWORD = st.secrets["password"]
#
#     credentials = {
#         'usernames': {
#             'admin': {
#                 'name': 'Admin User',
#                 'password': PASSWORD,  # Hashing 'admin' password
#                 'email': 'admin@example.com',
#             }
#         }
#     }
#
#     # Instantiate the Authenticate class
#     auth = Authenticate(credentials, cookie_name='auth', key='secret_key')
#
#     # Define a function to create the login form
#     # Use the login method from the Authenticate class
#     name, authentication_status, username = auth.login(location='main')
#
#     # Check if login was successful
#     if authentication_status:
#         return True
#         # Additional logic here for authenticated users
#     elif authentication_status == False:
#         st.error('Mot de passe incorrect')
#         return False
#     # For no input, do not display any message
#
#     # Call the login form function to display the form

def check_credentials():
    # Display an image (make sure the path to 'logo.svg' is correct or accessible from your app)
    st.image("logo.svg")

    # Assuming st.secrets is correctly set up in your `secrets.toml` file
    PASSWORD = st.secrets["password"]

    credentials = {
        'usernames': {
            'admin': {
                'name': 'Admin User',
                'password': PASSWORD,  # Assuming this password is hashed or stored securely
                'email': 'admin@example.com',
            }
        }
    }

    # Instantiate the Authenticate class
    auth = Authenticate(credentials, cookie_name='auth', key='secret_key')

    # Check if the login form should be displayed and handle login
    if 'authentication_status' not in st.session_state:
        # Define a function to create and handle the login form
        # Use the login method from the Authenticate class
        name, authentication_status, username = auth.login(location='main')

        # Save the authentication status in session state to persist across reruns
        st.session_state['authentication_status'] = authentication_status

        # Check if login was successful
        if authentication_status:
            st.success(f"Welcome {name}!")
            return True
            # Additional logic here for authenticated users
        elif authentication_status is False:
            st.error('Incorrect password')
            return False
    else:
        # For subsequent reruns, check the session state
        if st.session_state['authentication_status']:
            return True
        else:
            # Optional: prompt for re-authentication or handle unauthorized access
            return False
