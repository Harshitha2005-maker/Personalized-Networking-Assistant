
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

if "generated_topics" not in st.session_state:
    st.session_s# Initialize session state variables
tate["generated_topics"] = []

if "feedback" not in st.session_state:
    st.session_state["feedback"] = []