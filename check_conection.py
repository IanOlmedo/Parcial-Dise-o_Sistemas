from config.database import Database

# Crear instancia de base de datos y verificar conexión
db = Database()
if db.check_connection():
    print("Conexión a la base de datos exitosa.")
else:
    print("No se pudo conectar a la base de datos.")
