import os
from flask import Flask, jsonify, render_template, request
from datetime import datetime, timedelta
app = Flask(__name__)

import pyrise

# Log into the Highrise server
pyrise.Highrise.set_server('https://testingaccount1.highrisehq.com/')
pyrise.Highrise.auth('8d067f661c6611c3c3e40b245dd9de37')
 
# This is the list of tasks that should be attached to each person
task_template = []
task_template.append(['Send welcome email',1])
task_template.append(['Schedule phone call',7])
task_template.append(['First phone call',14])
task_template.append(['Convert to paid or end trial',40])
task_template.append(['Change tag to reflect new status',40])


# This is just for testing purposes, to make sure the app is running properly
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/add_to_highrise')
def add_hr():
	'''Receives a signup request from JSON, sends it to Highrise with attached signup tasks'''
	
	#Receive JSON data
	name = request.args.get('name')
	email = request.args.get('email')
	company = request.args.get('company')
	country = request.args.get('country')
	
	#Split name into first and last name. If there's no space, then we don't split
	splitter = name.find(" ")
	if splitter == -1:
		first_name = name
		last_name = ""
	else:
		first_name = name[:splitter]
		last_name = name[splitter+1:]
	
	#Create new person in Highrise
	p = pyrise.Person()
	p.first_name = first_name
	p.last_name = last_name		
	p.contact_data.email_addresses.append(pyrise.EmailAddress(address=email))
	
	p.save()
	
	p.add_note('Company name: ' + company + ", located in " + country)
	p.add_tag('Website signup')
	
	# Add tasks to the person
	for eachtask in task_template:
		
		t = pyrise.Task()
		t.body = eachtask[0]
		t.due_at = datetime.now() + timedelta(days=eachtask[1])
		t.subject_id = p.id	
		t.subject_type = 'Party'	
		t.save()
	
	return jsonify(result=first_name + " " + last_name + " " + country)


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)