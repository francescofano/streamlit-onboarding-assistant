from data.employees import generate_employee_data
import json
from gui import AssistantGUI
from assistant import Assistant
import streamlit as st
from dotenv import load_dotenv
import logging
from langchain_groq import ChatGroq
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

if __name__ == "__main__":
    st.set_page_config(page_title="Assistant", page_icon=":shark:", layout="wide")
    load_dotenv()

    logging.basicConfig(level=logging.INFO)
 
    @st.cache_data(ttl=3600, show_spinner="Loading Employee Data...")
    def get_user_data():
        return generate_employee_data(1)[0]

    customer_data = get_user_data()

    @st.cache_resource(ttl=3600, show_spinner="Loading Vector Store...")
    def init_vector_store(pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000, chunk_overlap=200
            )
            splits = text_splitter.split_documents(docs)

            embedding_function = OpenAIEmbeddings()
            persistent_path = "./data/vectorstore"

            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=embedding_function,
                persist_directory=persistent_path,
            )

            return vectorstore
        except Exception as e:
            logging.error(f"Error initializing vector store: {str(e)}")
            st.error(f"Failed to initialize vector store: {str(e)}")
            return None
        
    vector_store = init_vector_store("data/umbrella_corp_policies.pdf")

    if "customer" not in st.session_state:
        st.session_state.customer = customer_data

    if "message_history" not in st.session_state:
        st.session_state.message_history = [{"role": "ai", "content": WELCOME_MESSAGE}]

    user = get_user_data()

    llm = ChatGroq(model="llama-3.1-8b-instant")
    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm=llm,
        message_history=st.session_state.message_history,
        employee_information=st.session_state.customer,
        vector_store=vector_store,
    )
   
    gui = AssistantGUI(assistant)
    gui.render()
