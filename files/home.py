import streamlit as st

st.set_page_config(page_title="ATM", page_icon="📖", layout="wide") 
st.title("ANY TIME MENTOR")
st.caption("Choose a topic and level to start a guided learning + Q&A session.")

topics = ["Python","Exploratory Data Analysis","SQL","Power BI","Statistics","Machine Learning","Deep Learning","GenAI","AgenticAI"]
levels = ["Beginner","Intermediate","Expert"]

with st.form("start_form"):
    topic = st.selectbox("Choose Topic", topics)
    level = st.selectbox("Choose Level", levels)
    start = st.form_submit_button("Let's Begin")
 
if start:
    st.session_state["topic"] = topic
    st.session_state["level"] = level
    if topic=="Python":
        st.switch_page("pages/python.py")
    elif topic=="Exploratory Data Analysis":
        st.switch_page("pages/eda.py")
    elif topic=="SQL":
        st.switch_page("pages/sql.py")
    elif topic=="Power BI":
        st.switch_page("pages/powerbi.py")
    elif topic=="Statistics":
        st.switch_page("pages/stats.py")
    elif topic=="Machine Learning":
        st.switch_page("pages/ml.py")
    elif topic=="Deep Learning":
        st.switch_page("pages/dl.py")
    elif topic=="GenAI":
        st.switch_page("pages/genai.py")
    elif topic=="AgenticAI":
        st.switch_page("pages/agenticai.py")