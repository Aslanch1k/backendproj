from flask import jsonify, request
from backendproj import app

@app.route("/categories")
def get_categories():
    pass

@app.route("/category", methods=['POST'])
def create_category():
    pass