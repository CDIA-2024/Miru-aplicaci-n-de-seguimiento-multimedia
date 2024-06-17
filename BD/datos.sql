use miru;
-- Tabla estado (queda como está)
INSERT INTO estado (nombre_estado) VALUES 
("finalizado"),
("en emisión");

-- Tabla usuario
INSERT INTO usuario (nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion) VALUES 
("maxi", "maxi@email.com", "max", "1993-10-20", 29, "todo", 1),
("pedro", "pedro@m.com", "pedri", "2000-06-20", 23, "infantiles", 1),
("chaos", "cesiaf@gmail.com", "1234", "2002-09-24", 21, "psicológico", 1),
("kashmir", "valef51@gmail.com", "123", "2001-12-20", 22, "terror", 1);

-- Tabla desarrollador
INSERT INTO desarrollador (nombre) VALUES
("Bethesda"),
("Niantic"),
("Square Enix"),
("Rockstar Games"),
("Ubisoft");

-- Tabla director
INSERT INTO director (nombre) VALUES
("Justin Benson"),
("Tim Burton"),
("Matt Groening"),
("Andrew Adamson"),
("Ivan Reitman"),
("Steven Spielberg"),
("James Cameron"),
("Quentin Tarantino");

-- Tabla productora
INSERT INTO productora (nombre) VALUES
("Sony Pictures"),
("Walt Disney"),
("21st Century Fox"),
("DreamWorks"),
("Columbia Pictures"),
("Paramount Pictures"),
("Universal Pictures"),
("Warner Bros");

-- Tabla genero
INSERT INTO genero (nombre) VALUES
("Comedia"),
("Terror"),
("RPG"),
("Shonen"),
("Acción"),
("Drama"),
("Ciencia Ficción");

-- Tabla estudioanimacion
INSERT INTO estudioanimacion (nombre) VALUES
("Toei"),
("Pierrot"),
("Madhouse"),
("Studio Ghibli"),
("Bones");

-- Tabla contenido
INSERT INTO contenido (titulo, anio_lanzamiento, id_genero) VALUES
("Shrek", 2001, 1),              -- id 1
("Cazafantasmas", 1984, 2),      -- id 2
("Doom", 1993, 3),               -- id 3
("Pokemon", 1996, 3),            -- id 4
("Loki", 2021, 5),               -- id 5
("Los Simpsons", 1989, 1),       -- id 6
("Bleach", 2004, 4),             -- id 7
("Dragon Ball", 1984, 4),        -- id 8
("The Matrix", 1999, 7),         -- id 9
("Titanic", 1997, 6),            -- id 10
("The Godfather", 1972, 6),      -- id 11
("Breaking Bad", 2008, 6),       -- id 12
("Stranger Things", 2016, 7),    -- id 13
("Game of Thrones", 2011, 6),    -- id 14
("Naruto", 2002, 4),             -- id 15
("Final Fantasy VII", 1997, 3),  -- id 16
("Zelda: Ocarina of Time", 1998, 3); -- id 17

-- Tabla lista
INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES
("2024-06-13", 1, 4, "maxlist"),
("2023-07-01", 2, 1, "mi_list"),
("2024-06-16", 4, 2, "terror"),

-- Tabla videojuego
INSERT INTO videojuego (id_contenido, plataforma, id_desarrolador) VALUES
(3, "pc", 1),           -- Doom
(4, "game boy", 2),     -- Pokemon
(16, "ps1", 3),         -- Final Fantasy VII
(17, "n64", 5);         -- Zelda: Ocarina of Time

-- Tabla anime
INSERT INTO anime (id_contenido, capitulos, id_estudio, id_estado) VALUES
(7, 392, 2, 2),         -- Bleach
(8, 600, 1, 2),         -- Dragon Ball
(15, 220, 1, 1);        -- Naruto

-- Tabla serie
INSERT INTO serie (id_contenido, temporadas, id_director, id_productora, id_estado) VALUES
(5, 2, 1, 2, 1),       -- Loki
(6, 35, 3, 3, 2),      -- Los Simpsons
(12, 5, 6, 6, 1),      -- Breaking Bad
(13, 4, 7, 7, 1),      -- Stranger Things
(14, 8, 8, 8, 2);      -- Game of Thrones

-- Tabla pelicula
INSERT INTO pelicula (id_contenido, duracion, id_director, id_productora) VALUES
(1, 89, 4, 4),         -- Shrek
(2, 75, 5, 5),         -- Cazafantasmas
(9, 136, 6, 6),        -- The Matrix
(10, 195, 7, 7),       -- Titanic
(11, 175, 8, 8);       -- The Godfather

-- Tabla registro
INSERT INTO registro (puntuacion, id_estado, id_usuario, id_contenido) VALUES
(7.5, 2, 1, 6),        -- Los Simpsons
(9.0, 2, 2, 4),        -- Pokemon
(8.5, 2, 3, 10),       -- Titanic
(7.0, 1, 4, 2),        -- Cazafantasmas
(8.0, 2, 1, 5);        -- Loki

-- Tabla reseña
INSERT INTO reseña (fecha_creacion, texto, id_usuario, id_contenido, id_registro) VALUES
("2024-06-16", "Las primeras temporadas son magnificas, las demás con el pasar de tiempo perdieron su magia.", 1, 6, 1), -- Los Simpsons
("2020-12-28", "Un juego muy divertido y mucho más fácil de comprender que otros RPG.", 2, 4, 2), -- Pokemon
("2024-06-17", "Una película conmovedora con actuaciones impresionantes.", 3, 10, 3), -- Titanic
("2024-06-17", "Un clásico del terror que nunca pasa de moda.", 4, 2, 4), -- Cazafantasmas
("2024-06-17", "Una serie increíblemente emocionante.", 1, 5, 5); -- Loki
