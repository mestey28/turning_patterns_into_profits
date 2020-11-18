-- Create

ALTER TABLE transactions
	ADD utid VARCHAR;
	
UPDATE transactions
SET utid = CASE
			WHEN prod_subcat_code > 10 THEN CONCAT(cust_id, '_', transaction_id, '_', '0', prod_cat_code, '_', prod_subcat_code)
			ELSE CONCAT(cust_id, '_', transaction_id, '_', '0', prod_cat_code, '_', '0', prod_subcat_code)
			END
	
SELECT * FROM transactions

ALTER TABLE transactions
ADD PRIMARY KEY (utid);

SELECT
CASE
	WHEN prod_subcat_code > 10 THEN CONCAT(cust_id, '_', transaction_id, '_', '0', prod_cat_code, '_', prod_subcat_code)
	ELSE CONCAT(cust_id, '_', transaction_id, '_', '0', prod_cat_code, '_', '0', prod_subcat_code)
END AS utid
FROM transactions;

	
	
