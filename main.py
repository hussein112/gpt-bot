from flask import Flask, jsonify, request
from flask_cors import CORS


from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app) # For localhost


from helpers import casual, pre_process
from helpers import is_first_run
from bot import *


if(is_first_run('frf.txt')):
    bot = create_bot()
else:
    bot = get_bot()

cache = []

@app.route('/chat', methods=['GET'])
def test_route():
    global bot
    args = request.args
    question = args.get('question')

    question = pre_process(question)

    is_casual, response = casual(question)
    if(is_casual):
        cache.append((question, response))
        return jsonify({'answer': response})

    for QA in cache:
        if question == QA[0]:
            return jsonify({'answer': QA[1]})

    result = bot({"question": question})
    response = {'answer': result['answer']}
    cache.append((question, response['answer']))
    return jsonify(response)

@app.route('/reset', methods=['POST'])
def reset_chat():
    """Start a new Conversation
    """
    global bot
    cache.clear()
    bot = get_bot()
    return "New Conversation Started"

if __name__ == '__main__':
    app.run()