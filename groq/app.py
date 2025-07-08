import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()

## load the Groq API key
groq_api_key=os.environ['GROQ_API_KEY']

# Initialize session state
if "vector" not in st.session_state:
    st.session_state.current_url = "https://docs.smith.langchain.com/"
    st.session_state.embeddings = OllamaEmbeddings(model="llama3.2")
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    
def load_documents(url):
    """Load documents from the given URL"""
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        final_documents = st.session_state.text_splitter.split_documents(docs[:50])
        vectors = FAISS.from_documents(final_documents, st.session_state.embeddings)
        return vectors, len(docs)
    except Exception as e:
        st.error(f"Error loading documents: {str(e)}")
        return None, 0

# Load initial documents if not already loaded
if "vectors" not in st.session_state:
    with st.spinner("Loading initial documents..."):
        st.session_state.vectors, doc_count = load_documents(st.session_state.current_url)
        if st.session_state.vectors:
            st.success(f"Loaded {doc_count} documents from {st.session_state.current_url}")

st.title("ChatGroq Demo with Dynamic Document Loading")

# URL input section
st.sidebar.header("Document Source Configuration")
new_url = st.sidebar.text_input(
    "Enter URL to load documents from:", 
    value=st.session_state.current_url,
    help="Enter any website URL to load documents for Q&A"
)

if st.sidebar.button("Load New Documents", type="primary"):
    if new_url and new_url != st.session_state.current_url:
        with st.spinner(f"Loading documents from {new_url}..."):
            new_vectors, doc_count = load_documents(new_url)
            if new_vectors:
                st.session_state.vectors = new_vectors
                st.session_state.current_url = new_url
                st.success(f"Successfully loaded {doc_count} documents from {new_url}")
                st.rerun()
    elif new_url == st.session_state.current_url:
        st.info("This URL is already loaded!")
    else:
        st.warning("Please enter a valid URL")

# Display current document source
st.sidebar.info(f"Current source: {st.session_state.current_url}")

# Predefined URL options
st.sidebar.subheader("Quick Load Options")
predefined_urls = {
    "LangChain Docs": "https://docs.smith.langchain.com/",
    "Python Docs": "https://docs.python.org/3/tutorial/",
    "Streamlit Docs": "https://docs.streamlit.io/",
    "FastAPI Docs": "https://fastapi.tiangolo.com/",
    "React Docs": "https://react.dev/learn"
}

for name, url in predefined_urls.items():
    if st.sidebar.button(name, key=f"btn_{name}"):
        if url != st.session_state.current_url:
            with st.spinner(f"Loading {name}..."):
                new_vectors, doc_count = load_documents(url)
                if new_vectors:
                    st.session_state.vectors = new_vectors
                    st.session_state.current_url = url
                    st.success(f"Successfully loaded {doc_count} documents from {name}")
                    st.rerun()
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="llama3-8b-8192") 


prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)  

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt=st.text_input("Input you prompt here")


if prompt:
    start=time.process_time()
    response=retrieval_chain.invoke({"input":prompt})
    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")