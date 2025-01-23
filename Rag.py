from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint
from operator import itemgetter
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = str(os.getenv("HUGGINGFACE_API_KEY"))
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = str(os.getenv("LANGCHAIN_API_KEY"))

llm = HuggingFaceEndpoint(repo_id= "meta-llama/llama-2-7b")
prompt_template = 'please! Help the user to solve his problem and question , give him an appropriate and mindful answer . Question:{query}'

prompt= ChatPromptTemplate.from_messages(
    [ ("system", prompt_template),
     ("user", "question:{query}")
    ]
)

question = itemgetter("query")

# st.title('Langchain Demo with HuggingFace')
# input_text = st.text_input("Ask me anything...")

#output parser

output_parser = StrOutputParser()
Chain = prompt | llm | output_parser

query = "What is the history of the Eiffel Tower?"
response = Chain.invoke({"query": query})
print(response)

# if input_text:
#     st.write(Chain.invoke({"query": input_text}))