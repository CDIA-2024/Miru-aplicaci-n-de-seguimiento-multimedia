use miru;
-- Consultamos a todos los usuarios mayores de edad
select * from usuario where edad >= 18;
-- Consultamos los usuarios que el Email comeince con "pedro"
select * from usuario where email like "pedro%";
-- Solamente mostramos los titulos de nuestros contenidos
select titulo from contenido;
-- Consulta contenido de este milenio
select * from contenido where anio_lanzamiento >= 2000;
-- Consulta de Generos para Contenidos
select nombre from genero;
