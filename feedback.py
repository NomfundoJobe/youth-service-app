import streamlit as st

def feedback_form():
    st.subheader("Feedback Form")
    feedback = st.text_area("Share your thoughts on how we can improve youth services:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback! Your input helps us better serve in the name of Jesus Christ.")
