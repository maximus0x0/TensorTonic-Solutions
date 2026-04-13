-- Write your SQL query here
with daily_table as (
select 
    order_date,
    count(*) as daily_count,
    sum(amount) as amount
from orders
group by order_date
)
select 
    avg(daily_count) as avg_daily_orders,
    avg(amount) as avg_daily_revenue,
    max(daily_count) as busiest_day_orders
from daily_table
    