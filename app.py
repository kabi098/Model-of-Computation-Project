import streamlit as st
import re

# The user's provided regex for email validation.
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$")

def validate_email_regex(email):
   
    return EMAIL_REGEX.fullmatch(email) is not None

def main():
   
    # Set the page configuration for a wider layout
    st.set_page_config(page_title="Email Validator", layout="centered")
    
    # Use markdown to create a styled header with a small emoji
    st.markdown(
        "<h1 style='text-align: center; color: #1f64cc;'>📬 Email Validator</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1.2em; color: #555;'>A quick tool to check the validity of an email address.</p>",
        unsafe_allow_html=True,
    )
    
    # Use a container to visually group the input and button
    with st.container(border=True):
        email_input = st.text_input(
            "Enter an email address:", placeholder="e.g., user@example.com"
        )
        
        # Use columns to center the button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Validate", use_container_width=True, type="primary"):
                # Check if the input field is not empty.
                if email_input:
                    # Call the validation function with the user's input.
                    is_valid = validate_email_regex(email_input)
                    # Display the result in a styled info box.
                    if is_valid:
                        st.success(
                            f"'{email_input}' is a valid email address!", icon="✅"
                        )
                    else:
                        st.error(
                            f"'{email_input}' is an invalid email address.", icon="❌"
                        )
                else:
                    # Handle the case where the user clicks the button with an empty input.
                    st.warning("Please enter an email to validate.")
    
    # Add a sidebar for extra info or future features
    with st.sidebar:
        st.header("About This Tool")
        st.info(
            "This app uses a simple regular expression to validate email addresses."
        )
        st.caption("Developed with Streamlit.")

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()