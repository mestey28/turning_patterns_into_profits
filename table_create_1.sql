-- Create
CREATE TABLE transactions (
  	transaction_id FLOAT,
	cust_id FLOAT,
	tran_date DATE,
	prod_subcat_code VARCHAR,
	prod_cat_code VARCHAR,
	Qty INT,
	Rate FLOAT,
	Tax FLOAT,
	total_amt FLOAT,
	Store_type VARCHAR
);

SELECT * FROM transactions

-- Create
CREATE TABLE category (
  	prod_cat_code VARCHAR,
	prod_cat VARCHAR,
	prod_sub_cat_code VARCHAR,
	prod_subcat VARCHAR
);

SELECT * FROM category
