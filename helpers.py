from langchain.vectorstores import Pinecone
import pinecone

import os
import random

from casuals import *
from global_vars import *


def get_vecotrestore():
    """Retrieve the vectorstore to start querying it

    Returns:
        PineconeIndex
    """
    pinecone.init(environment=PINECONE_ENV)
    return Pinecone.from_existing_index(PINECONE_INDEX, embeddings)



def is_first_run(flag_file_path):
    """Determine wheter this is the first time the program executes on the computer.

    Args:
        flag_file_path (string): add a file as a flag.
    """
    if not os.path.exists(flag_file_path): # First Run
        with open(flag_file_path, 'w') as flag_file:
            flag_file.write("Executed")
        return True
    else: # Subsequent Runs
        return False



def casual(question):
    """Determine if the following question is casual.

    Args:
        question (str): The user question

    Returns:
        Boolean: Casuality Indication
        String: Casual Response for the Casual question.
    """
    for category, questions in casuals.items():
        if question.lower() in questions:
            return True, random.choice(casual_response[category])
    return False, None


def pre_process(question):
    """Remove polite tokens from the question

    Args:
        question (str): the user question
    """
    txt = question.split()
    for polite_token in polite_words:
        if polite_token in question:
            txt.remove(polite_token)
    return " ".join(w for w in txt)