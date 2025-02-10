-- crea base de datos
CREATE DATABASE 4thewords_prueba_kembly_munoz;

-- Usa base de datos creada
USE 4thewords_prueba_kembly_munoz;

-- Crea tabla leyendas
CREATE TABLE leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    descripcion TEXT,
    fecha DATE,
    provincia VARCHAR(100),
    canton VARCHAR(100),
    distrito VARCHAR(100),
    imagen_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserta datos de ejemplo
INSERT INTO leyendas (nombre, categoria, descripcion, fecha, provincia, canton, distrito, imagen_url)
VALUES
('La Llorona', 'Leyenda urbana', 'La Llorona es una figura mitológica que llora por sus hijos perdidos...', '2025-02-08', 'San José', 'Central', 'Carmen', 'https://example.com/la-llorona.jpg'),
('El Cadejos', 'Leyenda animal', 'El Cadejos es un perro sobrenatural, protector y guardián...', '2025-01-10', 'Alajuela', 'Central', 'La Fortuna', 'https://example.com/el-cadejos.jpg'),
('La Cegua', 'Leyenda urbana', 'La Cegua es una mujer con la cara desfigurada que busca venganza...', '2024-12-05', 'Cartago', 'Central', 'Cartago', 'https://example.com/la-cegua.jpg'),
('El Sombrerón', 'Leyenda misteriosa', 'El Sombrerón es conocido por su sombrero gigante y su amor por las jóvenes...', '2024-11-15', 'Guanacaste', 'Liberia', 'Cañas', 'https://example.com/el-sombreron.jpg'),
('La Segua', 'Leyenda animal', 'La Segua es una mujer que se transforma en un caballo...', '2024-10-25', 'Puntarenas', 'Central', 'Puntarenas', 'https://example.com/la-segua.jpg'),
('El Espíritu del Bosque', 'Leyenda espiritual', 'Se dice que un espíritu habita los bosques en busca de almas perdidas...', '2024-09-10', 'Heredia', 'Barva', 'San José de la Montaña', 'https://example.com/el-espiritu-del-bosque.jpg'),
('La Loba', 'Leyenda animal', 'La Loba es una criatura mitológica que se dice caza en la oscuridad...', '2024-08-18', 'Alajuela', 'San Ramón', 'Alajuela', 'https://example.com/la-loba.jpg'),
('El Muerto', 'Leyenda urbana', 'El Muerto es el alma errante de un hombre que no descansó en paz...', '2024-07-20', 'San José', 'Escazú', 'San Antonio', 'https://example.com/el-muerto.jpg'),
('La Bruja', 'Leyenda urbana', 'Una mujer que se convierte en bruja para hacer el mal...', '2024-06-12', 'Limón', 'Central', 'Limón', 'https://example.com/la-bruja.jpg'),
('El Chacal', 'Leyenda animal', 'El Chacal es un perro grande con ojos rojos que vigila las montañas...', '2024-05-02', 'Puntarenas', 'Osa', 'Bahía Ballena', 'https://example.com/el-chacal.jpg');
