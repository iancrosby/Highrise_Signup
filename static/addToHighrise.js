function addToHighrise(name, email, company, country) {

// All arguments are required, and must be strings. If you have no data to enter, just enter a blank string "".
// This function will add the data to Highrise as a new customer entry

// Change the URL below to where the JSON retriever is hosted
$.getJSON('http://sheltered-island-3519.herokuapp.com' + '/add_to_highrise', {
	name: name,
	email: email,
	company: company,
	country: country
	});

};


