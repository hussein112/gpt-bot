# gpt-bot
A Chatbot using langchain built using dummy hardware csv data and [https://pcandparts.com/](pcandparts) website data
# how it works
Simply put: 
1.	We have a collection of data vectorized and stored in a vector database.
2.	When a user asks a question, we retrieve the most relevant data from the vector store using similarity search.
3.	We pass the most relevant data to the LLM.
4.	Finally, the LLM – using relevant data - generates a response.

# High Level View
<img src="visuals/High Level.png">

# Mid Level View
<img src="visuals/Mid Level.png">
