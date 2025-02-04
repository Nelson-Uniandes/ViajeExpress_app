from dotenv import load_dotenv
import os
from flask import Flask
from db import db
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

# Registrar las rutas del microservicio
register_routes(app)

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    load_dotenv(override=True)
    port = int(os.getenv("CONFIG_PORT", 3000)) 
    print(f"Using port: {port}")  # Depuración
    app.run(host="0.0.0.0", port=port)
