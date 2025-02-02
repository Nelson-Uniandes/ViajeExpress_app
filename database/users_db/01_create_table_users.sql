-- Crear la tabla users
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    phoneNumber VARCHAR(15),
    dni VARCHAR(20),
    fullName VARCHAR(100),
    password VARCHAR(255) NOT NULL,
    salt VARCHAR(255) NOT NULL,
    token VARCHAR(255),
    status VARCHAR(20) NOT NULL CHECK (status IN ('POR_VERIFICAR', 'NO_VERIFICADO', 'VERIFICADO')),
    expireAt TIMESTAMP,
    createdAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Crear índices
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username ON users(username);