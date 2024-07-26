from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


expenses = []

income = float(2660.00)







@app.route('/')
def home_page():


    
    return render_template('index.html', income=income)





@app.route('/add_expense', methods=["GET", "POST"])
def add_expense():
    return render_template("add_expense.html")


    



if __name__ == "__main__":
    app.run(debug=True)