from flask import Flask,render_template,request,redirect,session, url_for

app = Flask(__name__) #static_url_path='/static') apres avoir ajouter la progressbar
app.secret_key = 'Borigo'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/SetName')
def SetName():
	return redirect(url_for('Starter')

@app.route('/Step1')
def Starter():
	return render_template("Step1.html")

@app.route('/Step2')
def Main():
	return render_template("Step2.html")

@app.route('/Step3')
def Cheese():
	return render_template("Step3.html")

@app.route('/Step4')
def Dessert():
	return render_template("Step4.html")

@app.route('/Bill')
def Bill():
	return render_template("Bill.html")
	

app.run(debug=True)