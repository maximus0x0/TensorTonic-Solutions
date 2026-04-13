-- Write your SQL query here
select 
    name,
    (case when email IS NOT NULL then email else 'N/A' end) as display_email,
    (case when deactivated_at IS NULL then 'active' else 'inactive' end) as status
    from customers
    WHERE phone IS NOT NULL
order by name asc