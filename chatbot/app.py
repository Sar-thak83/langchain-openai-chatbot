from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv("../.env")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer the question as best you can."),
        ("user","Question:{question}"),
    ]
)

# streamlit frameWork

st.title("Chatbot Application")
input_question = st.text_input("Search the topic whatever you want to know about")

#OpenAI LLM

llm= ChatOpenAI(
    model="gpt-3.5-turbo",
)
output_parser = StrOutputParser()
chain= prompt | llm | output_parser

if input_question:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": input_question})
            st.success(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")


