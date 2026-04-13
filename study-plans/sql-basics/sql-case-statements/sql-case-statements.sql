-- Write your SQL query here
select
    username,
    session_count,
    case
        when session_count >= 50 then 'Power'
        when session_count >=10 then 'Casual'
        else 'Dormant'
    END as activity_level,
    case
        when platform in ('ios','android') then 'Mobile'
        when platform in ('web','desktop') then 'Desktop'
        else 'Other'
    END as platform_type,
    from user_sessions
    order by
    case 
        when activity_level = 'Power' then 1
        when activity_level = 'Casual' then 2
        else 3 end, 
    username asc