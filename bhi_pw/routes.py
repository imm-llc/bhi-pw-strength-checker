from bhi_pw import app

from flask import render_template, request
import json, requests, binascii

@app.route('/')
def root():
    return render_template("base.html")