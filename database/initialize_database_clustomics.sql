CREATE DATABASE clustomics;

USE clustomics;

CREATE TABLE user_info (
	username VARCHAR(15) PRIMARY KEY NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    pass VARCHAR(20) 
	);
    
CREATE TABLE groups (
	group_name VARCHAR(40) PRIMARY KEY NOT NULL UNIQUE,
    max_users_number INT DEFAULT 8
	);
    
CREATE TABLE member_group (
	username VARCHAR(15),
    group_name VARCHAR(40),
    admin BOOLEAN default false
	);
    
CREATE TABLE projects(
    id_project INT PRIMARY KEY AUTO_INCREMENT,
    group_name VARCHAR(40),
    user VARCHAR(15),
    project_name VARCHAR(50),
    file_path VARCHAR(45)
	);
    
CREATE TABLE project_result(
    id_project INT,	
    project_name VARCHAR(50),
    validation_result FLOAT,
    date_time CHAR(20),
    algo_rithm INT,
    groups INT, 
    distance VARCHAR(25),
    linkage VARCHAR(25),
    group_name VARCHAR(40),
    user VARCHAR(15),
    path VARCHAR(15)
	);
