import streamlit as st
from motivation import show_motivational_message
from countdown import display_countdown_timer
from rsvp import rsvp_section
from testimonials import show_past_highlights
from polls import interactive_polls
from calendar_1 import display_upcoming_events_calendar
from feedback import feedback_form
from social import social_sharing_buttons
from achievements import show_achievement_badges
from community import show_community_chat, show_upcoming_community_events

# Title and introductory section
st.title("Friday Youth Services App")
st.subheader("Welcome to the Friday Youth Services in the Name of Jesus Christ!")

# Show motivational message
show_motivational_message()

# Display countdown timer
display_countdown_timer()

# Sections for RSVP, testimonials, polls, calendar, feedback, social sharing, achievements, and community building
rsvp_section()
show_past_highlights()
interactive_polls()
display_upcoming_events_calendar()
feedback_form()
social_sharing_buttons()
show_achievement_badges()
show_community_chat()
show_upcoming_community_events()
