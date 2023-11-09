-- Crear la tabla 'users'
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password TEXT,
    UNIQUE (username)
);

-- Crear la tabla 'posts'
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    author INT NOT NULL,
    title VARCHAR(100),
    body TEXT,
    dateTime DATETIME NOT NULL,
    FOREIGN KEY (author) REFERENCES users(id)
);

-- Crear la tabla 'comentarios'
CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto TEXT NOT NULL,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor_id INT NOT NULL,
    post_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES users(id),
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

-- Crear la tabla 'categorias'
CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    UNIQUE (nombre)
);
