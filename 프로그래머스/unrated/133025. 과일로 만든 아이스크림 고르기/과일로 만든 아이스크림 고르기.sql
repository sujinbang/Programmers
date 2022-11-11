-- 코드를 입력하세요
SELECT f.flavor
  FROM FIRST_HALF f inner join ICECREAM_INFO i
    ON (f.FLAVOR = i.FLAVOR
    AND TOTAL_ORDER > 3000
    AND INGREDIENT_TYPE = 'fruit_based')

 
  