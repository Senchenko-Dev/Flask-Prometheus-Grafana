#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, Response
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


counter = 0

@app.route('/owner')
def hello_world():
    return 'Сенченко Никита Тестовое'


@app.route('/')
def visit():
    global counter
    counter = counter + 1
    result = "Visit number %d\n" % counter
    return Response(result,mimetype='text/plain')


@app.route('/metrics')
def metrics():
    global counter
    result = "# TYPE hello_world_counter counter\nhello_world_counter %d\n" % counter
    return Response(result, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)
