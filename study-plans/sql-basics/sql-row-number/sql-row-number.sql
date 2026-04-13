-- Write your SQL query here
select 
    username,
    segment,
    engagement_score,
    ROW_NUMBER() OVER (PARTITION BY  segment order by engagement_score desc, username asc) as activity_rank
from user_activity
group by segment, username, engagement_score
order by segment asc, activity_rank asc