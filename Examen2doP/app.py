#Importacion del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del Servidor
app=Flask(__name__,)

#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        vnombre = request.form['flor']
        vcantidad = request.form['cantidad']
        vprecio = request.form['precio']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tbflores (nombre, cantidad, precio) VALUES (%s, %s, %s)',(vnombre, vcantidad, vprecio))
        mysql.connection.commit()

        return render_template('mensaje.html')
    
@app.route('/consultar')
def consultar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbflores')
    data = cur.fetchall()
    return render_template('registros.html', flores = data)

@app.route("/eliminar/<id>")
def eliminar(id):
    cs = mysql.connection.cursor()
    cs.execute('select * from tbflores where id_flor = %s', (id,))
    consultaFlor = cs.fetchall()
    return render_template('borrar.html', flores=consultaFlor)

@app.route("/eliminarenBD/<id>")
def eliminarenBD(id):
    cs = mysql.connection.cursor()
    cs.execute('delete from tbflores where id_flor = %s', (id,))
    mysql.connection.commit()
    return render_template("mensaje.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)