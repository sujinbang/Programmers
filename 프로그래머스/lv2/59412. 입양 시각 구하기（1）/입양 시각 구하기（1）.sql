-- 코드를 입력하세요
SELECT SUBSTR(DATETIME,12,2) as HOUR,COUNT(SUBSTR(DATETIME,12,2)) as COUNT
  FROM ANIMAL_OUTS
 GROUP BY SUBSTR(DATETIME,12,2)
 HAVING HOUR >= 9
   AND HOUR < 20
 ORDER BY HOUR
 

