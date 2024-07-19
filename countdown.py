import streamlit as st
from datetime import datetime, timedelta

def display_countdown_timer():
    st.subheader("Next Friday Service Countdown:")
    
    # Calculate next Friday
    today = datetime.now()
    days_to_next_friday = (4 - today.weekday()) % 7
    next_friday = today + timedelta(days=days_to_next_friday)

    # Display countdown using HTML and JavaScript
    countdown_str = f"""
    <div id="countdown"></div>
    <script>
        var countdownDate = new Date("{next_friday.strftime('%Y-%m-%d %H:%M:%S')}");
        
        var x = setInterval(function() {{
            var now = new Date().getTime();
            var distance = countdownDate - now;

            var days = Math.floor(distance / (1000 * 60 * 60 * 24));
            var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById("countdown").innerHTML = "<b>" + days + "d " + hours + "h "
            + minutes + "m " + seconds + "s </b>";
            
            if (distance < 0) {{
                clearInterval(x);
                document.getElementById("countdown").innerHTML = "EXPIRED";
            }}
        }}, 1000);
    </script>
    """
    
    st.markdown(countdown_str, unsafe_allow_html=True)

