from flask import Flask, render_template, request
import os, json
import os, json
from flask import jsonify
from BrandList import brands

app = Flask(__name__)


@app.route('/first')
def hello():
    return render_template('first.html')


@app.route('/second')
def secondLink():
    return render_template("second.html")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        search_name = request.form["search"]
        data = [["You have searched for ", search_name],
                ["Dolo", "Test"], ["Aspirin", "Best"], ["Vicks", "Own Brand"]]
        return render_template('home.html', data=data)
    else:
        return render_template('home.html', data=[])

@app.route('/search', methods=['POST'])
def search():
	term = request.form['q']
	print ('term: ', term)
	
	resp = brands.filterBrands(term)

	return resp