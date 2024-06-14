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
("Tim Burton"),
("John Ford");
INSERT INTO productora (nombre) VALUES
("Sony Pictures"),
("Walt Disney");
INSERT INTO genero (nombre) VALUES
("Comedia"),
("Terror"),
("RPG"),
("Shonen");
INSERT INTO estudioanimacion (nombre) VALUES
("Toei"),
("Pierrot");
INSERT INTO contenido (titulo, anio_lanzamiento, id_genero) VALUES
("Shrek", 2001, 1),
("Cazafantasmas", 1984, 2),
("Doom", 1993, 2),
("Pokemon", 1996, 3),
("Loki", 2021, 1),
("Los Simpsons", 1989, 1),
("Bleach", 2004, 4),
("Dragon Ball", 1984, 4);