import streamlit as st

def interactive_polls():
    st.subheader("Upcoming Service Polls")
    selected_activity = st.radio("What activities would you like to see?", ("Worship", "Bible Study", "Community Service"))
    if st.button("Submit Vote"):
        st.success(f"Thank you for your vote! Let's prepare for {selected_activity} in the name of Jesus Christ.")
