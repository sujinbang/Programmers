-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(PRICE*SALES_AMOUNT) as "SALES"
  FROM PRODUCT T1 INNER JOIN OFFLINE_SALE T2
    ON (T1.PRODUCT_ID = T2.PRODUCT_ID)
 GROUP BY PRODUCT_CODE
 ORDER BY SALES DESC, PRODUCT_CODE ASC