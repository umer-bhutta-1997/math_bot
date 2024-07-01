from flask import Flask, request, jsonify, make_response

from helper_fn import *

app = Flask(__name__)



@app.route('/query', methods=['POST'])
def process_query_route():
    data = request.get_json()
    query = data.get('query')
    if query is None:
        return 'No query provided', 400
    result = chain(query)
    print(result['output'])
    return make_response(result["output"])

if __name__ == '__main__':
    app.run(debug = True)