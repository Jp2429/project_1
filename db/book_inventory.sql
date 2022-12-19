DROP TABLE IF EXISTS authorsBooks;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    genre VARCHAR(255)
);

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE authorsBooks(
    id SERIAL PRIMARY KEY,
    book_id INT NOT NULL REFERENCES books(id),
    author_id INT NOT NULL REFERENCES authors(id)
);



