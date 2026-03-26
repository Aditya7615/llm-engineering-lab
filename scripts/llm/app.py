from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.3, max_tokens=100)

st.header("ChatGroq LLM Integration")

user_input = st.text_area("Enter your prompt here:")


if st.button("Generate Response"):
    st.write(result := model.invoke(user_input))

