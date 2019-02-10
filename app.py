from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
        age = request.form['age']
	race = request.form['race']
        ethnicity = request.form['ethnicity']
        zipCode = request.form['zipCode']
        dueDate = request.form['dueDate']
   print(age, race, ethnicity, zipCode, dueDate)
