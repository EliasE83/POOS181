from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'DB_Fruteria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route("/")
def Index():
    return render_template('ingreso.html')

@app.route("/ingreso", methods=['POST'])
def ingreso():
    if request.method == 'POST':
        vfruta = request.form['fruta']
        vtemporada = request.form['temporada']
        vprecio = request.form['precio']
        vstock = request.form['stock']

        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO tbfrutas (fruta, temporada, precio, stock) VALUES (%s, %s, %s, %s)', (vfruta, vtemporada, vprecio, vstock))
        mysql.connection.commit()

        flash('Fruta agregada satisfactoriamente')
        return render_template('ventanaemergente.html')

@app.route("/listado")
def listado():
    cs = mysql.connection.cursor()
    cs.execute('SELECT * FROM tbfrutas')
    data = cs.fetchall()
    return render_template('consultaregistros.html', frutas = data)

#Consultar
@app.route("/consulta")
def consulta():
    return render_template('consultapornombre.html')

@app.route("/consultanombre")
def consultanombre():
    vfrutas = request.form.get('frutas', False)
    cs = mysql.connection.cursor()
    cs.execute('select * from tbfrutas where fruta = %s order by fruta', [vfrutas])
    data = cs.fetchone()
    print(data)
    return render_template('consultapornombre.html', fruta = data)


#Actualizar
@app.route("/actualizar/<id>")
def actualizar(id):
    cs = mysql.connection.cursor()
    cs.execute('select * from tbfrutas where id_fruta = %s', (id,))
    data = cs.fetchone()
    return render_template('editarRegistro.html', frutas = data)

@app.route("/actualizarRegistro/<id>", methods=['POST'])
def actualizarRegistro(id):
    if request.method == 'POST':
        vfruta = request.form['fruta']
        vtemporada = request.form['temporada']
        vprecio = request.form['precio']
        vstock = request.form['stock']

        cs = mysql.connection.cursor()
        cs.execute('update tbfrutas set fruta = %s, temporada = %s, precio = %s, stock = %s where id_fruta = %s', (vfruta, vtemporada, vprecio, vstock, id))
        mysql.connection.commit()
    
    flash('Fruta actualizada satisfactoriamente')
    return redirect(url_for('listado'))    
#Eliminar
@app.route("/eliminar/<id>")
def eliminar(id):
    cs = mysql.connection.cursor()
    cs.execute('select * from tbfrutas where id_fruta = %s', (id,))
    datos = cs.fetchone()
    return render_template('mensajeliminar.html', frutas = datos)

@app.route("/eliminarRegistro/<id>", methods=['POST'])
def eliminarRegistro(id):
    cs = mysql.connection.cursor()
    cs.execute('delete from tbfrutas where id_fruta = %s', (id,))
    mysql.connection.commit()

    flash('Fruta eliminada satisfactoriamente')
    return redirect(url_for('listado'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)