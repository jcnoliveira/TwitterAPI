from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app


es = Elasticsearch([{'host': 'localhost'}])

app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

@app.route('/', methods=['GET'])
def index():
    results = es.get(index='contents', doc_type='title', id='my-new-slug')
    return jsonify(results['_source'])


@app.route('/insert_data', methods=['POST'])
def insert_data():
    slug = request.form['slug']
    title = request.form['title']
    content = request.form['content']

    body = {
        'slug': slug,
        'title': title,
        'content': content,
        'timestamp': datetime.now()
    }

    result = es.index(index='contents', doc_type='title', id=slug, body=body)

    return jsonify(result)

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']

    body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["content", "title"]
            }
        }
    }

    res = es.search(index="contents", doc_type="title", body=body)

    return jsonify(res['hits']['hits'])

app.run(port=8090, debug=True)