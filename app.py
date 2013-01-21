import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

import pyrise

pyrise.Highrise.set_server('https://testingaccount1.highrisehq.com/')
pyrise.Highrise.auth('8d067f661c6611c3c3e40b245dd9de37')
 



@app.route('/')
def index():
	return render_template('index.html')
    
@app.route('/add_to_highrise')
def add_hr():
	first_name = request.args.get('first_name')
	last_name = request.args.get('last_name')
	e_mail = request.args.get('e_mail')
	company = request.args.get('company')
	country = request.args.get('country')
	
	p = pyrise.Person()
	p.first_name = "first_name failed"
	p.last_name = "last_name failed"		
	p.contact_data.email_addresses.append(pyrise.EmailAddress(address="email@failed.cc"))
	
	if type(first_name) == str:
		p.first_name = first_name
	
	if type(last_name) == str:
		p.last_name = last_name
		
	if type(e_mail) == str:
		p.contact_data.email_addresses.append(pyrise.EmailAddress(address=e_mail))
	
	#if type(company) == str:
	#	p.company = company
	
	#if type(country) == str:
	#	p.country = country
	
	p.save()

	return jsonify(result=first_name + " " + last_name + " " + country)


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	#app.run(host='0.0.0.0')