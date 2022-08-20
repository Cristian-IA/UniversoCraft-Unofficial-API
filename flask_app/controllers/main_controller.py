from flask_app import app
from flask_app.models.scratch import Scratch
from flask import request, render_template, redirect, url_for, flash, jsonify

@app.route('/user/<string:name>', methods=['GET'])
def index(name):
    print(Scratch.get_user(name))
    return jsonify(Scratch.get_user(name))
