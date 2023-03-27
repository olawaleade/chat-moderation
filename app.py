from flask import Flask, render_template, request, jsonify, Response
import requests
import json
import codecs
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()



@app.route('/chat', methods=['GET', 'POST'])
def chat():
    api_url = os.getenv("CHAT_API_URL")
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        chat_data = {'name': name, 'text': text}
        response = requests.post(api_url, json=chat_data)
        response.encoding = 'utf-8'
        decoded_response = codecs.decode(response.text.encode(), 'unicode_escape')
        return Response(decoded_response, content_type='text/plain; charset=utf-8')
    else:
        return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug = True)


"""
@app.route('/webclient')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    input_data = request.form['text']
    api_url = 'https://xyr7no9012.execute-api.ap-northeast-1.amazonaws.com/chatapi/chat/'
    response = requests.get(api_url, params={'text': input_data})
    data = response.json()
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=False)
"""