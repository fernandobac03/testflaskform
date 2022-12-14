from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS
from procesos.basededatos import datos
import os

#Flask
app = Flask(__name__)
CORS(app)

###
###
@app.route("/formulario", methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        nombre = request.form['txtnombre']
        apellido = request.form['txtapellido']
        edad = request.form['txtedad']
        print(nombre, apellido, edad)
        response_status = datos.Almacenar(nombre,apellido,edad)
        return Response("{'Respuesta':'Se almacenó correctamente'}", status=response_status, mimetype='application/json')
    return render_template('formulario.html')

@app.route("/leer", methods=['GET'])
def read():
    df = datos.Leer()
    print(df)
    return render_template('listar.html', personas=df)

if __name__ == '__main__':
    app.run(debug=True)
