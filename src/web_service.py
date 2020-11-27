from flask import Flask, jsonify
from functions import read_csv

app = Flask("evaluacion_g5")

@app.route('/', methods=['GET'])
def home():
    response = read_csv()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)
