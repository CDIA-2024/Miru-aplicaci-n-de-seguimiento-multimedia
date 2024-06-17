use miru;

INSERT INTO estado (nombre_estado) VALUES 
("finalizado"),
("en emisión");
INSERT INTO usuario (nombre, correo, contrasena, año_nacimiento, edad, genero_de_interes, suscripcion) VALUES 
("maxi", "maxi@email.com", "max", "1993-10-20", 29, "todo", 1),
("pedro", "pedro@m.com", "pedri", "2000-06-20", 23, "infantiles", 1);
INSERT INTO desarrollador (nombre) VALUES
("Bethesda"),
("Niantic");
INSERT INTO director (nombre) VALUES
("Justin Benson"),
("Tim Burton"),
("Matt Groening"),
("Andrew Adamson"),
("Ivan Reitman");
INSERT INTO productora (nombre) VALUES
("Sony Pictures"),
("Walt Disney"),
("21st Century Fox"),
("DreamWorks"),
("Columbia Pictures");
INSERT INTO genero (nombre) VALUES
("Comedia"),
("Terror"),
("RPG"),
("Shonen");
INSERT INTO estudioanimacion (nombre) VALUES
("Toei"),
("Pierot");
INSERT INTO contenido (titulo, anio_lanzamiento, id_genero) VALUES
("Shrek", 2001, 1),
("Cazafantasmas", 1984, 2),
("Doom", 1993, 2),
("Pokemon", 1996, 3),
("Loki", 2021, 1),
("Los Simpsons", 1989, 1),
("Bleach", 2004, 4),
("Dragon Ball", 1984, 4);
INSERT INTO lista (fecha_creacion, id_usuario, id_contenido, nombre) VALUES
("2024-06-13", 1, 4, "maxlist"),
("2023-07-01", 2, 1, "mi_list");
INSERT INTO videojuego (id_contenido, plataforma, id_desarrolador) VALUES
(3, "pc", 1),
(4, "game boy", 2);
INSERT INTO anime (id_contenido, capitulos, id_estudio, id_estado) VALUES
(7, 392, 2, 2),
(8, 600, 1, 2);
INSERT INTO serie (titulo, id_contenido, temporadas, id_director, id_productora, id_estado) VALUES
("Loki", 5, 2, 1, 2, 1),
("Los Simpsons", 6, 35, 3, 3, 2);
INSERT INTO pelicula (id_contenido, duracion, id_director, id_productora) VALUES
(1, 89, 4, 4),
(2, 75, 5, 5);
INSERT INTO registro (puntuacion, id_estado, id_usuario, id_contenido) VALUES
(7.5, 2, 1, 6),
(9.0, 2, 2, 4);
INSERT INTO reseña (fecha_creacion, texto, id_usuario, id_contenido, id_registro) VALUES
("2024-06-16", "Las primeras temporadas son magnificas, las demas con el pasar de tiempo perdieron du magia.", 1, 6, 1),
("2020-12-28", "Un juego muy divertido y mucho mas facil de comprender que otros rpg.", 2, 4, 2);
