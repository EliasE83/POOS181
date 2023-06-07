from tkinter import *;
from tkinter import ttk;
from conexion_bd import *;
import tkinter as tk;

instancia = ConexionBD()

def alta():
    instancia.AltaBebidas(varNomb.get(), varClasifica.get(), varMarc.get(), varPreci.get())

def baja():
    instancia.BajaBebidas(varID.get())
    varID.set('')
    messagebox.showinfo("Baja", "Se ha dado de baja la bebida")

def consultar():

    tabla.delete(*tabla.get_children())
    datos = instancia.ConsultarBebidas()
    for row in datos:
        tabla.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

def actualizar():
    instancia.ActualizarBebidas(varId.get(), varNombre.get(), varClasificacion.get(), varMarca.get(), varPrecio.get())
    messagebox.showinfo("Actualización", "Se ha actualizado la bebida")

def promedio():
    tabla.delete(*tabla.get_children())
    datos = instancia.PrecioPromedio()
    for row in datos:
        messagebox.showinfo("Precio promedio", "El precio promedio de las bebidas es: "+str(row[0]))

def cantidadPorMarca():
    tabla.delete(*tabla.get_children())
    datos = instancia.CantBebidasMarca()
    for row in datos:
        tabla.insert('', 'end', text=row[0], values=(row[1]))
        messagebox.showinfo("Cantidad por marca", "Marca: "+str(row[0]) + " Cantidad: "+str(row[1]))

def cantidadPorClas():
    tabla.delete(*tabla.get_children())
    datos = instancia.CantBebidasClas()
    for row in datos:
        tabla.insert('', 'end', text=row[0], values=(row[1]))
        messagebox.showinfo("Cantidad por Clasificacion", "Clasificacion: "+str(row[0]) + " Cantidad: "+str(row[1]))        

ventana = Tk()

ventana.title("Almacén Bebidas")

ventana.geometry("500x500")

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)


#Pestaña 1 Alta Bebidas

titulo = Label(pestana1, text="Alta Bebidas", font=("Arial Bold", 20)).pack()

varNomb= StringVar()
lblNomb = Label(pestana1, text="Nombre: ").pack()
txtNomb = Entry(pestana1, textvariable=varNomb).pack()

varClasifica= StringVar()
lblClasifica = Label(pestana1, text="Clasificación: ").pack()
txtClasifica = Entry(pestana1, textvariable=varClasifica).pack()

varMarc= StringVar()
lblMarc = Label(pestana1, text="Marca: ").pack()
txtMarc = Entry(pestana1, textvariable=varMarc).pack()

varPreci= StringVar()
lblPreci = Label(pestana1, text="Precio: ").pack()
txtPreci = Entry(pestana1, textvariable=varPreci).pack()

#Pestaña 2 Baja Bebidas

titulo = Label(pestana2, text="Baja Bebidas", font=("Arial Bold", 20)).pack()
varID= StringVar()
lblID = Label(pestana2, text="ID: ").pack()
txtID = Entry(pestana2, textvariable=varID).pack()

#Pestaña 3 Consultar Bebidas

titulo = Label(pestana3, text="Consultar Bebidas", font=("Arial Bold", 20)).pack()
tabla = ttk.Treeview(pestana3)
tabla['columns']=('Nombre','Clasificacion','Marca','Precio')
tabla.column('#0', width=50, minwidth=50)
tabla.column('Nombre', width=100, minwidth=100)
tabla.column('Clasificacion', width=100, minwidth=100)
tabla.column('Marca', width=100, minwidth=100)
tabla.column('Precio', width=100, minwidth=100)
tabla.heading('#0', text='ID', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.CENTER)
tabla.heading('Clasificacion', text='Clasificacion', anchor=tk.CENTER)
tabla.heading('Marca', text='Marca', anchor=tk.CENTER)
tabla.heading('Precio', text='Precio', anchor=tk.CENTER)
tabla.pack()
#Pestaña 4 Actualizar Bebidas

titulo = Label(pestana4, text="Actualizar Bebidas", font=("Arial Bold", 20)).pack()
varId= StringVar()
lblID = Label(pestana4, text="ID: ").pack()
txtID = Entry(pestana4, textvariable=varId).pack()

varNombre= StringVar()
lblNombre = Label(pestana4, text="Nombre: ").pack()
txtNombre = Entry(pestana4, textvariable=varNombre).pack()

varClasificacion= StringVar()
lblClasificacion = Label(pestana4, text="Clasificación: ").pack()
txtClasificacion = Entry(pestana4, textvariable=varClasificacion).pack()

varMarca= StringVar()
lblMarca = Label(pestana4, text="Marca: ").pack()
txtMarca = Entry(pestana4, textvariable=varMarca).pack()

varPrecio= StringVar()
lblPrecio = Label(pestana4, text="Precio: ").pack()
txtPrecio = Entry(pestana4, textvariable=varPrecio).pack()

#Botones

btnAlta = Button(pestana1, text="Alta", command=alta).pack()
btnBaja = Button(pestana2, text="Baja", command=baja).pack()
btnConsultar = Button(pestana3, text="Consultar", command=consultar).pack()
btnActualizar = Button(pestana4, text="Actualizar", command=actualizar).pack()
btnPromedio = Button(pestana3, text="Precio promedio de bebidas", command=promedio).pack()
btnCantidadPorMarca = Button(pestana3, text="Cantidad de bebidas por marca", command=cantidadPorMarca).pack()
btnCantidadPorClas = Button(pestana3, text="Cantidad de bebidas por clasificación", command=cantidadPorClas).pack()

panel.add(pestana1, text="Alta Bebidas")
panel.add(pestana2, text="Baja Bebidas")
panel.add(pestana3, text="Consultar Bebidas")
panel.add(pestana4, text="Actualizar Bebidas")

ventana.mainloop()