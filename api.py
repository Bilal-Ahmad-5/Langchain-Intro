from fastapi import FastAPI
from langchain.llms import HuggingFaceHub
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
from langchain_core.output_parsers import StrOutputParser
import uvicorn
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = str(os.getenv("HUGGINGFACE_API_KEY"))
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = str(os.getenv("LANGCHAIN_API_KEY"))

app = FastAPI(
    title="API LANGCHAIN",
    description="A RESTful API using LangChain",
    version="1.0"
)

llm = HuggingFaceHub(repo_id="meta-llama/llama-2-7b")
llm2 = HuggingFaceHub('question-answering',repo_id="google-bert/bert-large-uncased-whole-word-masking-finetuned-squad")
add_routes(
    app,
    llm,
    path="/api"
)

prompt_template = "Answer the user questions like you are a only one in the world who can help them so please solve thier problem by answering mindfuly and properly , Question:{query}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt_template),
        ("user", "question:{query}")
    ]
)

prompt2 = ChatPromptTemplate.from_template("create a mindful story on given topic {topic}")
chain = prompt | llm | StrOutputParser()

chain2 = prompt2 | llm2 | StrOutputParser()

add_routes(
    app,
    chain,
    path="/chain"
)

add_routes(
    app,
    chain2,
    path="/story"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=5000)

