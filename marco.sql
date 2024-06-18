-- Create tables
CREATE TABLE estudiantes (
    estudiante_id INT PRIMARY KEY,
    rut VARCHAR(11),
    alumno VARCHAR(20),
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    edad INT,
    carrera_id INT
);

CREATE TABLE cursos (
    curso_id INT PRIMARY KEY,
    nombre_curso VARCHAR(20),
    creditos INT,
    carrera_id INT
);

CREATE TABLE facultades (
    facultad_id INT PRIMARY KEY,
    nombre_facultad VARCHAR(20),
    directores VARCHAR(20)
);

CREATE TABLE carreras (
    carrera_id INT PRIMARY KEY,
    nombre_carrera VARCHAR(20),
    duracion INT,
    facultad INT
);

-- Insert data into tables
INSERT INTO estudiantes (estudiante_id, rut, alumno, nombre, apellido, edad, carrera_id)
VALUES
    (1, '11111111-k', 'Juan', 'Perez', 20, 1),
    (2, '22222222-k', 'María', 'Lopez', 21, 2),
    (3, '2222222-k', 'Carlos', 'García', 22, 1),
    (4, '44444444-4', 'Laura', 'Martínez', 23, 3);

INSERT INTO cursos (curso_id, nombre_curso, creditos, carrera_id)
VALUES
    (1, 'Calculo 1', 4, 1),
    (2, 'Anatomía', 5, 2),
    (3, 'Microeconomía', 3, 3),
    (4, 'Programación', 4, 1);

INSERT INTO facultades (facultad_id, nombre_facultad, directores)
VALUES
    (1, 'Ingeniería', 'Dr. Lopez'),
    (2, 'Medicina', 'Dra. Gomez'),
    (3, 'Economía', 'Dr. Ramirez');

INSERT INTO carreras (carrera_id, nombre_carrera, duracion, facultad)
VALUES
    (1, 'Ingeniería', 5, 1),
    (2, 'Medicina', 6, 2),
    (3, 'Economía', 4, 3);
    