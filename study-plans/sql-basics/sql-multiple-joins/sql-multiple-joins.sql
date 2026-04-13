-- Write your SQL query here
select
    u.username,
    exp.experiment_name,
    exp.variant,
    conv.revenue
    from users u
    inner join experiment_assignments exp on u.id = exp.user_id
    inner join conversions conv on u.id = conv.user_id
    order by exp.experiment_name asc,
            conv.revenue desc,
            u.username asc