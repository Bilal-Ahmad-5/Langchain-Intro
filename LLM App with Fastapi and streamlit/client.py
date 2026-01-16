import requests
import streamlit as st 

def get_ollama_response(input_text):
    response = requests.post("http://localhost:5000/story/invoke",
                             json={'input':{'topic':input_text}})
    return response.json()['output']


def get_HF_response(input_text):
    response = requests.post("http://localhost:5000/chain/invoke",
                             json={'input':{ 'query' : input_text}})
    return response.json()['output']

st.title("Langchain Demo")
input_text = st.text_input("Ask me anything")
input_text1 = st.text_input("Write a story on ")

if input_text:
    st.write(get_ollama_response(input_text))
    
if input_text1:
    st.write(get_HF_response(input_text1))