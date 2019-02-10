from flask import Flask, request, render_template

def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		return ("Welcome " username)
		# code that uses the data you've got
		# in our case, checking if the user exists
		# and logs them in, if not redirect to sign up
		
	else:
		# an exception
		pass

