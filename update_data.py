from langchain.vectorstores import Pinecone
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings


open_ai_key = 'key'
embeddings = OpenAIEmbeddings(openai_api_key=open_ai_key)

api_key = "api_key"
env = "asia-southeast1-gcp-free"
index_name = "test2"
pinecone.init(api_key=api_key, environment=env)
# return Pinecone.from_texts([t.page_content for t in documents], embeddings, index_name=index_name)

vectorstore = Pinecone.from_existing_index('test2', embeddings)

Pinecone.add_texts(vectorstore, texts=["amar", "shafiq"])