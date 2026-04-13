-- Write your SQL query here
-- select u.username, COALESCE(referred.username,'organic') as referrer_name
-- from user_referrals u left join user_referrals referred on u.referred_by = referred.id

SELECT 
    u.username,
    COALESCE(r.username, 'organic') AS referrer_name
FROM user_referrals u
LEFT JOIN user_referrals r
    ON u.referred_by = r.id
ORDER BY u.username ASC;