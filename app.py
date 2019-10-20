from flask import Flask, render_template, url_for, redirect, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def food():
    data = pd.read_csv("taco_burrito.csv")
    taco = request.form['foodChoice']
    ingredients = request.form.getlist('ingredients')
    exclude = request.form['allergies']
    zipcode = request.form['zipCode']

    is_taco = data['tacovburrito'] =='burrito'
    if(taco == 'tacos'):
        is_taco = data['tacovburrito']=='taco'
    taco_data = data[is_taco]

    contains = []
    for row in taco_data['menus.description']:
        row = str(row)
        contains.append(0)
        i = len(contains) -1
        for ingredient in ingredients:
            if row != 'nan' and ingredient in row:
                contains[i] -=1
        if exclude in row or exclude + 's' in row:
            contains[i] = 10
    taco_data['contains'] = pd.Series(contains, index=taco_data.index)
    taco_data.set_index("contains")
    ex = taco_data['contains'] <= 0
    fin_data = taco_data[ex]
    zipmatch = []
    for row in fin_data['postalCode']:
        if isinstance(row, str):
            row = float(row[0:5])
        dist = abs(float(zipcode) - row)
        zipmatch.append(dist)
        
    fin_data['zipmatch'] = pd.Series(zipmatch)

    mydata = fin_data.sort_values(by=['contains', 'zipmatch']).copy()
    topten = mydata.head(10)
    
    mydata = fin_data.sort_values(by=['contains', 'zipmatch']).copy()
    topten = mydata.head(10)
    posts = []
    for index, row in topten.iterrows():
        mydict = {'item':row['menus.name'],
                    'name':row['name'],
                    'address':row['address'],
                    'description':row['menus.description'],
                    'price':row['price.average']
                }
        posts.append(mydict)
    return render_template('results.html', posts=posts)
# @app.route("/about")
# def yo():
#     # return render_template('about.html', posts=posts, title='Title')

if __name__ == "__main__":
    app.run(debug=True)