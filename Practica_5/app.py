#Importar el framework
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask(__name__)

#Configuracion de la conexion a la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='dbflask'
mysql = MySQL(app)

#Declaracion de rutas http://localhost:5000/
@app.route("/")
def index():
    return render_template('index.html')

#Declaracion de rutas http://localhost:5000/guardar tipo post
@app.route("/guardar", methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo,artista,anio)
        
    return "Los datos llegaron por POST"





#Declaracion de rutas http://localhost:5000/
@app.route("/eliminar")
def eliminar():
    return "Se eliminó en la BD"

#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)