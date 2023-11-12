
IF NOT EXISTS (SELECT schema_id FROM sys.schemas WHERE name = 'ss')
    EXEC('CREATE SCHEMA ss;');
    
Drop table IF Exists ss.FACT_OrderDetails;
Drop table IF Exists ss.DIM_product;
Drop table IF Exists ss.DIM_customer;
Drop table IF Exists ss.DIM_order_shipper
Drop table IF Exists ss.DIM_product_category;
Drop table IF Exists ss.DIM_product_supplier;
Drop table IF Exists ss.DIM_order_employee;

Drop sequence IF Exists ss.order_Details_pk_sequence;

--Creating sequence for FACT_OrderDetails
CREATE SEQUENCE ss.order_Details_pk_sequence
    INCREMENT BY 1
    MINVALUE 1
    MAXVALUE 10000
    START WITH 1;

--Creating table FACT_OrderDetails
CREATE TABLE ss.FACT_OrderDetails (
    id BIGINT PRIMARY KEY DEFAULT NEXT VALUE FOR ss.order_Details_pk_sequence,
    OrderID int,
    price DECIMAL(10, 2),
    quantity int,
    Discount DECIMAL(4, 2),
    order_date DATE,
    product_Id int,
    customer_Id varchar(50),
    shipper_Id int,
    employee_Id int,
    supplier_Id int,
    category_Id int
   );

-- Creating table DIM_order_shipper
CREATE TABLE ss.DIM_order_shipper (
    shipper_Id int PRIMARY key,
    company_name VARCHAR(255)
);

-- Creating table DIM_product
CREATE TABLE ss.DIM_product (
    product_Id int PRIMARY key,
    product_name VARCHAR(255),
    quantity_per_unit VARCHAR(50),
    unit_price DECIMAL(10, 2)
);

-- Creating table DIM_product_category
CREATE TABLE ss.DIM_product_category (
    category_Id int PRIMARY key,
    category_name VARCHAR(50)
);

-- Creating table DIM_product_supplier
CREATE TABLE ss.DIM_product_supplier (
    supplier_Id int PRIMARY key,
    company_name VARCHAR(255),
    region VARCHAR(50),
    country VARCHAR(50),
    eff_start_date DATE,
    eff_end_date DATE
);

-- Creating table DIM_order_employee
CREATE TABLE ss.DIM_order_employee (
    employee_Id int PRIMARY key,
    employee_name VARCHAR(255),
    title VARCHAR(50),
    country VARCHAR(50)
);

-- Creating table DIM_customer
CREATE TABLE ss.DIM_customer (
    customer_Id Varchar(50) PRIMARY key,
    company_name VARCHAR(255),
    region VARCHAR(50),
    country VARCHAR(50)
);
