from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import HuggingFaceHub
from langchain_community.llms import Ollama
from operator import itemgetter
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from.env file

os.environ["HUGGINGFACEHUB_API_TOKEN"] = str(os.getenv("HUGGINGFACE_API_KEY"))
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = str(os.getenv("LANGCHAIN_API_KEY"))

llm = Ollama(model= "llama2")
prompt_template = 'please! Help the user to solve his problem and question , give him an appropriate and mindful answer . Question:{query}'

prompt= ChatPromptTemplate.from_messages(
    [ ("system", prompt_template),
     ("user", "question:{query}")
    ]
)

question = itemgetter("query")

st.title('Langchain Demo with Ollama')
input_text = st.text_input("Ask me anything...")

# #output parser

output_parser = StrOutputParser()
Chain = prompt | llm | output_parser

response = Chain.invoke('hi ! my name ia bilal')
print(response)

if input_text:

    st.write(response)
    
    