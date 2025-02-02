import os
from dotenv import load_dotenv

class Config:
    """Configuración de la aplicación y base de datos."""

    # Cargar variables desde el archivo .env si existe
    load_dotenv()

    #SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Imprimir configuración en consola (útil para depuración)
    print(f"[*] Conectando a la base de datos: {SQLALCHEMY_DATABASE_URI}")

