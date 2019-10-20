from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/results")
def tacos():
    return render_template('results.html')

@app.route("/", methods=['POST'])
def food():
    foodChoice = request.form['foodChoice']
    text = request.form.getlist('ingredients')
    # zipCode = request.form['zipCode']
    print(foodChoice)
    return render_template('index.html')
# @app.route("/about")
# def yo():
#     # return render_template('about.html', posts=posts, title='Title')

if __name__ == "__main__":
    app.run(debug=True)