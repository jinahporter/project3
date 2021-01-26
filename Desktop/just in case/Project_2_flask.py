# Docs on session basics
# https://docs.sqlalchemy.org/en/13/orm/session_basics.html

import numpy as np
import os
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
app = Flask(__name__)

#################################################
# Jennifer Postgres
#################################################
pg_user = 'postgres'
db_name = 'Gamers'

connection_string = f"{pg_user}:Jennifer11@localhost:5432/{db_name}"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{connection_string}'
db = SQLAlchemy(app)
db.init_app(app)
engine = db.engine

#################################################
# Michael & Sadie's Postgres
#################################################
# pg_user = 'postgres'
# db_name = 'Gamers'

# connection_string = f"{pg_user}:bootcampDavid@1942@localhost:5432/{db_name}"
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{connection_string}'
# db = SQLAlchemy(app)
# db.init_app(app)
# engine = db.engine


# # Save reference to the table
# revenue = Base.classes.revenue
# console.log(revenue)


#################################################
# Flask Setup
#################################################


#################################################
# Flask Routes
#################################################


@app.route("/gamerChoice", methods=["POST"])
def gamerChoice():
    choice = request.form["id"]
    print(choice)
    gamerName = request.form["gamerName"]
    print(gamerName)
    genderOption = request.form["optionsRadios"]
    print(genderOption)

#     

@app.route("/age")
def age():
    """Return a list of all age names"""

    # Query all gamer data
    session = Session(engine)
    df = pd.read_sql_query("SELECT * FROM age", engine)
    all_names = df.to_dict(orient="list")

    # close the session to end the communication with the database
    session.close()

    return jsonify(all_names)


@app.route("/revenue")
def revenue():
    """Return a list of all age names"""

    # Query all gamer data
    session = Session(engine)
    df = pd.read_sql_query("SELECT * FROM revenue", engine)
    all_names = df.to_dict(orient="list")

    # close the session to end the communication with the database
    session.close()

    return jsonify(all_names)


@app.route("/map_")
def map_():
    """Return a list of all age names"""

    # Query all gamer data
    session = Session(engine)
    df = pd.read_sql_query("SELECT * FROM country_hours", engine)
    all_maphours = df.to_dict(orient="list")

    # close the session to end the communication with the database
    session.close()

    return jsonify(all_maphours)


@app.route('/')
def home():

    # Query all gamer data
    session = Session(engine)
    df = pd.read_sql_query("SELECT * FROM age", engine)
    all_names = df.to_dict(orient="list")

    # close the session to end the communication with the database
    session.close()

    # stuff goes here
    return render_template('index.html', all_names=all_names)


@app.route('/hours')
def hours():

    # Query all gamer data
    session = Session(engine)
    df = pd.read_sql_query("SELECT * FROM hours_average_country", engine)
    all_names = df.to_dict(orient="list")

    # close the session to end the communication with the database
    session.close()

    # stuff goes here
    return jsonify(all_names)


if __name__ == '__main__':
    app.run(debug=True)
