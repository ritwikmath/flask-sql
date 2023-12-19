# Flask MySQL Project

This project serves as a code example accompanying my blog on Clean Code. It is a Flask-based application designed to demonstrate clean and organized coding practices. The main functionality of the project is to establish a connection to MySQL databases using Flask. The project also includes setups for pytest, pylint, and JSON Web Token (JWT).

## Features

- Flask-based web application
- MySQL database connectivity
- Pytest for testing
- Pylint for code quality checking
- JSON Web Token (JWT) setup for authentication

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ritwikmath/flask-mysql.git
   cd flask-mysql

2. **Create User Table in Database:**
   ```sql
   CREATE TABLE users (
      user_id INT PRIMARY KEY AUTO_INCREMENT,
      username VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL,
      password VARCHAR(255) NOT NULL
   );
   INSERT INTO users (username, email, password) VALUES
   ('john_doe', 'john.doe@example.com', 'hashed_password_1'),
   ('jane_smith', 'jane.smith@example.com', 'hashed_password_2'),
   ('bob_jones', 'bob.jones@example.com', 'hashed_password_3');
   ```
3. **Create ENV file**
   Create a .env file in project root directory 
   ```text
   MYSQL_USER=root
   MYSQL_PASSWORD=secret
   MYSQL_HOST=host.docker.internal
   MYSQL_PORT=3306
   MYSQL_DB=test
   ENV=DEV
   ```

4. **Run as Docker Container:**
   Create Docker Image
   ```bash
      docker build -t flasksql .
   ```
   Windows:
   ```bash
   docker run --rm -p 5000:5000 -v ${PWD}:/usr/src/app --env-file .env flasksql
   ```
   Linux:
   ```bash
   docker run --rm -p 5000:5000 -v $(pwd):/usr/src/app --env-file .env flasksql
   ```
