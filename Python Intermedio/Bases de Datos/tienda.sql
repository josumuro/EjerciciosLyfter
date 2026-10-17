
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
