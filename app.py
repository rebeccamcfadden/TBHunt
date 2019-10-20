from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/tacos")
def tacos():
    return render_template('food_template.html')

# @app.route("/about")
# def yo():
#     # return render_template('about.html', posts=posts, title='Title')

if __name__ == "__main__":
    app.run(debug=True)