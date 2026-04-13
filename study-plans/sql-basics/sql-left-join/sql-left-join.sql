-- Write your SQL query here
select cust.name, cust.city, 
    COALESCE(SUM(ord.amount),0) as total_spent
    from customers cust left join orders ord on cust.id = ord.customer_id
    group by cust.name, cust.city
    order by total_spent desc, name asc