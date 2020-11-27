from flask import Flask, jsonify
from functions import read_csv

app = Flask("patito")

def ejemplo(x="a",y="b",z="c"):
    print(x)

@app.route('/json', methods=['GET'])
def ejemplo_json():
    contenido = {"id": 1, "nombre": "Juan", "apellido": "algun apellido"}
    segundo = {"id": 2, "nombre": "Javier", "apellido": "Zepeda"}
    lista = [contenido, segundo]
    return jsonify(lista)


@app.route('/', methods=['GET'])
def home():
    response = read_csv()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)
