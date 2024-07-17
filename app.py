## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for


# create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to Saurabh Sawant Channel"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to Index Page"

@app.route('/success/int:<score>')
def success(score):
    return "the person has passed and the score is :" + str(score)

@app.route('/fail/int:<score>')
def fail(score):
    return "the person has failed and the score is :" + str(score)

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)