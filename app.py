import os
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

import pyrise

pyrise.Highrise.set_server('https://testingaccount1.highrisehq.com/')
pyrise.Highrise.auth('8d067f661c6611c3c3e40b245dd9de37')

@app.route('/')
def index():
    p = pyrise.Person()
    p.first_name = 'My_first_test'
    p.last_name = "Yippee"
    p.contact_data.email_addresses.append(pyrise.EmailAddress(address="joe@schmoe.com"))
    p.save()
    return null



if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)