from flask import Blueprint, request, jsonify
from models import User
from db import db
from utils.security import hash_password, generate_auth_token
from datetime import datetime

users_bp = Blueprint('users', __name__)

# 📌 Endpoint para crear un usuario
@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json

    # Validar campos requeridos
    required_fields = ["username", "password", "email"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "username, password, and email are required"}), 400

    # Verificar si el usuario ya existe
    if User.query.filter((User.username == data["username"]) | (User.email == data["email"])).first():
        return jsonify({"error": "Username or email already exists"}), 412

    # Crear usuario con contraseña encriptada
    new_user = User(
        username=data["username"],
        password=hash_password(data["password"]),
        email=data["email"],
        dni=data.get("dni"),
        full_name=data.get("fullName"),
        phone_number=data.get("phoneNumber"),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "createdAt": new_user.created_at.isoformat() + "Z"
    }), 201

# 📌 Endpoint para verificar que el servicio está activo
@users_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Users microservice is running"}), 200

# 📌 Endpoint para resetear la base de datos (solo pruebas)
@users_bp.route('/reset', methods=['POST'])
def reset_db():
    try:
        db.session.query(User).delete()
        db.session.commit()
        return jsonify({"message": "Database reset successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
