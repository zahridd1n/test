CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    tel VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL
);


CREATE TABLE category(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL);

CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    file VARCHAR(255) NOT NULL,
    price REAL NOT NULL DEFAULT 0,
    quantity INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE cart(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    is_active BOOLEAN DEFAULT true);

CREATE TABLE cart_product(
    id SERIAL PRIMARY KEY,
    cart_id INTEGER NOT NULL REFERENCES cart_id(id),
    product_id INTEGER  NOT NULL REFERENCES product(id),
    quantity INTEGER NOT NULL
);