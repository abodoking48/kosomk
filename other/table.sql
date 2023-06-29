CREATE TABLE users ( id INT PRIMARY KEY  , username TEXT NOT NULL , password_hash TEXT NOT NULL , birth DATE NOT NULL , phone TEXT NOT NULL , email TEXT);
CREATE TABLE HOUSES ( id INT PRIMARY KEY  , user_id INT NOT NULL , price NUMERIC  ,rooms NUMERIC  , space FLOAT , description TEXT , address TEXT NOT NULL ,phone_number TEXT NOT NULL, is_featured , for_rent BOOLEAN , FOREIGN KEY (user_id) REFERENCES users(id));
CREATE TABLE APARTMENT (id INT PRIMARY KEY ,user_id INT NOT NULL,price NUMERIC ,rooms INT,space FLOAT,description TEXT,address TEXT NOT NULL,phone_number TEXT NOT NULL,is_featured ,for_rent BOOLEAN,FOREIGN KEY(user_id) REFERENCES users(id));
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
photo_id INT NOT NULL,
path,
FOREIGN KEY (user_id) REFERENCES users(id)
);