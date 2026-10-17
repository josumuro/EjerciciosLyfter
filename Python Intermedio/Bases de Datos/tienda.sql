
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS shopping_cart_products;
DROP TABLE IF EXISTS shopping_carts;
DROP TABLE IF EXISTS invoice_products;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    code        VARCHAR(20)   UNIQUE NOT NULL,
    name        VARCHAR(100)  NOT NULL,
    price       DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    entry_date  DATE          NOT NULL DEFAULT (date('now')),
    brand       VARCHAR(50)   NOT NULL,
    stock       INT           NOT NULL DEFAULT 0 CHECK (stock >= 0)
);


CREATE TABLE invoices (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATETIME      NOT NULL DEFAULT (datetime('now')),
    buyer_email   VARCHAR(100)  NOT NULL CHECK (buyer_email LIKE '%_@_%._%'),
    total         DECIMAL(10,2) NOT NULL CHECK (total >= 0)
);


-- -----------------------------------------------------
CREATE TABLE invoice_products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id  INT           NOT NULL REFERENCES invoices(id) ON DELETE CASCADE,
    product_id  INT           NOT NULL REFERENCES products(id),
    quantity    INT           NOT NULL CHECK (quantity > 0),
    total       DECIMAL(10,2) NOT NULL CHECK (total >= 0),
    UNIQUE (invoice_id, product_id)   -- un producto no se repite en la misma factura
);


CREATE TABLE shopping_carts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer_email VARCHAR(100) UNIQUE NOT NULL CHECK (buyer_email LIKE '%_@_%._%')
);

CREATE TABLE shopping_cart_products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id     INT NOT NULL REFERENCES shopping_carts(id) ON DELETE CASCADE,
    product_id  INT NOT NULL REFERENCES products(id)       ON DELETE CASCADE,
    quantity    INT NOT NULL DEFAULT 1 CHECK (quantity > 0),
    UNIQUE (cart_id, product_id)
);

CREATE TABLE employees (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    code  VARCHAR(20)  UNIQUE NOT NULL,
    name  VARCHAR(100) NOT NULL
);

ALTER TABLE invoices ADD buyer_phone VARCHAR(20);

ALTER TABLE invoices ADD cashier_code VARCHAR(20) REFERENCES employees(code);


-- =====================================================
-- DATOS DE PRUEBA 
-- =====================================================(
PRAGMA foreign_keys = ON;

INSERT INTO products (code, name, price, brand, stock) VALUES
    ('P-001', 'Filtro de aceite',   12500.00, 'Bosch',  40),
    ('P-002', 'Bateria 12V',        85000.00, 'Duncan', 15),
    ('P-003', 'Llanta 205/55R16',   62000.00, 'Michelin', 20),
    ('P-004', 'Bujia',               3990.00, 'NGK',   100);

INSERT INTO employees (code, name) VALUES ('E-01', 'Ana Mora'), ('E-02', 'Luis Rojas');

INSERT INTO invoices (buyer_email, total, buyer_phone, cashier_code) VALUES
    ('maria@mail.com', 97500.00, '+506 8888-1111', 'E-01'),   -- factura 1
    ('juan@mail.com',  62000.00, '+506 8888-2222', 'E-02'),   -- factura 2
    ('maria@mail.com',  16490.00, '+506 8888-1111', 'E-01');  -- factura 3

INSERT INTO invoice_products (invoice_id, product_id, quantity, total) VALUES
    (1, 2, 1, 85000.00),
    (1, 1, 1, 12500.00),
    (2, 3, 1, 62000.00),
    (3, 1, 1, 12500.00),
    (3, 4, 1,  3990.00);

-- =====================================================
-- SELECTS
-- =====================================================

-- 1. Todos los productos
SELECT * FROM products;

-- 2. Productos con precio mayor a 50000
SELECT * FROM products WHERE price > 50000;

-- 3. Todas las compras de un mismo producto (por id)
SELECT ip.id, ip.invoice_id, ip.quantity, ip.total, i.purchase_date, i.buyer_email
FROM invoice_products ip
JOIN invoices i ON i.id = ip.invoice_id
WHERE ip.product_id = 1;

-- 4. Compras agrupadas por producto con el total comprado
SELECT p.id, p.name,
       SUM(ip.quantity) AS unidades_vendidas,
       SUM(ip.total)    AS monto_total
FROM invoice_products ip
JOIN products p ON p.id = ip.product_id
GROUP BY p.id, p.name;

-- 5. Todas las facturas de un mismo comprador
SELECT * FROM invoices WHERE buyer_email = 'maria@mail.com';

-- 6. Facturas ordenadas por monto total descendente
SELECT * FROM invoices ORDER BY total DESC;

-- 7. Una sola factura por numero de factura
SELECT * FROM invoices WHERE id = 1;