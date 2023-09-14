from langchain.embeddings.openai import OpenAIEmbeddings

polite_words = [
    'please', 'sorry', 'may'
]

embeddings = OpenAIEmbeddings()


##### Constants
PINECONE_ENV = 'us-west4-gcp-free'
PINECONE_INDEX = 'chatbot'