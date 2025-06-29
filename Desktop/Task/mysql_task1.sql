use techm;
create table customers(
customer_id int primary key,
customer_name varchar(50),
region varchar(50));

create table orders(
order_id int primary key,
customer_id int,
order_date date,
total_amount decimal,
foreign key (customer_id) references customers(customer_id)
);

create table products(
product_id int primary key,
product_name varchar(50),
category varchar(50));

create table order_details(
detail_id int primary key,
order_id int,
product_id int,
quantity int,
unit_price decimal,
foreign key (order_id) references orders(order_id),
foreign key (product_id) references products(product_id)
);


insert into customers values(101,'Alice','East'),(102,'Bob','West'),(103,'Charlie','North'),(104,'Dave','South');
commit;
select * from customers;

insert into orders values(1,101,'2023-01-10',500.00),(2,102,'2023-02-15',300.00),(3,101,'2023-03-01',700.00),(4,103,'2023-04-20',450.00),(5,102,'2023-05-10',200.00);
commit;
select * from orders;

insert into products values(201,'Laptop','Electronics'),(202,'Mouse','Accssories'),(203,'Headphones','Accessories');
commit;
select * from products;

insert into order_details values (1,1,201,2,200.00),(2,1,202,1,100.00),(3,2,203,3,100.00),(4,3,201,1,700.00),(5,4,202,2,225.00);
commit;
select * from order_details;


-- Question 1: Find Customers Whose Total Order Amount Exceeds the Average Order Amount in Their Region
SELECT c.customer_name,
       c.region,
       SUM(o.total_amount) AS total_order_amount
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING SUM(o.total_amount) > AVG(o.total_amount);
    

-- Question 2: Find Orders Containing Products from All Categories
SELECT od.order_id,p.category
FROM order_details od
INNER JOIN products p
  ON od.product_id = p.product_id
GROUP BY od.order_id,p.category;


-- Question 3: Find the Most Expensive Product Ordered by Each Customer After a Specific Date
SELECT c.customer_name,
       p.product_name,
       od.unit_price,
       o.order_date
FROM customers c
INNER JOIN order_details od
  ON o.order_id = od.order_id
INNER JOIN products p
  ON od.product_id = p.product_id
WHERE o.order_date > '2023-02-01'
ORDER BY od.unit_price desc;

-- Question 4: Find Regions Where No Customer Ordered a Specific Product
SELECT region
FROM customers
WHERE customer_id NOT IN (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN products p
      ON od.product_id = p.product_id
    WHERE p.product_name = 'Laptop'
);
