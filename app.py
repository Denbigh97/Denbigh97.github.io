from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_cors import CORS
import csv
import os
from config import URI  
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)