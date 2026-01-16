# ⛓️ LANGCHAIN-INTRO

A comprehensive introduction to LangChain with hands-on examples covering LLM applications, RAG systems, Research Assistants, and Chatbots. Perfect for developers looking to build powerful AI applications with LangChain framework.

---

## 🌟 Why LANGCHAIN-INTRO?

💡 **Learn by Building**: Practical examples that demonstrate core LangChain concepts through real applications.

🔥 **Complete Workflows**: From basic LLM chains to advanced RAG systems and research assistants.

🎓 **Production Ready**: Well-structured code with FastAPI backends and Streamlit frontends.

🚀 **Modern Stack**: Uses latest LangChain features including LangChain Community, Core, and HuggingFace integrations.

---

## 📂 Repository Structure

### 🦜 LLM (Language Model Applications)

Core LangChain applications demonstrating fundamental concepts.

- **api.py** - FastAPI backend for LLM applications with RESTful endpoints
- **client.py** - Client interface for interacting with LLM APIs
- **requirements.txt** - Python dependencies for LLM applications

### 📀 RAG (Retrieval Augmented Generation)

Advanced RAG implementations for context-aware AI applications.

- **rag_agent.ipynb** - Intelligent RAG agent with autonomous retrieval capabilities
- **rag.ipynb** - Basic RAG implementation and foundational concepts
- **self_reflective_rag.ipynb** - Self-improving RAG system with reflection mechanisms
- **task.ipynb** - Task-specific RAG applications and examples
- **requirements.txt** - Dependencies for RAG implementations

### 🔬 Research Assistants

Specialized AI assistants for research, web search, and data analysis.

- **Rag_web_search.ipynb** - RAG system integrated with web search capabilities
- **Skeleton of Thoughts.ipynb** - Structured thinking framework for complex reasoning
- **SQL_Research_Assistent.ipynb** - Research assistant with SQL database integration

### 💬 Simple Chatbots

Easy-to-understand chatbot implementations for learning and experimentation.

- **Various chatbot examples** - Step-by-step chatbot development

---

## 📦 Core Dependencies

### LangChain Ecosystem

- **langchain** - Core LangChain framework
- **langchain_community** - Community integrations and tools
- **langchain_core** - Core abstractions and interfaces
- **langchain_huggingface** - HuggingFace model integrations
- **langchainhub** - Pre-built chains and prompts
- **langchain_pinecone** - Pinecone vector database integration
- **langchain-chroma** - ChromaDB vector store integration

### AI & ML Libraries

- **huggingface_hub** - Access to HuggingFace models
- **pinecone** - Vector database for semantic search
- **faiss-cpu** - Efficient similarity search

### Backend & API

- **fastapi** - Modern web framework for APIs
- **uvicorn** - ASGI server for FastAPI
- **sse_starlette** - Server-sent events support

### Frontend & Utilities

- **streamlit** - Interactive web applications
- **langserve** - LangChain application serving
- **python-dotenv** - Environment variable management
- **pypdf** - PDF processing capabilities

---

## 💡 Key Features

### 🦜 LLM Applications

- **RESTful API Design**: FastAPI backend with clean endpoints
- **Client-Server Architecture**: Modular design for scalability
- **Streaming Responses**: Real-time response generation
- **Error Handling**: Robust error management

### 📀 RAG Systems

- **Vector Databases**: Pinecone and ChromaDB integration
- **Self-Reflective RAG**: Agents that improve their retrieval
- **Context Management**: Efficient document chunking and retrieval
- **Multi-Source RAG**: Combine multiple knowledge sources

### 🔬 Research Assistants

- **Web Search Integration**: Real-time web search capabilities
- **SQL Integration**: Query and analyze structured data
- **Structured Reasoning**: "Skeleton of Thoughts" framework
- **Report Generation**: Automated research summaries

### 💬 Chatbots

- **Conversational Memory**: Context-aware conversations
- **Multiple Backends**: Support for various LLM providers
- **Customizable Personas**: Tailor chatbot behavior
- **Easy Deployment**: Simple setup and deployment

---

## 🏗️ Architecture Patterns

### Basic LLM Chain

```
User Input → Prompt Template → LLM → Output Parser → Response
```

### RAG Architecture

```
Query → Embedding → Vector Search → Context Retrieval → LLM + Context → Response
```

### Research Assistant Flow

```
Query → Planning → Web Search → Data Extraction → Analysis → Report
```

### Self-Reflective RAG

```
Query → Retrieval → Generation → Self-Critique → Refinement → Final Response
```

---

## 📚 Learning Path

1. **Start with LLM basics** (`LLM/` directory)

   - Understand prompts and chains
   - Build your first API

2. **Explore RAG systems** (`Rag/` directory)

   - Learn vector databases
   - Implement document retrieval

3. **Build Research Assistants** (`Research Assistants/` directory)

   - Integrate web search
   - Work with structured data

4. **Create Chatbots** (`Simple chatbots/` directory)
   - Add conversational memory
   - Deploy interactive applications

---

## 🛠️ Common Use Cases

- **📄 Document Q&A**: Ask questions about your documents
- **🔍 Research Automation**: Automated research and analysis
- **💬 Customer Support**: Intelligent chatbot assistants
- **📊 Data Analysis**: SQL-powered research assistants
- **🌐 Web Search Integration**: Real-time information retrieval
- **📝 Content Generation**: AI-powered writing assistants

---

## 📖 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain Community](https://github.com/langchain-ai/langchain)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [HuggingFace Hub](https://huggingface.co/)

---

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

---

## 🙏 Acknowledgments

Built with:

- **LangChain** - Framework for LLM applications
- **FastAPI** - Modern web framework
- **Streamlit** - Interactive web apps
- **HuggingFace** - Model hub and integrations
- **Pinecone** - Vector database

---

## ⭐ Star This Repository

If you find this repository helpful, please give it a star! It helps others discover these LangChain tutorials and examples.

---

**Happy Learning! 🚀 Build amazing AI applications with LangChain!**
