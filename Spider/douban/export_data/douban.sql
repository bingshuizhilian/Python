﻿-- env: mysql8.0, navicat12.1
-- 增
-- INSERT INTO movie_top250(title, star, evaluation, quote, movieInfo) VALUES("测试1", "9.9", "32", "0", "")
-- INSERT INTO movie_top250(title, movieInfo, star, evaluation, quote) VALUES("测试2", "9.9", "32", "0", '')
-- 删
-- DELETE FROM `movie_top250` WHERE title = '测试2'
-- DELETE FROM `movie_top250` WHERE title LIKE '测试%'
-- 改
-- UPDATE `movie_top250` SET star = '3.6', quote = '引用测试' WHERE title = "测试2"
-- 查
-- SELECT * FROM `movie_top250` WHERE title LIKE '测试%'
SELECT * FROM `movie_top250` WHERE star >= 9.6 OR star <= 4