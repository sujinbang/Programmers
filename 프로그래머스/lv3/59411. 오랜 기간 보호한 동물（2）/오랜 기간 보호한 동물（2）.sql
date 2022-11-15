-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
  FROM (SELECT a.ANIMAL_ID, a.NAME,
               b.DATETIME - a.DATETIME as new
          FROM ANIMAL_INS a, ANIMAL_OUTS b
         WHERE a.ANIMAL_ID = b.ANIMAL_ID
         ORDER BY new DESC)
 WHERE ROWNUM < 3