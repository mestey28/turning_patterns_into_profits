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

# class customer(Base):
#     __tablename__ = 'customer' 

Base.prepare(engine, reflect=True)

session=Session(engine)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"To get the transactions by date: /transaction<br/>"
        f"To get a list of customers: /customer<br/>"
        f"To get the product category defs: /category<br/>"
        f"To get all data: /alldata<br/>"
    )
    
@app.route("/transaction")
def transaction():

    
    results = engine.execute('select * from `transaction`').fetchall()
    results_list=[{'id': result[0], 'transaction_id': result[1], 'cust_id': result[2], 'tran_date': result[3], 'pro_subcat_code': result[4], 
    'pro_cat_code': result[5], 'Qty': result[6], 'Rate': result[7], 'Tax': result[8], 'total_amt': result[9], 'Store_type': result[10]} for result in results]

    return jsonify(results_list)

@app.route("/customer")
def customer():

    
    results = engine.execute('select * from customer').fetchall()
    results_list=[{'id': result[0], 'customer_id': result[1], 'DOB': result[2], 'Gender': result[3], 'city_code': result[4]} for result in results]

    return jsonify(results_list)

@app.route("/category")
def category():

    results = engine.execute('select * from category').fetchall()
    results_list=[{'id': result[0], 'prod_cat_code': result[1], 'prod_cat': result[2], 'prod_sub_cat_code': result[3], 'prod_subcat': result[4]} for result in results]

    return jsonify(results_list)

@app.route("/alldata")
def alldata():

    results = engine.execute('select * from alldata').fetchall()
    results_list=[{'id': result[0], 'transaction_id': result[1], 'cust_id': result[2], 'DOB': result[12], 'Gender': result[13], 'city_code': result[14], 
    'tran_date': result[3], 'prod_cat_code': result[5], 'prod_cat': result[15], 'prod_subcat_code': result[4], 'prod_subcat': result[17], 
    'Qty': result[6], 'Rate': result[7], 'Tax': result[8], 'total_amt': result[9], 'Store_type': result[10]} for result in results]

    return jsonify(results_list)


if __name__ == "__main__":
    app.run(debug=True)