# turning_patterns_into_profits

Using Python, I applied different machine learning methods to analyze retail sales.

-Apriori Algorithm: To determine which products were often purchased together.  This information can then be used for product placement or a promotional sale that offers a  
                    discount if both items are purchased at the same time.  One challenge of this particular dataset was that each transaction involved the purchase of only one
                    item type.  To overcome this, I used the algorithm to determine which items were purchased by the same customer, even if at different times.
                    
-Linear Regression: Used to forecast sales for the upcoming year.  The forecasts are broken down by product category and then even further to product subcategory.  This is useful
                    to determine:
                                  how much of each product to stock next year
                                  which items are big sellers
                                  which items have seen a decrease in sales
                                  should we run a promotion for the decreased items or replace them
                                  
-Simple categorization of customers:  Break down sales and profits by customer type.  This particular dataset provided each customer's age, gender, and location.  By pulling apart 
                                      each category, it became apparent that the company needs to market more towards customers born in the 1990's and to increase advertising in
                                      the city code 0 (no name was given for the city codes).
