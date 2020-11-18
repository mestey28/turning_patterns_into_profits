from flask import Flask

app = Flask(__name__)

import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import jsonify, render_template

engine = create_engine("sqlite:///test.db")

Base=automap_base()

Base.prepare(engine, reflect=True)

transaction = Base.classes.tran_df

session=Session(engine)

@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"To get the precipitation by date: /api/v1.0/precipitation<br/>"
        f"To get a list of stations: /api/v1.0/stations<br/>"
        f"To get the observed temperature for the last 12 mos: /api/v1.0/tobs<br/>"
        f"To get min, avg, and max temp for a given start date: /api/v1.0/yyyy-mm-dd<br/>"
        f"To get min, avg, and max temp for a given date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )
    
@app.route("/transaction")
def transactions():
    session=Session(engine)
    
    results = session.query(tran_df).all()
    # results_list=[{'idc': result[0], 'id': result[1], 'timestamp': result[2], 'lat': result[3], 'lon': result[4]} for result in results]
    session.close()

    return jsonify(results)


        


if __name__ == "__main__":
    app.run(debug=True)