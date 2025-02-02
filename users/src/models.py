from db import db
from datetime import datetime

class User(db.Model):
    """Modelo para la tabla de usuarios."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # 🔐 Hash en producción
    email = db.Column(db.String(120), unique=True, nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=True)
    full_name = db.Column(db.String(150), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
