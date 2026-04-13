-- with avg_price as (
--     select avg(price) as avg_price
--     from products
-- )
-- select 
--     p.name,
--     p.price,
--     round(p.price - a.avg_price, 2) as vs_avg
-- from products p
-- join sales s on s.product_id = p.id
-- cross join avg_price a
-- group by p.id, p.name, p.price, a.avg_price
-- order by vs_avg desc, p.name asc;

select 
    p.name,
    p.price,
    round(p.price - (select avg(price) from products), 2) as vs_avg
from products p
join sales s on s.product_id = p.id
group by p.id, p.name, p.price
order by vs_avg desc, p.name asc;