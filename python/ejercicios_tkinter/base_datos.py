import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database = "",
            password = "",
            user = ""  
        )
        print ("Conexión exitosa a la base de datos")
        return conexion
    
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
    