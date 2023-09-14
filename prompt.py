from langchain.prompts.prompt import PromptTemplate

prompt_template = """You are the AI assistant for PCANDPARTS.COM hardware store. Your name is Botty.

Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""
QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
