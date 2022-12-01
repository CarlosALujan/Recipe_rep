# Recipe_rep
GitHub Project Repo Link: https://github.com/CarlosALujan/Recipe_rep

Carlos Lujan 2 Pull Request List Link
https://github.com/CarlosALujan/Recipe_rep/pull/2


Neil williamson 2 pull request list links
https://github.com/CarlosALujan/Recipe_rep/pull/3
https://github.com/CarlosALujan/Recipe_rep/pull/1

2+ examples of things you enjoyed about or learned from this project
1. Carlos - I learned to be confident in my REST API implementation skills, I had trouble with the moviedatabase and was terrified to 
handle this food related API. Suprisingly this API was easier to implement thanks to our previous task in the class.
2. Neil - Getting more familiar with css and making pages look more interesting than barebones html

2+ examples of things you didn’t enjoy or wanted to learn from this project
1. Carlos - One thing I didnt enjoy about the project was that it was great idea, but there wasn't enough time to complete the website as planned. The website is great and is unique for people who dont know what to make for food but could have better features.
2. Neil - Similarly for me, time constraints/conflicts with other classes and projects prevented us from meeting together early on and working on the project for any extended amount of time.

Google Doc Link Access: https://docs.google.com/document/d/1kuS3163BdiRUt3XGXGROzh7W2G6vgTYHsv9nNyhH_J8/edit?usp=sharing
Fly.io Deployment Link: https://bitter-darkness-8066.fly.dev/


Technical Requirements:
1 - Flask Server
2 - Postgres database
3 - REST API Integration
4 - User login
Strech Features:
1 - Beautification

App Overview:
/Static
  Stylesheet.css - basic css file that includes a background color used in some html pages.
/Templates
  home.html- an html page that is used by users to put in a plate/ingredient and submit to recieve a random recipe.
  login.html- an html page that is used by users to login into their account for the website.
  random.html- an html page that displayed the data from the api which was the recipe name, image, ingredients, and steps.
  randomupdated.html- replaced random.html due to it having beautification.
  signup.html- an html page that is used by users to signup and create an account for the website.
  
.gitignore - ignore file that is used to hide our api key.
Procfile - Procfile contains gunicorn which helps our app run.
README.md - Currently in the README.md
app.py - python file used to handle all our API, Login, Flask, and database work.
fly.toml - contains the info needed for the deployment and upkeep of our website in fly.io
requirments.txt - has all requirments for the deployment to have in order to run.
