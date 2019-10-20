from flask import Flask, render_template, url_for, redirect, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    newdict = {'radish': 100, 'tofu': 116, 'zucchini': 116, 'tuna': 123, 'scallion': 142, 'cod': 175, 'carrot': 180, 'poblano': 182, 'mayo': 194, 'honey': 195, 'cucumber': 208, 'tilapia': 226, 'spinach': 274, 'pineapple': 294, 'hash': 297, 'mahi': 342, 'mushroom': 363, 'queso': 372, 'chorizo': 395, 'ham': 401, 'tomatillo': 402, 'aioli': 448, 'carne': 469, 'jalapeno': 472, 'olive': 544, 'sirloin': 585, 'wahoo': 651, 'slaw': 780, 'chile': 799, 'avocado': 866, 'bacon': 1177, 'potato': 1186, 'carnita': 1271, 'shrimp': 1290, 'lime': 1335, 'fish': 1377, 'sausage': 2038, 'pork': 2156, 'cabbage': 2217, 'guacamole': 2615, 'pepper': 2764, 'cilantro': 3146, 'pico': 3273, 'steak': 3725, 'egg': 4131, 'cream': 4314, 'tomato': 4384, 'corn': 4522, 'flour': 4928, 'beef': 5421, 'rice': 6111, 'onion': 6178, 'salsa': 6369, 'chicken': 6487, 'lettuce': 6498, 'sauce': 6828, 'bean': 8431,  'cheese': 13832}
    ingredients = newdict.keys()
    ingredients = ingredients.sort()
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
        mydict = {'item':row['menus.name'].title(),
                    'name':row['name'].title(),
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