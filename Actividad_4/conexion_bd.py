from tkinter import messagebox;
import sqlite3;
import bcrypt;



class ConexionBD():

    def conexionbd(self):
        try:
            conexion = sqlite3.connect("C:/laragon/www/POOS181/Actividad_4/BDActividad4.db")
            return conexion
        except sqlite3.OperationalError:
            messagebox.showwarning("Error", "Error al abrir la base de datos")

    def AltaBebidas(self, nombre, clasificacion, marca, precio):
        conx = self.conexionbd()
        if(nombre == '' or clasificacion == '' or marca == '' or precio == ''):
            messagebox.showwarning("Error", "Faltan datos")
            conx.close()
        else:   
            cursor = conx.cursor()
            datos = (nombre, clasificacion, marca, precio)
            sqlInsert = '''INSERT INTO Bebidas (Nombre, Clasificacion, Marca, Precio) VALUES ('{}','{}','{}','{}')'''.format(nombre, clasificacion, marca, precio)
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Alta", "Se ha dado de alta la bebida")

    def BajaBebidas(self, id):
        conx = self.conexionbd()
        if(id == ''):
            messagebox.showwarning("Error", "Faltan datos")
            conx.close()
        else:
            cursor = conx.cursor()
            sqlDelete = 'DELETE FROM Bebidas WHERE ID = '+id+''
            cursor.execute(sqlDelete, (id,))
            conx.commit()
            conx.close()
            messagebox.showinfo("Baja", "Se ha dado de baja la bebida") 

    def ConsultarBebidas(self):
        conx = self.conexionbd()
        cursor = conx.cursor()
        sqlSelect = 'SELECT * FROM Bebidas'
        cursor.execute(sqlSelect)
        datos = cursor.fetchall()
        conx.close()
        return datos
    
    def ActualizarBebidas(self, id, nombre, clasificacion, marca, precio):
        conx = self.conexionbd()
        if(id == '' or nombre == '' or clasificacion == '' or marca == '' or precio == ''):
            messagebox.showwarning("Error", "Faltan datos")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (id, nombre, clasificacion, marca, precio)
            sqlUpdate = 'update Bebidas set (nombre, clasificacion, marca, precio) = (?,?,?,?) where id = '+id+''
            cursor.execute(sqlUpdate, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Actualizar", "Se ha actualizado la bebida")