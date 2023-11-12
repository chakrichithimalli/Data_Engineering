CREATE PROCEDURE ss.load_DIM_Tables
AS
BEGIN

insert into ss.FACT_OrderDetails(OrderID, customer_id, product_id, price, quantity, discount, employee_id, shipper_id, order_date, category_id, supplier_id )
select o.OrderID, ord.CustomerID, o.ProductID, o.UnitPrice, o.Quantity, o.Discount, ord.EmployeeID, ord.ShipVia, ord.OrderDate, pp.CategoryID, sp.SupplierID
from [Order Details] o inner join Orders ord on ord.OrderID = o.OrderID inner join dbo.Customers cus on cus.CustomerID = ord.CustomerID inner join 
dbo.Products pp on o.ProductID = pp.ProductID inner join dbo.Suppliers sp on pp.SupplierID = sp.SupplierID; 

insert into ss.DIM_product_category(category_Id, category_name) select CategoryID,CategoryName from dbo.Categories;
insert into ss.DIM_product_supplier(supplier_Id, company_name,region,country,eff_start_date,eff_end_date) select SupplierID,CompanyName,Region,Country, '2023-01-01', DATEADD(YEAR, 1, '2023-01-01') - 1 from dbo.Suppliers;
insert into ss.DIM_order_employee(employee_id,employee_name,title,country) select employeeID, CONCAT(FirstName,' ',LastName),Title,Country from dbo.Employees;
insert into ss.DIM_customer(customer_Id,company_name,region,country) select CustomerID,CompanyName,Region,Country from dbo.Customers; 
insert into ss.DIM_order_shipper(shipper_id,company_name) select ShipperID, CompanyName from dbo.Shippers;
insert into ss.DIM_product(product_Id,product_name,quantity_per_unit,unit_price) select ProductID,ProductName,QuantityPerUnit,UnitPrice from dbo.Products; 

END;
