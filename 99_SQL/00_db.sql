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
-- rowid 컬럼을 포함ㅁ한 다른 모든 컬럼
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