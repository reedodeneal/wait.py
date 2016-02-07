#!/usr/bin/env/ python

from flask import Flask
from flask import jsonify
from flask import request
import time

app = Flask(__name__)

@app.route('/wait')
def wait():
  t = float(request.args.get('t'))
  time.sleep(t)
  return jsonify(time=t), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
  app.run()