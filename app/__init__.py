from flask import Flask, jsonify, render_template, request, redirect, session, flash, url_for
from os.path import dirname, realpath, join

from flask.templating import render_template_string
from app.rnds import gen_map, data_processing
import os

base_dir = dirname(realpath(__file__))

app = Flask(__name__, template_folder=join(base_dir, 'templates'))


@app.route('/')
def index():
    #data_processing.execute(base_dir)
    map = gen_map.execute(base_dir)
    return render_template_string(map)
    #render_template('map.html')