-- DB 초기화 SQL 스크립트
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS flag;

CREATE TABLE users (
    username VARCHAR(32) PRIMARY KEY,
    password VARCHAR(64) NOT NULL
);

CREATE TABLE flag (
    username VARCHAR(32) PRIMARY KEY,
    value VARCHAR(128) NOT NULL
);

-- 더미 계정들 (로그인용)
INSERT INTO users (username, password) VALUES
('guest', 'guest'),
('hacker', '1337');