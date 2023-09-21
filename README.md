# gpt-bot
A Customer support Chatbot built using langchain. <br>
the bot is able to answer user questions about the company products, make comparison between two products, and provide the end user with the pros and cons of each product. <br>
built using dummy hardware csv data and [pcandparts](https://pcandparts.com/) website data
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
