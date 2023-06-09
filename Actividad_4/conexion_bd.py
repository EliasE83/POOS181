from tkinter import messagebox;
import pyodbc;
import bcrypt;



class ConexionBD():

    def conexionbd(self):
        try:
            conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER=ELIAS;DATABASE=Actividad4POO;UID=DBA;PWD=1234')
            return conexion
        except pyodbc.Error as error:
            messagebox.showwarning("Error", "Error al abrir la base de datos")

    def AltaBebidas(self, nombre, clasificacion, marca, precio):
        conx = self.conexionbd()
        if(nombre == '' or clasificacion == '' or marca == '' or precio == ''):
            messagebox.showwarning("Error", "Faltan datos")
            conx.close()
        else:
            conx = self.conexionbd()   
            cursor = conx.cursor()
            sqlInsert = 'INSERT INTO Bebidas (nombre, clasificacion, marca, precio) VALUES (?,?,?,?)'
            datos = (nombre, clasificacion, marca, precio)
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
            conx = self.conexionbd()
            cursor = conx.cursor()
            sqlDelete = 'DELETE FROM Bebidas WHERE id_bebida = '+id+''
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
        if(id == ''):
            messagebox.showwarning('Error', 'Ingrese un ID')
            conx.close()
        else:
            conx = self.conexionbd()
            if(nombre == '' or clasificacion == '' or marca == '' or precio == ''):
                messagebox.showwarning('Error', 'Formulario incompleto.')
                conx.close()
            else:
                cursor = conx.cursor()
                datos = (nombre, clasificacion, marca, precio)
                sqlUpdate = 'update Bebidas set (nombre, clasificacion, marca, precio) = (?,?,?,?) where id = '+id
                cursor.execute(sqlUpdate, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo('Exito', 'Registro actualizado correctamente.')

    def PrecioPromedio(self):
        conx = self.conexionbd()
        cursor = conx.cursor()
        sqlSelect = 'SELECT AVG(precio) FROM Bebidas'
        cursor.execute(sqlSelect)
        datos = cursor.fetchall()
        conx.close()
        return datos
    
    def CantBebidasMarca(self):
        conx = self.conexionbd()
        cursor = conx.cursor()
        sqlSelect = 'SELECT marca, COUNT(marca) FROM Bebidas GROUP BY marca'
        cursor.execute(sqlSelect)
        datos = cursor.fetchall()
        conx.close()
        return datos
    
    def CantBebidasClas(self):
        conx = self.conexionbd()
        cursor = conx.cursor()
        sqlSelect = 'SELECT clasificacion, COUNT(clasificacion) FROM Bebidas GROUP BY clasificacion'
        cursor.execute(sqlSelect)
        datos = cursor.fetchall()
        conx.close()
        return datos
