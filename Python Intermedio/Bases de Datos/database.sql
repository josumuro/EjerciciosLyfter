CREATE TABLE `Products`(
    `code` VARCHAR(50) NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `entry date` DATE NOT NULL,
    `Brand` VARCHAR(100) NOT NULL,
    `Stock Available` INT NOT NULL,
    PRIMARY KEY(`code`)
);
CREATE TABLE `Invoices`(
    `invoice_number` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `purchase date` DATETIME NOT NULL,
    `buyer email` VARCHAR(255) NOT NULL,
    `total amount` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `Products Per Invoice`(
    `quantity` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `total amountbigint` DECIMAL(10, 2) NOT NULL,
    `invoice_number` BIGINT NOT NULL,
    `product_code` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`invoice_number`)
);
ALTER TABLE
    `Products Per Invoice` ADD PRIMARY KEY(`product_code`);
CREATE TABLE `Shopping Cart`(
    `shopping cart id` BIGINT NOT NULL,
    `buyer email` VARCHAR(255) NOT NULL,
    PRIMARY KEY(`shopping cart id`)
);
ALTER TABLE
    `Shopping Cart` ADD INDEX `shopping cart_buyer email_index`(`buyer email`);
CREATE TABLE `Cart Items`(
    `buyer_email` VARCHAR(255) NOT NULL,
    `product_code` VARCHAR(50) NOT NULL,
    `quantity` INT NOT NULL,
    PRIMARY KEY(`buyer_email`)
);
ALTER TABLE
    `Cart Items` ADD PRIMARY KEY(`product_code`);
ALTER TABLE
    `Cart Items` ADD CONSTRAINT `cart items_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);
ALTER TABLE
    `Cart Items` ADD CONSTRAINT `cart items_buyer_email_foreign` FOREIGN KEY(`buyer_email`) REFERENCES `Shopping Cart`(`buyer email`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `Products`(`code`);
ALTER TABLE
    `Products Per Invoice` ADD CONSTRAINT `products per invoice_invoice_number_foreign` FOREIGN KEY(`invoice_number`) REFERENCES `Invoices`(`invoice_number`);