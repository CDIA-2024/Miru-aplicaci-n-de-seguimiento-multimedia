use miru;
-- Una sola tabla (mostrando todos los datos)
select * from contenido;
-- Una sola tabla (mostrando algunas columnas)
select nombre, correo, edad from usuario;
-- Una sola tabla con where
select * from contenido where id_genero = 2;
--  Una sola tabla con where utilizando between
SELECT nombre, edad FROM usuario WHERE edad BETWEEN 25 AND 30;
-- Una sola tabla con where utilizando limit
SELECT * FROM contenido WHERE id_genero = 1 LIMIT 10;
-- Más de 1 tabla con inner join
SELECT contenido.titulo, genero.nombre AS nombre_genero
FROM contenido
INNER JOIN genero ON contenido.id_genero = genero.id_genero;
-- Más de 1 tabla con inner join y con filtros
SELECT contenido.titulo, genero.nombre AS nombre_genero
FROM contenido
INNER JOIN genero ON contenido.id_genero = genero.id_genero
WHERE contenido.anio_lanzamiento > 2000 AND genero.nombre = 'Terror';
