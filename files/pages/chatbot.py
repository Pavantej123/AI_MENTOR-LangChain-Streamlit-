import streamlit as st
import os
import langchain
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate,SystemMessagePromptTemplate,PromptTemplate

os.environ["HF_TOKEN"] = os.getenv("hface")

if "topic" not in st.session_state or "level" not in st.session_state:
    st.warning("Please choose a topic and level on the Home page first.")
    st.switch_page("home.py")

t = st.session_state["topic"]
l = st.session_state["level"]

st.title("Mentor Chat")
st.caption(f"Topic: {t} | Level: {l}")

if "chat" not in st.session_state or "message" not in st.session_state:
    st.session_state["chat"] = []
    st.session_state["message"] = []
    st.session_state["message"].append(("system","""You are an expert assistant restricted
    to a single user-selected domain (e.g., Data Science, Machine Learning, SQL, Python).
    Answer only if the user's question clearly belongs to the selected domain and the specified topic.
    Adjust depth, terminology, and explanation strictly according to the expertise level provided by the user (Beginner /
    Intermediate / Advanced / Expert).
    If the question is outside the selected domain or topic, respond only with:
    “The question is not related to the selected topic.”
    For valid questions, produce a concise, accurate response of 5to 6 lines, maintaining a professional expert tone with
    out extra commentary."""))

for i in st.session_state["chat"]:
    with st.chat_message(i["role"]):
        st.write(i["content"])

user_input = st.chat_input("enter your doubt")
if user_input:
    pt = PromptTemplate.from_template("answer to the {user_msg} according to the expertise level {lvl} from the topic {tpc}")
    final_prompt = pt.format(user_msg=user_input,lvl=l,tpc=t)
    st.session_state["message"].append(("user",final_prompt))
    st.session_state["chat"].append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.write(user_input)
    

    rmodel = HuggingFaceEndpoint(model = "deepseek-ai/DeepSeek-V3.2")
    cm = ChatHuggingFace(llm=rmodel)
    output = cm.invoke(st.session_state["message"])
    with st.chat_message("ai"):
        st.write(output.content)

    st.session_state["chat"].append({"role":"ai","content":output.content})
    st.session_state["message"].append(("ai",output.content))

st.page_link("home.py", label="← Back to Home")