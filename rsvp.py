import streamlit as st

def rsvp_section():
    st.subheader("RSVP for Next Friday Service")
    name = st.text_input("Your Name:")
    contact = st.text_input("Contact Number:")
    attending = st.radio("Will you attend the service?", ("Yes", "No"))
    if st.button("Submit RSVP"):
        if name and contact and attending:
            st.success(f"Thank you, {name}! Your RSVP has been recorded in the name of Jesus Christ.")
        else:
            st.warning("Please fill in all fields.")
