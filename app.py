import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
import bcrypt 
from bson.objectid import ObjectId

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
#app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#@app.route('/')
#def hello():
#  return 'Hello World ...again'
    
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", Recipies=mongo.db.Recipies.find())


@app.route('/add_recipes')
def add_recipes():
    return render_template("addRecipes.html", categories=mongo.db.categories.find())
    
    
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    Recipies = mongo.db.Recipies
    Recipies.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
    
@app.route('/edit_recipes/<recipes_id>')
def edit_recipes(recipes_id):
    the_recipes =  mongo.db.Recipies.find_one({"_id": ObjectId(recipes_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editRecipes.html', recipe=the_recipes,
                           categories=all_categories)
                           

@app.route('/update_recipes/<recipes_id>', methods=["POST"])
def update_recipes(recipes_id):
    Recipies = mongo.db.Recipies
    Recipies.update( {'_id': ObjectId(recipes_id)},
    {
        'recipe_title':request.form.get('recipe_title'),
        'prep_time':request.form.get('prep_time'),
        'cook_time': request.form.get('cook_time'),
        'number_of_servings': request.form.get('number_of_servings'),
        'ingredients':request.form.get('ingredients'),
        'instructions':request.form.get('instructions')
    })
    return redirect(url_for('get_recipes'))
    
    
@app.route('/delete_recipes/<recipes_id>')
def delete_recipes(recipes_id):
    mongo.db.Recipies.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_recipes'))
    
@app.route('/view_recipes/<recipes_id>', methods=["GET"])
def view_recipes(recipes_id):
    the_recipes =  mongo.db.Recipies.find_one({"_id": ObjectId(recipes_id)})
    return render_template('viewRecipes.html', recipe=the_recipes)
    
@app.route('/contact_Us')
def contact_Us():
    return render_template("contactUs.html")
    
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           Recipies=mongo.db.Recipies.find())

@app.route('/search_recipes', methods=['GET'])
def search_recipes():
    return render_template("searchRecipes.html", Recipies=mongo.db.Recipies.find_one({'recipe_title': request.form['browse_recipes']}))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
