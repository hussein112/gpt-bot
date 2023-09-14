from langchain.chains import ConversationalRetrievalChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Pinecone

import pinecone

from helpers import get_vecotrestore

from prompt import QA_PROMPT

def get_bot():
    vectorstore = get_vecotrestore()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0, openai_api_key="openai_api_key"), 
        vectorstore.as_retriever(), 
        memory=memory,
        combine_docs_chain_kwargs={"prompt": QA_PROMPT}
    )