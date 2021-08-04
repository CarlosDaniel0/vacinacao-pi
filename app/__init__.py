from flask import Flask, jsonify, render_template, request, redirect, session, flash, url_for
from flask_assets import Environment, Bundle
from os.path import dirname, realpath, join
from app.rnds import gen_map, data_processing

base_dir = dirname(realpath(__file__))

app = Flask(__name__, static_url_path='',
            static_folder=join(base_dir, 'public'),
            template_folder=join(base_dir, 'templates'))

# assets = Environment(app)
# assets.url = app.static_url_path
# scss = Bundle('assets/bulma/bulma.sass', filters='pyscss',output='assets/css/styles.css' )
# assets.register('scss_all', scss)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mapa-dados-vacinacao-pi')
def mapa():
    data_processing.execute(base_dir)
    gen_map.execute(base_dir)
    return render_template('show_map.html')

@app.route('/mapa-dados-vacinacao-pi/iframe')
def mapa_iframe():
    return render_template('map.html')

@app.route('/api/data')
def data_api():
    return jsonify(
        ''
    )

