

DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS rents;

CREATE TABLE BOOKS(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE AUTHORS(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE CUSTOMERS(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE RENTS(
    id INTEGER PRIMARY KEY,
    book_id INTEGER,
    customer_id INTEGER,
    state TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
-- =====================================================
-- DATOS 
-- =====================================================


INSERT INTO BOOKS(ID,TITLE,AUTHOR_ID)VALUES
(1,'Don Quijote',1),
(2,'La Divina Comedia',2),
(3,'Vagabond 1-3',3),
(4,'Dragon Ball 1',4),
(5,'The Book of the 5 Rings',NULL);

INSERT INTO AUTHORS(ID,NAME)VALUES
(1,'Miguel de Cervantes'),
(2,'Dante Alighieri'),
(3,'Takehiko Inoue'),
(4,'Akira Toriyama'),
(5,'Walt Disney');

INSERT INTO CUSTOMERS(ID,NAME,EMAIL)VALUES
(1,'JOHN DOE','john.doe@example.com'),
(2,'JANE DOE','jane.doe@example.com'),
(3,'LUKE SKYWALKER','luke.skywalker@example.com');

INSERT INTO RENTS(ID,BOOK_ID,CUSTOMER_ID,STATE)VALUES
(1,1,2,'RENTED'),
(2,2,2,'RETURNED'),
(3,1,1,'On time'),
(4,3,1,'On time'),
(5,2,2,'Overdue');

-- =====================================================
-- SELECTS
-- =====================================================


-- 1. Libros y sus autores (si los tienen)
SELECT b.title, a.name AS author
FROM books b
LEFT JOIN authors a ON a.id = b.author_id;

-- 2. Libros sin autor
SELECT b.*
FROM books b
LEFT JOIN authors a ON a.id = b.author_id
WHERE a.id IS NULL;

-- 3. Autores sin libros
SELECT a.*
FROM authors a
LEFT JOIN books b ON b.author_id = a.id
WHERE b.id IS NULL;

-- 4. Libros rentados alguna vez
SELECT DISTINCT b.*
FROM books b
INNER JOIN rents r ON r.book_id = b.id;

-- 5. Libros nunca rentados
SELECT b.*
FROM books b
LEFT JOIN rents r ON r.book_id = b.id
WHERE r.id IS NULL;

-- 6. Clientes que nunca han rentado
SELECT c.*
FROM customers c
LEFT JOIN rents r ON r.customer_id = c.id
WHERE r.id IS NULL;

-- 7. Libros rentados en estado Overdue
SELECT DISTINCT b.*
FROM books b
INNER JOIN rents r ON r.book_id = b.id
WHERE r.state = 'Overdue';