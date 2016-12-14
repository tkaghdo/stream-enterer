## 2. And operator ##

SELECT Major,ShareWomen,Employed FROM recent_grads 
WHERE ShareWomen>0.5 AND Employed>10000 limit 10;

## 3. Or operator ##

select major,Median,Unemployed
from recent_grads
where Median >= 10000 or Unemployed <= 1000 limit 20;

## 4. Grouping operators ##

select Major, Major_category, ShareWomen, Unemployment_rate
from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate < 0.051);

## 5. Practice grouping operators ##

select Major, Major_category, Employed, Unemployment_rate
from recent_grads
where Major_category in ('Business','Arts','Health') and (Employed > 20000 or Unemployment_rate  < 0.051);

## 6. Order by ##

select Major 
from recent_grads
order by Major  desc
limit 10;

## 7. Order using multiple columns ##

select Major_category, Median, Major
from recent_grads order by 3 asc, 2 asc limit 20