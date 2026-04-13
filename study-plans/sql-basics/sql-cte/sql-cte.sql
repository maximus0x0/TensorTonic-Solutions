-- Write your SQL query here
select
    customer,
    order_count,
    total_spent
from(
select
    customer,
    sum(amount) as total_spent,
    count(*) as order_count
from orders
group by customer
) t
where order_count >1
order by total_spent desc , customer asc