import os
from dotenv import load_dotenv
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
# question from human is human message, System message is when we want
# system to act in some way, AI message is the output message from model.
from langchain.chat_models import ChatOpenAI

# Streamlit UI

st.set_page_config(page_title="Conversational QandA ChatBot")
st.header("Personal Conversational QandA chatbot")
load_dotenv()

chat = ChatOpenAI()

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="You are a comedian AI assitant")
    ]

# function to load OpenAI modell and get respones


def get_openai_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")

# if ask button is clicked

if submit:
    st.subheader("The response is")
    st.write(response)
