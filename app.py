import os
import re
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return render_template("recipes.html",
                               Recipies=mongo.db.Recipies.find())
    return render_template('index.html')


"""https://github.com/PrettyPrinted/mongodb-user-login/
blob/master/login_example.py
"""


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return render_template('failedindex.html')


"""https://github.com/PrettyPrinted/mongodb-user-login/
blob/master/login_example.py"""


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert({'name': request.form['username'],
                         'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return render_template('failedregister.html')

    return render_template('register.html')


@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", Recipies=mongo.db.Recipies.find())


@app.route('/add_recipes')
def add_recipes():
    return render_template("addRecipes.html",
                           categories=mongo.db.categories.find())


@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    Recipies = mongo.db.Recipies
    Recipies.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipes/<recipes_id>')
def edit_recipes(recipes_id):
    the_recipes = mongo.db.Recipies.find_one({"_id": ObjectId(recipes_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editRecipes.html', recipe=the_recipes,
                           categories=all_categories)


@app.route('/update_recipes/<recipes_id>', methods=["POST"])
def update_recipes(recipes_id):
    Recipies = mongo.db.Recipies
    Recipies.update({'_id': ObjectId(recipes_id)},
                    {
        'category_name': request.form.get('category_name'),
        'recipe_title': request.form.get('recipe_title'),
        'prep_time': request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'number_of_servings': request.form.get('number_of_servings'),
        'ingredients': request.form.get('ingredients'),
        'instructions': request.form.get('instructions')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipes/<recipes_id>')
def delete_recipes(recipes_id):
    mongo.db.Recipies.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_recipes'))


@app.route('/view_recipes/<recipes_id>', methods=["GET"])
def view_recipes(recipes_id):
    the_recipes = mongo.db.Recipies.find_one({"_id": ObjectId(recipes_id)})
    return render_template('viewRecipes.html', recipe=the_recipes)


@app.route('/contact_Us')
def contact_Us():
    return render_template("contactUs.html")


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           Recipies=mongo.db.Recipies.find())


@app.route('/view_appetizer')
def view_appetizer():
    return render_template('appetizer.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': 'Appetizer'}))


@app.route('/view_dessert')
def view_dessert():
    return render_template('dessert.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': 'Dessert'}))


@app.route('/view_lunch')
def view_lunch():
    return render_template('lunch.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': 'Lunch'}))


@app.route('/view_maindish')
def view_maindish():
    return render_template('maindish.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': 'Main Dish'}))


@app.route('/view_sidedish')
def view_sidedish():
    return render_template('sidedish.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': 'Side Dish'}))


@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    regx = re.compile(request.form['browse_recipes'], re.IGNORECASE)
    return render_template("searchRecipes.html",
                           Recipies=mongo.db.Recipies.find
                           ({'recipe_title': regx}))
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
