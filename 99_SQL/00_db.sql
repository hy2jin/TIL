-- tutoriaal db 생성
-- sqlite3 tutorial.sqlite3

-- table 확인
-- .tables

-- 현재 작업중인 database 저장 위치
-- .database

-- 현재 shell창 clear
-- .shell cls

-- .schema users


-- 모든 내용 조회
SELECT * FROM examples;

-- CREATE TABLE
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- .tables
-- .schemaa table_name

-- DROP TABLE
DROP TABLE classmates;

-- 실습
CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- data CREATE -> INSERT
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

-- 이름이 홍길동, 나이는 30, 주소는 서울
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES ('홍길동', 30, '서울');

-- 조회시, 필요한 column 같이 생성
-- rowid 컬럼을 포함한 다른 모든 컬럼
SELECT rowid, * FROM classmates;

-- id와 NOT NULL을 포함한 table 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 이름이 홍길동, 나이는 30, 주소는 서울
INSERT INTO classmates
(name, age, address)
VALUES ('홍길동', 30, '서울');

-- 컬럼은 전부 집어넣을거라면 생략 가능
INSERT INTO classmates VALUES ('김길동', 30, '부울경');
-- 단, id 컬럼이 정의되어 있으므로 직접 id를 넣어 줘야 함

-- NOT NULL만 포함한 테이블 생성
CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 여러개의 데이터 한번에 집어넣기
-- 홍길동 / 30 / 서울
-- 김길동 / 20 / 대전
-- 박길동 / 10 / 광주
-- 최길동 / 40 / 구미
-- 조길동 / 50 / 부울경
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김길동', 20, '대전'),
('박길동', 10, '광주'),
('최길동', 40, '구미'),
('조길동', 50, '부울경');

-- name, age 컬럼만 가지고 오기
SELECT name, age FROM classmates;

-- name, age 컬럼만 볼건데 3개만 조회
SELECT name, age FROM classmates
LIMIT 3;

-- name, age 컬럼만 볼건데 3번째의 값 하나 조회
SELECT name, age FROM classmates
LIMIT 1 OFFSET 2;

-- name, age 컬럼, 주소가 서울
SELECT name, age FROM classmates
WHERE address='서울';

-- 중복제거
SELECT DISTINCT age FROM classmates;

-- 5번 아이디 삭제
DELETE FROM classmates WHERE rowid=5;

INSERT INTO classmates VALUES ('김사피', 30, '부산');

-- 수정
-- 1번 데이터의 이름을 '박싸피', 나이를 100살
UPDATE classmates
SET name='박싸피', age=100
WHERE rowid=1;

-- WHERE
-- CREATE TABLE
CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

-- csv에 대응할 수 있도록 mode 적용
-- .mode csv

-- csv 파일 불러온다.
-- .import users.csv users

-- 데이터 전체 조회
SELECT * FROM users;

-- users 테이블에서 age가 30이상인 유저의 모든 컬럼 정보 조회
SELECT * FROM users WHERE age >= 30;

-- users 테이블에서 age가 30이상인 유저의 이름 조회
SELECT first_name FROM users WHERE age >= 30;

-- users 테이블에서
-- age가 30이상이고 성이 '김' 유저의 나이와 성 조회
SELECT age, last_name FROM users
WHERE age>=30 AND last_name='김';

-- age가 30이하이거나 성이 '김' 유저 조회
SELECT * FROM users
WHERE age<=30 OR last_name='김';

-- users 테이블의 레코드 총 개수
SELECT COUNT(*) FROM users;

-- 나이의 평균값
SELECT AVG(age) FROM users;

-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age>=30;

-- 계좌 작액(BALANCE)가 가장 높은 사람의 이름과 액수 조회
SELECT first_name, MAX(balance) FROM users;

-- 30살 이상의 평균 나이와 평균 계좌 잔액
SELECT AVG(age), AVG(balance) FROM users
WHERE age >= 30;

-- 30살 이하의 최소 계좌 잔액
SELECT MIN(balance) FROM users WHERE age<=30;

-- LIKE
-- 나이가 20대인 사람만 조회
SELECT * FROM users WHERE age LIKE '2_';

-- 지역번호가 02인 사람만 조회
SELECT * FROM users WHERE phone LIKE '02-%';

-- 이름이 '준'으로 끝나거나 '진'으로 끝나는 경우
SELECT first_name FROM users
WHERE first_name LIKE '%준'
OR first_name LIKE '%진';

-- 지역번호의 중간번호가 5114인 사람
SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- ORDER BY
-- 나이순으로 오름차순 정렬해서 상위 10개만 조회
SELECT * FROM users ORDER BY age ASC LIMIT 10;

-- 나이순, 성 순으로 오름차순 정렬해서 상위 10개만 조회
SELECT * FROM users ORDER BY age, last_name ASC
LIMIT 10;
SELECT * FROM users ORDER BY last_name, age ASC
LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬해서
-- 해당 유저의 성과 이름을 10개만 조회
SELECT last_name, first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;

-- ESCAPE
SELECT * FROM escapes
WHERE text LIKE '^%%안녕'
ESCAPE '^';
-- "%%안녕"


-- GROUP BY
-- 조회 하고자 하는 컬럼명 변경
SELECT last_name, COUNT(*) AS name_count FROM users
GROUP BY last_name;

SELECT country, COUNT(*) AS name_count FROM users
GROUP BY country;


-- 복습
-- title과 content라는 컬럼을 가진
-- articles라는 이름의 table 생성 (NOT NULL, rowid 이용)
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);
-- 1번제목, 1번내용 값 추가
INSERT INTO articles VALUES('1번제목', '1번내용');


-- ALTER TABLE
-- articles table news로 변경하기
ALTER TABLE articles RENAME TO news;

-- 새로운 컬럼 추가
ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL
DEFAULT 'now';

INSERT INTO news
VALUES ('제목', '내용', datetime('now'));

-- column명 수정
ALTER TABLE news RENAME COLUMN created_at
TO updated_at;