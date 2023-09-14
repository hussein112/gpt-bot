from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Pinecone

import pinecone

from helpers import get_vecotrestore

from prompt import QA_PROMPT

from prepare_data import *

def create_bot():
    """Scaffold the bot by loading, splitting, and vectorizing data. Then store it in Pinecone index
    """
    csv_documents = load_split_data("data/products.csv", CSV=True)
    txt_documents = load_split_data("data/data.txt", TEXT=True)
    create_vectors(csv_documents)
    create_vectors(txt_documents)
    return get_bot()
    

def get_bot():
    """Get a new chatbot with new chat memory"""
    vectorstore = get_vecotrestore()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0, openai_api_key="openai_api_key"), 
        vectorstore.as_retriever(), 
        memory=memory,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT}
    )