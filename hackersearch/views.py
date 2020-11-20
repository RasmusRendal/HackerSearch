from hackersearch import app
from flask import render_template, request, redirect, url_for

import truequery
from miniengine import Result
import some


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/', methods=['GET'])
def search():
    if 'query' not in request.args:
        return redirect(url_for('index'))
    query_text = request.args['query']
    query = truequery.parse(query_text)
    results = some.search(query)
    return render_template('search.html', query=query_text, results=results)
