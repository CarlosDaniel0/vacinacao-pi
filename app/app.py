from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
from scraping.scraping import execute
from util.convert import to_json
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

sched = BackgroundScheduler(deamon=True)
# Definir intervalo ex: 'hours', 'minutes' ...
sched.add_job(execute, 'interval', hours=12)
sched.start()

app = Flask(__name__, static_url_path='',
            static_folder=os.path.join(base_dir, 'public'),
            template_folder=os.path.join(base_dir, 'templates'))


@app.route('/')
def index():
    return "<p>Hello, World</p>"


@app.route('/api/data')
def data_api():
    return jsonify(
        to_json(os.path.join(base_dir, 'public', 'data.csv'))
    )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
