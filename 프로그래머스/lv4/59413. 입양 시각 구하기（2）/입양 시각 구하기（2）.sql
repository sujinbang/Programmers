-- 코드를 입력하세요
-- SELECT TO_CHAR(DATETIME, 'HH24') AS HOUR, COUNT(DATETIME) AS COUNT
--   FROM ANIMAL_OUTS
--  GROUP BY TO_CHAR(DATETIME, 'HH24')
--  ORDER BY TO_CHAR(DATETIME, 'HH24')
 
 with tmp as (
    select level-1 as hour
      from dual
   connect by level < 25 
)

select a.hour
     , nvl(b.count, 0)
  from tmp a
  left outer join
     (
        select to_char(datetime, 'HH24')    as hour
             , count(*)                     as count
          from animal_outs
         group by to_char(datetime, 'HH24')
     ) b
    on a.hour = b.hour
 order by a.hour
;