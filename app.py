from crypt import methods
from src.crawler.Crawler import crawler
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search/<term>', methods=['GET'])
def search(term):
    return crawler(term)

if __name__ == '__main__':
    app.run(port=5000)

