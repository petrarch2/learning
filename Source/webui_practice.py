#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'NERO'
__date__ = '2019/4/9'

from flask import Flask

app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

