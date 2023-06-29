CREATE TABLE users ( id INT PRIMARY KEY  , username TEXT NOT NULL , password_hash TEXT NOT NULL , birth DATE , phone TEXT , email TEXT);
CREATE TABLE HOUSES ( id INT PRIMARY KEY  , user_id INT NOT NULL , price NUMERIC  ,rooms NUMERIC  , space FLOAT , description TEXT , address TEXT NOT NULL ,phone_number TEXT NOT NULL, for_rent BOOLEAN , featured BOOLEAN not null default false, FOREIGN KEY (user_id) REFERENCES users(id));
CREATE TABLE LAND (id INT PRIMARY KEY ,
user_id INT NOT NULL,
price NUMERIC ,
space FLOAT,
description TEXT,
address TEXT NOT NULL,
phone_number TEXT NOT NULL,
is_featured ,
FOREIGN KEY(user_id) REFERENCES users(id));
CREATE TABLE HISTORY (
    id INT PRIMARY KEY ,
    user_id INT not null,
    comment TEXT,
    favorite_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE PHOTO (id INT PRIMARY KEY ,
user_id INT NOT NULL,
HOUSES_id INT ,
APARTMENT_id INT,
LAND_id INT,
path,
FOREIGN KEY (user_id) REFERENCES users(id)
);
