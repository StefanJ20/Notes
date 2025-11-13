// OPEN FILE AS CODE, NOT PREVIEW.

// This file represents my learning process towards MySQL, figuring out how to create
Databases and Tables within those databases, how to edit information pertaining to them 
and the users who edit it. This log was created using a tee command built into MySQL:

    tee ./log.txt 

mysql> CREATE DATABASE NewDatabase;
Query OK, 1 row affected (0.004 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| firstDatabase      |
| information_schema |
| mysql              |
| NewDatabase        |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.002 sec)

mysql> USE NewDatabase;
Database changed
mysql> DROP DATABASE firstDatabase;
Query OK, 1 row affected (0.011 sec)

mysql> CREATE TABLE subjects (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     username VARCHAR(50),
    ->     email VARCHAR(100),
    ->     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -> );
Query OK, 0 rows affected (0.012 sec)

mysql> SHOW TABLES;
+-----------------------+
| Tables_in_newdatabase |
+-----------------------+
| subjects              |
+-----------------------+
1 row in set (0.003 sec)

mysql> DESCRIBE subjects;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| username   | varchar(50)  | YES  |     | NULL              |                   |
| email      | varchar(100) | YES  |     | NULL              |                   |
| created_at | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
4 rows in set (0.004 sec)

mysql> DROP TABLE subjects;
Query OK, 0 rows affected (0.006 sec)

mysql> create table users (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     username VARCHAR(50),
    ->     email VARCHAR(50),
    ->     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.010 sec)

mysql> SHOW TABLES;
+-----------------------+
| Tables_in_newdatabase |
+-----------------------+
| users                 |
+-----------------------+
1 row in set (0.002 sec)

mysql> select * from users
    -> ;
Empty set (0.002 sec)

mysql> INSERT INTO users (username, email) VALUES ('Nutrition35', 'Nut@gmail.com');
Query OK, 1 row affected (0.002 sec)

mysql> select * from users;
+----+-------------+---------------+---------------------+
| id | username    | email         | created_at          |
+----+-------------+---------------+---------------------+
|  1 | Nutrition35 | Nut@gmail.com | 2025-06-26 20:25:45 |
+----+-------------+---------------+---------------------+
1 row in set (0.001 sec)

mysql> UPDATE users SET email = 'NoNuts@gmail.com' WHERE username = 'Nutrition35';
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from users;
+----+-------------+------------------+---------------------+
| id | username    | email            | created_at          |
+----+-------------+------------------+---------------------+
|  1 | Nutrition35 | NoNuts@gmail.com | 2025-06-26 20:25:45 |
+----+-------------+------------------+---------------------+
1 row in set (0.001 sec)

mysql> DELETE FROM users WHERE username = 'Nutrition35';
Query OK, 1 row affected (0.002 sec)

mysql> select * from users;
Empty set (0.001 sec)

mysql> INSERT INTO users (username, email) VALUES ('OneDude', 'firstDude@gmail.com')
    -> ;
Query OK, 1 row affected (0.002 sec)

mysql> INSERT INTO users (username, email) VALUES ('SecondDude', 'SecondDude@gmail.com');
Query OK, 1 row affected (0.002 sec)

mysql> select * from users;
+----+------------+----------------------+---------------------+
| id | username   | email                | created_at          |
+----+------------+----------------------+---------------------+
|  2 | OneDude    | firstDude@gmail.com  | 2025-06-26 20:28:40 |
|  3 | SecondDude | SecondDude@gmail.com | 2025-06-26 20:29:01 |
+----+------------+----------------------+---------------------+
2 rows in set (0.001 sec)

mysql> INSERT INTO users (username, email) VALUES ('SecondDude', 'SecondDude@hotmail.com');
Query OK, 1 row affected (0.002 sec)

mysql> select * from users;
+----+------------+------------------------+---------------------+
| id | username   | email                  | created_at          |
+----+------------+------------------------+---------------------+
|  2 | OneDude    | firstDude@gmail.com    | 2025-06-26 20:28:40 |
|  3 | SecondDude | SecondDude@gmail.com   | 2025-06-26 20:29:01 |
|  4 | SecondDude | SecondDude@hotmail.com | 2025-06-26 20:29:25 |
+----+------------+------------------------+---------------------+
3 rows in set (0.001 sec)

mysql> UPDATE users SET username = 'ThirdDude' WHERE email = 'SecondDude@hotmail.com';
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE users SET email = 'ThirdDude@hotmail.com' WHERE username = 'ThirdDude';
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from users;
+----+------------+-----------------------+---------------------+
| id | username   | email                 | created_at          |
+----+------------+-----------------------+---------------------+
|  2 | OneDude    | firstDude@gmail.com   | 2025-06-26 20:28:40 |
|  3 | SecondDude | SecondDude@gmail.com  | 2025-06-26 20:29:01 |
|  4 | ThirdDude  | ThirdDude@hotmail.com | 2025-06-26 20:29:25 |
+----+------------+-----------------------+---------------------+
3 rows in set (0.001 sec)

mysql> select * from users WHERE email LIKE '%hotmail.com';
+----+-----------+-----------------------+---------------------+
| id | username  | email                 | created_at          |
+----+-----------+-----------------------+---------------------+
|  4 | ThirdDude | ThirdDude@hotmail.com | 2025-06-26 20:29:25 |
+----+-----------+-----------------------+---------------------+
1 row in set (0.001 sec)

mysql> SELECT * FROM users ORDER BY created_at DESC;
+----+------------+-----------------------+---------------------+
| id | username   | email                 | created_at          |
+----+------------+-----------------------+---------------------+
|  4 | ThirdDude  | ThirdDude@hotmail.com | 2025-06-26 20:29:25 |
|  3 | SecondDude | SecondDude@gmail.com  | 2025-06-26 20:29:01 |
|  2 | OneDude    | firstDude@gmail.com   | 2025-06-26 20:28:40 |
+----+------------+-----------------------+---------------------+
3 rows in set (0.001 sec)

mysql> SELECT * FROm users LIMIT 1;
+----+----------+---------------------+---------------------+
| id | username | email               | created_at          |
+----+----------+---------------------+---------------------+
|  2 | OneDude  | firstDude@gmail.com | 2025-06-26 20:28:40 |
+----+----------+---------------------+---------------------+
1 row in set (0.001 sec)

mysql> CREATE USER 'worker'@'localhost' IDENTIFIED BY 'Password1!';
Query OK, 0 rows affected (0.006 sec)

mysql> GRANT ALL PRIVILEGES ON NewDatabase.* TO 'worker'@'localhost';
Query OK, 0 rows affected (0.003 sec)

mysql> SELECT user, host FROM mysql.user;
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| jojos            | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
| worker           | localhost |
+------------------+-----------+
6 rows in set (0.001 sec)

mysql> DROP USER 'worker'@'localhost';
Query OK, 0 rows affected (0.003 sec)

mysql> SELECT user, host FROM mysql.user;
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| jojos            | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
5 rows in set (0.001 sec)

mysql> SELECT DATABASE();
+-------------+
| DATABASE()  |
+-------------+
| newdatabase |
+-------------+
1 row in set (0.000 sec)

mysql> SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2025-06-26 20:35:48 |
+---------------------+
1 row in set (0.000 sec)

mysql> SELECT VERSION();
+-----------+
| VERSION() |
+-----------+
| 9.3.0     |
+-----------+
1 row in set (0.000 sec)

mysql> EXIT;

//The next segment will connect my Django hosted domain to an SQL cloud.

// To alter a databases properties, use the 'ALTER' method:

mysql> ALTER DATABASE FirstDatabase READ ONLY = 1;

// This line enables the read only property.
// The same can be done with tables:

mysql> ALTER TABLE users ADD phone_number VARCHAR(15);

//This allows you to add datatypes to the existing table.

// Inserting data into the database works similarly as creating the initial database values
// or a superuser, you specify the fields, and then fill them in. 

mysql> INSERT INTO users (username, email)  VALUES ("James", "crabman@gmail.com");
Query OK, 1 row affected (0.004 sec)

mysql> SELECT * FROM users;
+----+------------+-----------------------+---------------------+
| id | username   | email                 | created_at          |
+----+------------+-----------------------+---------------------+
|  2 | OneDude    | firstDude@gmail.com   | 2025-06-26 20:28:40 |
|  3 | SecondDude | SecondDude@gmail.com  | 2025-06-26 20:29:01 |
|  4 | ThirdDude  | ThirdDude@hotmail.com | 2025-06-26 20:29:25 |
|  5 | James      | crabman@gmail.com     | 2025-06-27 14:21:08 |
+----+------------+-----------------------+---------------------+
4 rows in set (0.001 sec)

// We can change values within the columns if we specify which value we want 
// to change as well as the updating value we want to use.

mysql> UPDATE users SET email = "james@gmail.com" WHERE username = "James";
Query OK, 1 row affected (0.004 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM users;
+----+------------+-----------------------+---------------------+
| id | username   | email                 | created_at          |
+----+------------+-----------------------+---------------------+
|  2 | OneDude    | firstDude@gmail.com   | 2025-06-26 20:28:40 |
|  3 | SecondDude | SecondDude@gmail.com  | 2025-06-26 20:29:01 |
|  4 | ThirdDude  | ThirdDude@hotmail.com | 2025-06-26 20:29:25 |
|  5 | James      | james@gmail.com       | 2025-06-27 14:21:08 |
+----+------------+-----------------------+---------------------+
4 rows in set (0.001 sec)

// Here, Im updating the users with a new email where that username exists.
// I'm using existing data to identify where to make changes.

// In MySQL, if you want to turn off AUTOCOMMIT for changes in your database,
// you can do 'SET AUTOCOMMIT = OFF' and then 'COMMIT' when you want changes.
// If you dont want to commit those changes, you can do 'ROLLBACK' to rollback 
// to the initual autocommit state. This is a fault-proof method for returning 
// back to a save state when you make a human/machine error.

// To make data entries unique in MySQL, just add 'UNIQUE' tag to the variable.

    CREATE TABLE products (

            product_id INT,
            product_name VARCHAR(25) UNIQUE,
            price DECIMAL(4, 2)
        );

// To add a constraint to it after the table is created:

    ALTER TABLE products ADD CONSTRAINT UNIQUE(product_name);

// To make a value always not initially null:

    CREATE TABLE products (
        product_id INT,
        product_name VARCHAR(25),
        price DECIMAL (4, 2) NOT NULL
    );

// Alter value:

ALTER TABLE products MODIFY price DECIMAL(4,2) NOT NULL;

// Constraints are used in order to limit what values can be places in a column,
// therefore the columns must either always have a value or not if constrained.

// CHECKS

    CREATE TABLE employees (

        employee_id INT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        hourly_pay DECIMAL(5, 2),
        hire_date DATE,
        CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10.00)

        ); 

// You could optionally add the Constraint:

    ALTER TABLE employees ADD CONSTRAINT chk_hourly_pay CHECK (hourly_pay >= 10.00);

// You can drop the check:
    
    ALTER TABLE employees DROP CHECK chk_hourly_pay;

// This way, whenever creating a new item in the table, it will check constraints first
// before applying your code to the tables. If the constraint isn't met, the item won't
// be added to the table. If you don't like the constraint, you can drop it. 

// Default Constraint: A default value will be set on an item on a table if not specified.

// Base way:

    INSERT INTO products VALUES (104, "straw", 0.00),
                                (105, "napkin", 0.00),
                                (106, "fork", 0.00),
                                (107, "spoon", 0.00);

    SELECT * FROM products      

// Default constraints:

    CREATE TABLE products (

        product_id INT,
        product_name VARCHAR(25),
        price DECIMAL(4, 2) DEFAULT 0.00

        );      

    ALTER TABLE products ALTER price SET DEFAULT 0.00;

    SELECT * FROM products;

// When only implicating specific things in the table, you need to make sure you
// specify within the insert what items you're adding

    INSERT INTO (product_id, product_name) VALUES (), (), (), ();

    SELECT * FROM products;

// In order to reference objects from other tables, we'll need a 'FOREIGN KEY' cosntraint
// so for example:

    CREATE TABLE transactions (

        transaction_id INT PRIMARY KEY AUTO_INCREMENT,
        amount DECIMAL(5,2),
        customer_id INT,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)

        );

// To apply the foreign key to an existing table, do this:

    ALTER TABLE transactions ADD CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES customers(customer_id);

    DELETE FROM customers WHERE customer_id = 3;

// In MySQL, a lot of the time you'll want to gather related data in different tables, in order to accurately store information 
// with its coincided values, and doing that we can use 'INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN'.

mysql> SELECT * FROM transactions INNER JOIN customers ON transactions.customer_id = customers.id;
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
| transaction_id | customer_id | amount | Transacted_at       | id | name         | email                   | created_at          |
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
|           1000 |           1 |   4.99 | 2025-07-04 15:26:53 |  1 | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|           1001 |           2 |   8.99 | 2025-07-04 15:26:53 |  2 | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|           1002 |           3 |   1.99 | 2025-07-04 15:26:53 |  3 | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|           1003 |           4 |  99.25 | 2025-07-04 15:26:53 |  4 | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
4 rows in set (0.001 sec)

mysql> SELECT transaction_id, amount, name, email  FROM transactions INNER JOIN customers ON transactions.customer_id = customers.id;
+----------------+--------+--------------+-------------------------+
| transaction_id | amount | name         | email                   |
+----------------+--------+--------------+-------------------------+
|           1000 |   4.99 | James        | squidward@gmail.com     |
|           1001 |   8.99 | Gomez        | HankSchrader@gmail.com  |
|           1002 |   1.99 | Petite Frank | HolyFuckLouis@yahoo.com |
|           1003 |  99.25 | John         | PorkedIt@hotmail.org    |
+----------------+--------+--------------+-------------------------+
4 rows in set (0.000 sec)

mysql> SELECT * FROM transactions LEFT JOIN customers ON transactions.customer_id = customers.id;
+----------------+-------------+--------+---------------------+------+--------------+-------------------------+---------------------+
| transaction_id | customer_id | amount | Transacted_at       | id   | name         | email                   | created_at          |
+----------------+-------------+--------+---------------------+------+--------------+-------------------------+---------------------+
|           1000 |           1 |   4.99 | 2025-07-04 15:26:53 |    1 | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|           1001 |           2 |   8.99 | 2025-07-04 15:26:53 |    2 | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|           1002 |           3 |   1.99 | 2025-07-04 15:26:53 |    3 | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|           1003 |           4 |  99.25 | 2025-07-04 15:26:53 |    4 | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
|           1004 |        NULL |   2.99 | 2025-07-04 15:45:25 | NULL | NULL         | NULL                    | NULL                |
+----------------+-------------+--------+---------------------+------+--------------+-------------------------+---------------------+
5 rows in set (0.000 sec)

mysql> SELECT * FROM transactions RIGHT JOIN customers ON transactions.customer_id = customers.id;
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
| transaction_id | customer_id | amount | Transacted_at       | id | name         | email                   | created_at          |
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
|           1000 |           1 |   4.99 | 2025-07-04 15:26:53 |  1 | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|           1001 |           2 |   8.99 | 2025-07-04 15:26:53 |  2 | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|           1002 |           3 |   1.99 | 2025-07-04 15:26:53 |  3 | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|           1003 |           4 |  99.25 | 2025-07-04 15:26:53 |  4 | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
+----------------+-------------+--------+---------------------+----+--------------+-------------------------+---------------------+
4 rows in set (0.000 sec)

// This way, information is validly sorted how we desire, and the tables are joined. 

// MySQL has a variety of performative functions that are documented in documentation, and can be executed to show you different databits of 
// information in a MySQL schema.

mysql> SELECT COUNT(amount) FROM transactions;
+---------------+
| COUNT(amount) |
+---------------+
|             5 |
+---------------+
1 row in set (0.000 sec)

mysql> SELECT COUNT(amount) AS "Transactions:" FROM transactions;
+---------------+
| Transactions: |
+---------------+
|             5 |
+---------------+
1 row in set (0.000 sec)

mysql> SELECT MAX(amount) AS maximum FROM transactions;
+---------+
| maximum |
+---------+
|   99.25 |
+---------+
1 row in set (0.002 sec)

mysql> SELECT MIN(amount) AS minimum FROM transactions;
+---------+
| minimum |
+---------+
|    1.99 |
+---------+
1 row in set (0.000 sec)

mysql> SELECT AVG(amount) AS average FROM transactions;
+-----------+
| average   |
+-----------+
| 23.642000 |
+-----------+
1 row in set (0.000 sec)

mysql> SELECT SUM(amount) AS sum FROM transactions;
+--------+
| sum    |
+--------+
| 118.21 |
+--------+
1 row in set (0.000 sec)

// You can request Data to be presented in a readable fashion with introduction of "writable space"
// and Functions.

mysql> SELECT CONCAT(name, " - ",  email) AS 'Name and Email: ' FROM customers;
+----------------------------------------+
| Name and Email:                        |
+----------------------------------------+
| James - squidward@gmail.com            |
| Gomez - HankSchrader@gmail.com         |
| Petite Frank - HolyFuckLouis@yahoo.com |
| John - PorkedIt@hotmail.org            |
+----------------------------------------+
4 rows in set (0.000 sec)

mysql> ALTER TABLE customers ADD COLUMN membership VARCHAR(20) AFTER id;
Query OK, 0 rows affected (0.009 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> UPDATE customers SET membership = "Premium" WHERE id = 1;
Query OK, 1 row affected (0.001 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM customers;
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  1 | Premium    | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|  2 | NULL       | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  3 | NULL       | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|  4 | NULL       | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
+----+------------+--------------+-------------------------+---------------------+
4 rows in set (0.000 sec)

mysql> UPDATE customers SET membership = "Standard" WHERE id = 2;
Query OK, 1 row affected (0.002 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE customers SET membership = "Standard" WHERE id = 3;
Query OK, 1 row affected (0.001 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE customers SET membership = "VIP" WHERE id = 4;
Query OK, 1 row affected (0.001 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM customers WHERE created_at < "2025-07-04";
Empty set (0.000 sec)

mysql> SELECT * FROM customers WHERE created_at > "2025-07-04";
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  1 | Premium    | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|  4 | VIP        | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
+----+------------+--------------+-------------------------+---------------------+
4 rows in set (0.000 sec)

mysql> SELECT * FROM customers WHERE created_at > "2025-07-04" AND membership = "Standard";
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
+----+------------+--------------+-------------------------+---------------------+
2 rows in set (0.000 sec)

mysql> SELECT * FROM customers WHERE membership = "Standard" AND id >= 2;
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
+----+------------+--------------+-------------------------+---------------------+
2 rows in set (0.000 sec)

mysql> SELECT * FROM customers WHERE membership = "Standard" OR id >= 2;
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|  4 | VIP        | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
+----+------------+--------------+-------------------------+---------------------+
3 rows in set (0.000 sec)

mysql> SELECT * FROM customers WHERE NOT membership = "Standard";
+----+------------+-------+----------------------+---------------------+
| id | membership | name  | email                | created_at          |
+----+------------+-------+----------------------+---------------------+
|  1 | Premium    | James | squidward@gmail.com  | 2025-07-04 15:06:10 |
|  4 | VIP        | John  | PorkedIt@hotmail.org | 2025-07-04 15:07:14 |
+----+------------+-------+----------------------+---------------------+
2 rows in set (0.001 sec)

mysql> SELECT * FROM customers WHERE NOT membership = "Standard" AND NOT name = "James";
+----+------------+------+----------------------+---------------------+
| id | membership | name | email                | created_at          |
+----+------------+------+----------------------+---------------------+
|  4 | VIP        | John | PorkedIt@hotmail.org | 2025-07-04 15:07:14 |
+----+------------+------+----------------------+---------------------+
1 row in set (0.000 sec)

mysql> SELECT * FROM customers WHERE membership IN ("VIP", "Premium");
+----+------------+-------+----------------------+---------------------+
| id | membership | name  | email                | created_at          |
+----+------------+-------+----------------------+---------------------+
|  1 | Premium    | James | squidward@gmail.com  | 2025-07-04 15:06:10 |
|  4 | VIP        | John  | PorkedIt@hotmail.org | 2025-07-04 15:07:14 |
+----+------------+-------+----------------------+---------------------+
2 rows in set (0.000 sec)

// There are many methods in selecting the data which you wish to view.

// You can select specific things with wild card characters like "%" and "_" In MySQL
// The "%" character attempts to search for queries with whatever prefixes or suffixes it.
// The "_" character attempts to fill in the blank of the query you're searching for.

mysql> SELECT * FROM customers WHERE name LIKE "J%";
+----+------------+-------+----------------------+---------------------+
| id | membership | name  | email                | created_at          |
+----+------------+-------+----------------------+---------------------+
|  1 | Premium    | James | squidward@gmail.com  | 2025-07-04 15:06:10 |
|  4 | VIP        | John  | PorkedIt@hotmail.org | 2025-07-04 15:07:14 |
+----+------------+-------+----------------------+---------------------+
2 rows in set (0.002 sec)

mysql> SELECT * FROM customers WHERE email LIKE "%.org";
+----+------------+----------+----------------------+---------------------+
| id | membership | name     | email                | created_at          |
+----+------------+----------+----------------------+---------------------+
|  4 | VIP        | John     | PorkedIt@hotmail.org | 2025-07-04 15:07:14 |
|  5 | Premium    | Han Solo | ElfMan@hotmail.org   | 2025-07-06 18:44:44 |
+----+------------+----------+----------------------+---------------------+
2 rows in set (0.000 sec)

mysql> SELECT * FROM customers WHERE membership LIKE "____ium";
+----+------------+----------+---------------------+---------------------+
| id | membership | name     | email               | created_at          |
+----+------------+----------+---------------------+---------------------+
|  1 | Premium    | James    | squidward@gmail.com | 2025-07-04 15:06:10 |
|  5 | Premium    | Han Solo | ElfMan@hotmail.org  | 2025-07-06 18:44:44 |
+----+------------+----------+---------------------+---------------------+
2 rows in set (0.000 sec)

// In MySQL, you can use the 'ORDER BY' clause to order a specific column alphabetically or numerically.

mysql> SELECT * FROM customers ORDER BY name;
ERROR 4031 (HY000): The client was disconnected by the server because of inactivity. See wait_timeout and interactive_timeout for configuring this behavior.
No connection. Trying to reconnect...
Connection id:    117
Current database: learningdatabase

+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  5 | Premium    | Han Solo     | ElfMan@hotmail.org      | 2025-07-06 18:44:44 |
|  1 | Premium    | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|  4 | VIP        | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
+----+------------+--------------+-------------------------+---------------------+
5 rows in set (0.019 sec)

mysql> SELECT * FROM customers ORDER BY name DESC;
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
|  4 | VIP        | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
|  1 | Premium    | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|  5 | Premium    | Han Solo     | ElfMan@hotmail.org      | 2025-07-06 18:44:44 |
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
+----+------------+--------------+-------------------------+---------------------+
5 rows in set (0.000 sec)

mysql> SELECT * FROM customers ORDER BY name ASC;
+----+------------+--------------+-------------------------+---------------------+
| id | membership | name         | email                   | created_at          |
+----+------------+--------------+-------------------------+---------------------+
|  2 | Standard   | Gomez        | HankSchrader@gmail.com  | 2025-07-04 15:06:27 |
|  5 | Premium    | Han Solo     | ElfMan@hotmail.org      | 2025-07-06 18:44:44 |
|  1 | Premium    | James        | squidward@gmail.com     | 2025-07-04 15:06:10 |
|  4 | VIP        | John         | PorkedIt@hotmail.org    | 2025-07-04 15:07:14 |
|  3 | Standard   | Petite Frank | HolyFuckLouis@yahoo.com | 2025-07-04 15:06:51 |
+----+------------+--------------+-------------------------+---------------------+
5 rows in set (0.001 sec)

mysql> SELECT * FROM transactions ORDER BY amount;
+----------------+-------------+--------+---------------------+
| transaction_id | customer_id | amount | Transacted_at       |
+----------------+-------------+--------+---------------------+
|           1002 |           3 |   1.99 | 2025-07-04 15:26:53 |
|           1004 |        NULL |   2.99 | 2025-07-04 15:45:25 |
|           1000 |           1 |   4.99 | 2025-07-04 15:26:53 |
|           1001 |           2 |   8.99 | 2025-07-04 15:26:53 |
|           1003 |           4 |  99.25 | 2025-07-04 15:26:53 |
+----------------+-------------+--------+---------------------+
5 rows in set (0.001 sec)

mysql> SELECT * FROM transactions ORDER BY amount, customer_id;
+----------------+-------------+--------+---------------------+
| transaction_id | customer_id | amount | Transacted_at       |
+----------------+-------------+--------+---------------------+
|           1002 |           3 |   1.99 | 2025-07-04 15:26:53 |
|           1004 |        NULL |   2.99 | 2025-07-04 15:45:25 |
|           1000 |           1 |   4.99 | 2025-07-04 15:26:53 |
|           1001 |           2 |   8.99 | 2025-07-04 15:26:53 |
|           1003 |           4 |  99.25 | 2025-07-04 15:26:53 |
+----------------+-------------+--------+---------------------+
5 rows in set (0.000 sec)



