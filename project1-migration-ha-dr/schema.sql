CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  department VARCHAR(50),
  salary INT
);

INSERT INTO employees (name, department, salary) VALUES
('Anil', 'IT', 50000),
('Ravi', 'HR', 40000),
('John', 'Finance', 60000);
