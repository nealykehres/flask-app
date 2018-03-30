from flask import Flask, render_template
from modules import convert_to_dict
from datetime import datetime


app = Flask(__name__)

coffee_list = convert_to_dict("coffee.csv")

@app.route('/')
def index():
    ids_list = []
    name_list = []
# fill one list with the number of each presidency and
# fill the other with the name of each president
    for coffee in coffee_list:
        ids_list.append(coffee['id'])
        name_list.append(coffee['name'])
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="Coffee Shop Index")

# your code here

@app.route('/coffee/<num>')
def detail(num):
    for coffee in coffee_list:
        if coffee['id'] == num:
            coffee_dict = coffee
            break
    return render_template('coffee.html', coff=coffee_dict, the_title=coffee_dict['name'])
# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
