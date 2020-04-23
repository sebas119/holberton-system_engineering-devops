/* Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost
and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.
Make sure that holberton_user has permission to check the primary/replica status of your databases. */

-- Task 1
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';


-- Task 2
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
 );

INSERT INTO nexus6 (name)
VALUES ('Leon');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Task 3 only web-01
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';


-- Task 4
-- Slave query
-- ufw allow mysql
CHANGE MASTER TO
MASTER_HOST='18.234.214.65',
MASTER_USER='replica_user',
MASTER_PASSWORD='root';


-- Tests

SELECT * FROM tyrell_corp.nexus6;
INSERT INTO tyrell_corp.nexus6 (name)
VALUES ('Test');



TRUNCATE TABLE tyrell_corp.nexus6;