from db import db
from datetime import datetime
import uuid


class User(db.Model):
    """Modelo para la tabla de usuarios."""
    __tablename__ = 'users'  # 📌 Especifica el nombre correcto de la tabla
    
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    dni = db.Column(db.String(20), nullable=True)
    full_name = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(20), nullable=False, 
                       default='POR_VERIFICAR', 
                       check_constraint="status IN ('POR_VERIFICAR', 'NO_VERIFICADO', 'VERIFICADO')")
    expire_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        return f"<User {self.username}>"
