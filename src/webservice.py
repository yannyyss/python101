from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json',methods=['GET'])
def ejemplo_json():
    contenido = {"id":1,"nombre":"Juan","apellido":"algun apellido"}
    segundo = {"id":1,"nombre":"Javier","apellido":"Zepeda"}
    lista = [contenido,segundo]
    return jsonify(lista)

#la funcion se va a ejecutar cuando vaya esa ruta
@app.route('/', methods=['GET'])
def saludo():
    return "Hola enrouters"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")