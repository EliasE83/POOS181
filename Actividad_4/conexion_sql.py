import pyodbc   # Libreria para la conexion con SQL Server

try:
        connection=pyodbc.connect('DRIVER={SQL SERVER};SERVER=ELIAS;DATABASE=Actividad4POO;UID=DBA;PWD=1234')
        print("Conexion exitosa")
        cursor=connection.cursor()
        cursor.execute("SELECT @@version;")
        row=cursor.fetchone()
        print(row)
        cursor.execute("select * from Bebidas")
        rows=cursor.fetchall()
        for row in rows:
            print(row) 
except Exception as ex:
        print(ex)
        print("Conexion fallida")