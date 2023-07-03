#Importar el framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask(__name__)

#Configuracion de la conexion a la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='dbflask'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#Declaracion de rutas http://localhost:5000/
@app.route("/")
def index():
    cc = mysql.connection.cursor()
    cc.execute('select * from tb_albums')
    consultaAlbums = cc.fetchall()
    #print (consultaAlbums)
    return render_template('index.html', lsAlbums = consultaAlbums)

#Declaracion de rutas http://localhost:5000/guardar tipo post
@app.route("/guardar", methods=['POST'])
def guardar():
    if request.method == 'POST':
        #Pasamos a las variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        
        #Conectar nuestra BD y ejecutar el insert

        cs = mysql.connection.cursor()
        cs.execute('insert into tb_albums (titulo, artista, anio) values (%s, %s, %s)', (Vtitulo, Vartista, Vanio))
        mysql.connection.commit()

    flash('Los datos se guardaron correctamente')
    return redirect(url_for('index'))





#Declaracion de rutas http://localhost:5000/
@app.route("/eliminar")
def eliminar():
    return "Se eliminó en la BD"

#Ruta con parametros
@app.route("/actualizar/<id>")
def actualizar(id):
    cs = mysql.connection.cursor()
    cs.execute('select * from tb_albums where id_album = %s', (id,))
    consultaAlbumID = cs.fetchone()
    return render_template('editarAlbum.html', album=consultaAlbumID)

@app.route("/actualizarBD/<id>", methods=['POST'])
def actualizarBD(id):
    return ""

#Ejecucion del Servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)