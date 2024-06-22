-- 코드를 입력하세요
SELECT info.rest_id as rest_id, info.rest_name as rest_name, info.food_type as food_type, info.favorites as favorites, info.address as address, ROUND(AVG(review.review_score),2) as score
from 
    (select rest_id, rest_name, food_type, favorites, address
     from rest_info) as info
     join
     (select rest_id, review_score
      from rest_review) as review
     on info.rest_id = review.rest_id
group by rest_id
having address like "서울%"
order by score desc, favorites desc