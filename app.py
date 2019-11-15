import os
import re
import boto3
from botocore.client import Config
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId
from werkzeug import secure_filename

from dotenv import load_dotenv
load_dotenv()

ACCESS_KEY_ID = os.environ.get('ACCESS_KEY_ID')
ACCESS_SECRET_KEY = os.environ.get('ACCESS_SECRET_KEY')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

s3 = boto3.resource('s3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
    )

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
    
    f = request.files['file']
    
    f.save(secure_filename(f.filename))
    filename= secure_filename(f.filename)
    with open( filename, 'rb') as f: 
 
    
        s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=f, ACL='public-read')

    Recipies = mongo.db.Recipies
    recipe_dict = request.form.to_dict()
    recipe_dict['image_url'] = "https://naija-recipe.s3.eu-west-2.amazonaws.com/" + filename
    Recipies.insert_one(recipe_dict)
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


@app.route('/view_category')
def view_category():
    cat = request.args.get('cat')
    return render_template('getCat.html',
                           Recipies=mongo.db.Recipies.find
                           ({'category_name': cat}))


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
