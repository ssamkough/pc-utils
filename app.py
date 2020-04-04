from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'pc': 'utils'})


PORT = 8000

if __name__ == '__main__':
    app.run(port=PORT, debug=True)
