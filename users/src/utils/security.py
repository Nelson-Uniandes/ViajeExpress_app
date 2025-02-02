import bcrypt
import uuid

def hash_password(password):
    """Hashea la contraseña antes de almacenarla en la base de datos."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def generate_auth_token():
    """Genera un token aleatorio (NO JWT)."""
    return str(uuid.uuid4())
