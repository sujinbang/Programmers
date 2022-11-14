-- 코드를 입력하세요
SELECT Price as MAX_PRICE
  FROM (SELECT PRICE
      FROM PRODUCT
      ORDER BY Price desc)
WHERE ROWNUM = 1