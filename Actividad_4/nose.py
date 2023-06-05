import os
import sqlite3
import os
import sqlite3

# Establecer la ruta de la biblioteca DLL de SQLite
sqlite_dll_path = r"C:\Users\mayor\AppData\Local\Programs\Python\Python311\sqlite3\sqlite3.dll"
os.environ['PY_SQLITE_DLL'] = sqlite_dll_path

# Resto del código...

# Cargar la biblioteca DLL de SQLite
sqlite3.dll = sqlite_dll_path

# Realizar operaciones de SQLite
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO test VALUES (1, "Ejemplo")')
cursor.execute('SELECT * FROM test')
print(cursor.fetchall())
conn.close()
