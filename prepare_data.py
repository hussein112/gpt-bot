from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import CSVLoader, UnstructuredFileLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

from global_vars import embeddings, PINECONE_ENV, PINECONE_INDEX

def load_split_data(path, CSV=None, TEXT=None):
    """ 
    Load dataset, split into smaller documents.
    
    Args:
        path: The path to the csv/txt file.
    """
    if(TEXT):
        loader = UnstructuredFileLoader(path)
        raw_documents = loader.load() 
    elif(CSV):
        loader = CSVLoader(path)
        raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=15)
    return text_splitter.split_documents(raw_documents)


def create_vectors(documents):
    """Add the loaded document into the vectorstore index.

    Args:
        documents (Documents): the documents to be added to the index.

    Returns:
        PineconeIndex: we can use similarity search on it.
    """
    pinecone.init(environment=PINECONE_ENV)
    return Pinecone.from_texts([t.page_content for t in documents], embeddings, index_name=PINECONE_INDEX)


def count_tokens(documents):
    """An approximation count of the number of tokens within the given documents. [Used for cost calculations]
    """
    tokens = []
    for document in documents:
        tokens.append(document.split())