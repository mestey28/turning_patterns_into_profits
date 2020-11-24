from flask import Flask

app = Flask(__name__)

import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import jsonify, render_template

engine = create_engine("sqlite:///test1.db")

Base=automap_base()

Base.prepare(engine, reflect=True)

session=Session(engine)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"To get the transactions by date: https://retail-sales-data.herokuapp.com/transaction<br/>"
        f"To get a list of customers: https://retail-sales-data.herokuapp.com/customer<br/>"
        f"To get the product category defs: https://retail-sales-data.herokuapp.com/category<br/>"
        f"To get all data: https://retail-sales-data.herokuapp.com/alldata<br/>"
    )
    
@app.route("/transaction")
def transaction():

    
    results = engine.execute('select * from `transaction`').fetchall()
    results_list=[{'id': result[0], 'transaction_id': result[1], 'cust_id': result[2], 'tran_date': result[3], 'pro_subcat_code': result[4], 
    'pro_cat_code': result[5], 'Qty': result[6], 'Rate': result[7], 'Tax': result[8], 'total_amt': result[9], 'Store_type': result[10], 'Item': result[11], 'Sale/Return': result[12]} for result in results]

    return jsonify(results_list)

@app.route("/customer")
def customer():

    
    results = engine.execute('select * from customer').fetchall()
    results_list=[{'id': result[0], 'customer_id': result[1], 'DOB': result[2], 'Gender': result[3], 'city_code': result[4], 'city': result[5], 'state': result[6], 'zip': result[7], 'age': result[8]} for result in results]

    return jsonify(results_list)

@app.route("/category")
def category():

    results = engine.execute('select * from category').fetchall()
    results_list=[{'id': result[0], 'prod_cat_code': result[1], 'prod_cat': result[2], 'prod_sub_cat_code': result[3], 'prod_subcat': result[4]} for result in results]

    return jsonify(results_list)

@app.route("/alldata")
def alldata():

    results = engine.execute('select * from alldata').fetchall()
    results_list=[{'id': result[0], 'transaction_id': result[1], 'cust_id': result[2], 'DOB': result[14], 'Gender': result[15], 'city_code': result[16], 'city': result[17], 
    'state': result[18], 'zip': result[19],'tran_date': result[3], 'prod_cat_code': result[5], 'prod_cat': result[21], 'prod_subcat_code': result[4], 'prod_subcat': result[23], 
    'Qty': result[6], 'Rate': result[7], 'Tax': result[8], 'total_amt': result[9], 'Store_type': result[10], 'Item': result[11], 'Sale/Return': result[12]} for result in results]

    return jsonify(results_list)


if __name__ == "__main__":
    app.run(debug=True)