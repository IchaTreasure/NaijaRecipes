<h1>Naija Recipes</h1>

<h2> WHAT IS IT? </h2>

<p> This webapp is designed to allow users to add their recipes and / or search for other recipes that have been added by other 
users. The webapp offers a search bar to search for existing recipes. The webapp also allows users to edit any inaccurate information about a recipe.
The overall aim is to have an easy to navigate website that was designed desktop first to enable users to find Recipes.</p>

<h2>UX</h2>
<p>The web application is designed to be extremely straight forward, a registration page for new users, a login page for existing users which takes them to the homepage.
The homepage has links to All Recipes which shows all the recipes that have been added into the database, then another link with a dropdown to 5 different categories i.e 
Appetizer, dessert, Lunch, Main Dish and Side Dish. clicking any of this links sends the user to all the recipes with that category. There is an Add Recipe link the shows 
the user a form to input the recipe they want to, a contact us page with a form, alink to sign out which ends the current session and finally a search form that searches the database for any recipe.
When a user clicks the view button to view a recipe they have the option of either deleting or editing the recipe. 
</p> 


<h2>User Stories</h2>
<p>This web application is accesible for all user from mobile device and desktop.</p>

<p> As a new user I'm able to do the following:</p>

<p> Register/ sign up to use the services.</p>
<p> Go to the All Recipes page where all recipes will be shown. The user is also able to search for a recipe on the nav bar</p>
<p> The user is able to add a new recipe, by clicking on the Add Recipe.</p>
<p> The user is able to search for a recipe with the help of the search form on the navbar</p>
<p> The user is able to see a single recipe by clicking on the View Recipe botton on the recipe cards</p>
<p> The user is able to edit a recipe once the sinlge recipe is displayed</p>
<p> The user is able to remove a recipe.</p>

<h2>Features</h2>
<p>User Registration: User's who wish to submit their work to the site will have to register first. This is done using Flask, Bcrypt and MongoDB as the database for users.</p>

<p>User Login: As above. Registered users must login before attempting to share work on the site.</p>

<p>Messages indicating if Username is already taken at registration, or incorrect username/password at login.</p>

<p>User Logout: Enables the user to end the session.</p>

<p>Search functionality: To search for recipes by name.</p>

<p>Recipes by categories: 5 main recipe categories</p>


<h2> Future features </h2>

<p>Comments section: Give other users the ability to comment/critique on others work.</p>

<p>Rate recipes: Rate the recipes with a star rating system.</p>

<p>Add pictures </p>

<h2>Tools/Technologies</h2>
<h3>AWS Cloud9</h3>
<p>Cloud9 hosted my Workspace for this project</p>

<h3>Git</h3>
<p>Used to push and commit any and all changes to my repository on GitHub</p>

<h3>Bootstrap</h3>
<p>Allows for extra responsiveness of html5 and JavaScript files, also Provided my buttons and modal.</p>

<h3>Materialize</h3>
<p>Materialize has been implemented for styling the webapp.</p>

<h3>JavaScript</h3>
<p>JavaScript has been used to implement the functionalities of the side nav, slider and nav dropdown</p>

<h3>Heroku</h3>
<p>The site has been deployed using Heroku and is available to visit here: https://naija-recipes.herokuapp.com/</p>

<h3>Plugins</h3>
<p>• https://fonts.googleapis.com/icon?family=Material+Icons</p>

<p>• https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css</p>

<p>• https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js</p>

<p>• https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js</p>

<h3>Testing</h3>
<p>The HTML and CSS coding was tested by using the W3C Mark Validator Service by direct input.</p>
<p>To test the responsiveness of the website in phones, tablets, and desktops screens, I have used the Chrome Developer Tools.</p>
<p>The JavaScript files were tested using https://jslint.com/ by direct input of the files on the validator.</p>
<p>The game functionality, tested on multiple browers such as Chrome, Edge, Safari and Firefox.</p>
<p>The game has been tested by some of my friends with the question if the game was clear, easy to use and understandable.</p>

<h2>Bugs</h2>
<p>Had some issues with the re-sizing of the tiles on smaller devices. Since these kind of games are not made for small mobile devices, I kept iPad size in mind as the smallest easy accesible play-size</p>

<h2>Deployment</h2>
<p> Modules to be installed</p>
<p> os</p>
<p> Flask - render_template, redirect, request, url_for, session, flash</p>
<p> PyMongo</p>
<p> flask_pymongo</p>
<p> Bcrypt</p>
<p> bson.objectid - ObjectId</p>
<p> Creating a requirements.txt and Procfile</p>
<p> In CLI input pip3 freeze --local > requirements.txt . This should generate a file with all tools listed and they're version number.</p>
<p> Procfile - in CLI input echo web: python app.py > Procfile</p>
<p> Creating an app on Heroku</p>
<p> Create account with Heroku.</p>
<p> Select "New" then "Create new app"</p>
<p> Input app-name and region (Europe in this case)</p>
<p> Follow steps for "Deploy using Heroku Git" (push from CLI, described below)</p>
<p> Set Config vars (described below)
<p> Push to Heroku
<p> First, ensure requirements.txt and Procfile are configured.</p>
<p> In temrinal window, run "heroku login"
<p> Press and key to be redirected to Heroku Login page, select "Login in to Heroku CLI"</p>
<p> Return back to Terminal, Herok ushould be logged in, run the command "git push heroku master".</p>
<p> Once successfully completed, " https://share-a-script.herokuapp.com/ deployed to Heroku" will be available in terminal window, you can follow this link to view your application.</p>
<p> Set config vars on Heroku</p>
<p> From your app dashboard, select settings</p>.
<p> In settings, select "Reveal config vars"</p>
<p> The following need to be configured;</p>
<p> I.P : 0.0.0.0</p>
<p> PORT : 5000</p>
<p> MONGO_URI : mongodb+srv://root:password@clustername-yibrd.mongodb.net/collectionname?retryWrites=true&w=majority</p>
<p> SECRET_KEY : secret_key</p>

<p>The repository can be found on: https://github.com/IchaTreasure/NaijaRecipes</p>

<p>The site has been deployed using GitHub Pages and is available to visit here: https://naija-recipes.herokuapp.com/</p>

<h2>Credits</h2>
<p>I would to credit the following sources for their inspiration:</p> 
<p>Stack Overflow community</p>
<p>CodePen community </p>
<p>GitHub community</p> 
<p>W3schools</p>


<h2>Media</h2>
<p>Slider image was taken from google.</p> 

<h2>Acknowledgement</h2>
<p>I would like to thank my mentor Anthony Ngene, for his support throughout this project.</p>