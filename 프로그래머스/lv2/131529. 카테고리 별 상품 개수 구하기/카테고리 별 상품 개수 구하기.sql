-- 코드를 입력하세요
SELECT SUBSTR(PRODUCT_CODE, 1,2) as CATEGORY,
       Count(SUBSTR(PRODUCT_CODE, 1,2)) as PRODUCTS
  FROM PRODUCT
 GROUP BY SUBSTR(PRODUCT_CODE, 1,2)
 ORDER BY CATEGORY