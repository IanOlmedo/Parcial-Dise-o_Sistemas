import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from models.base_model import BaseModel  # Base general de tus modelos

# Carga las variables de entorno
env_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(env_path)

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


class Database:
    _instance = None
    engine = create_engine(DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def __init__(self):
        self._session = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._engine = cls.engine
            cls._instance._SessionLocal = cls.SessionLocal
        return cls._instance

    def get_session(self) -> Session:
        if self._session is None:
            self._session = self._SessionLocal()
        return self._session

    def drop_database(self):
        try:
            BaseModel.metadata.drop_all(self._engine)
            print("Tables dropped.")
        except Exception as e:
            print(f"Error dropping tables: {e}")

    def create_tables(self):
        try:
            BaseModel.metadata.create_all(self._engine)
            print("Tables created.")
        except Exception as e:
            print(f"Error creating tables: {e}")

    def close_session(self):
        if hasattr(self, "_session"):
            self._session.close()
            del self._session

    def check_connection(self):
        try:
            with self._engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Connection established.")
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False

# Función para obtener la sesión de base de datos
def get_db():
    db_instance = Database()
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db_instance.close_session()

# Crear una instancia de la base de datos y verificar la conexión
db_instance = Database()
connected = db_instance.check_connection()
print("Connected to database:" if connected else "Not connected to database.")


