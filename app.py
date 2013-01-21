import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

# import pyrise

''' pyrise.Highrise.set_server('https://testingaccount1.highrisehq.com/')
pyrise.Highrise.auth('8d067f661c6611c3c3e40b245dd9de37')
 
p = pyrise.Person()
p.first_name = 'My_first_test'
p.last_name = "Yippee"
p.contact_data.email_addresses.append(pyrise.EmailAddress(address="joe@schmoe.com"))
p.save()'''


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
	
	return render_template('index.html')
	#return jsonify(result=first_name + " " + last_name + " " + country)


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
	#app.run(host='0.0.0.0')