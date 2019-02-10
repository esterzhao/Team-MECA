from flask import Flask, render_template, request
app = Flask(__name__)

import data.py

@app.route("/home")
def home():
    return render_template("index.html")

 @app.route("/infomation")
def about():
    return render_template("info.html")

 @app.route("/aboutus")
def about():
    return render_template("about.html")

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)


