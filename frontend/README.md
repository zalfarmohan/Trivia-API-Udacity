# Full Stack Trivia API  Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend).
> It is recommended you stand up the backend first, test using Postman or curl, update the endpoints in the frontend, and then the frontend should integrate smoothly.

# Features
    - Play the quiz game, randomizing either all questions or within a specific category.
    - Add questions and require that they include question and answer text.
    - Search for questions based on a text query string.
    - Display questions - both all questions and by category. questions show the question, category and difficulty rating by default and can show/hide the answer.
    - Delete questions.
    

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

## Required Tasks

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

# Backend
# Installing Dependencies
# Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs.

# Virtual Environment
We recommend working within a virtual environment whenever using python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the python docs https://docs.python.org/3/library/venv.html?highlight=virtual%20environment

# PIP Dependencies
Once you have your virtual environments setup and running, installing dependencies by navigating to the /backend directory and running:
    `pip install -r requirements.txt`
This will install all of the required packages we selected within the requirements.txt file.

# Key Dependencies
* Flaks (http://flask.pocoo.org/ "Flask") is a lightweight backend microseervices framework. Flask is required to handle requests and responses.
* SQLAlchemy (https://www/sqlalchemy.org/ "SQLAlchemy") is the python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in __init__.py and reference models.py
* Flask-Cors - (https://flask-cors.readthedocs.io/en/latest/ "Flask-CORS") is the extension we will use to hadnle cros origin requests from our frontend server.

# database Setup
With postgres running, restore a database using the trivia.psql file provided.
From the /backend folder in terminal run
`psql trivia < trivia.psql`

# Running The Server
From within the backend directory first ensure you're working using your created virtual environment.
To run the server, execute:
` *export FLASK_APP=flaskr*
*export FLASK_ENV=development*
*FLASK_DEBUG=true flask run* `

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.
if running locallay on windows, look for the commands in the [Flask docuemntation] (http://flask.pocoo.org/docs/1.0/tutorial/factory/ "Flask Documentation").

The application is running on http://127.0.0.1:5000 by default and is a proxy in the fronted configuration.

# Testing....
in order to run tests, navigate to the backend folder and run the following commands

>` dropdb trivia_test
  createdb trivia_test
  psql trivia_test < trivia.psql
  python3 test_flaskr.py `
  
  > Tip: *First time you run the tests, omit the dropdb command.*

  All tests are kept in that file adn should be maintained as updates are made to app functionality.



## Request Formatting

The frontend should be fairly straightforward and disgestible. You'll primarily work within the ```components``` folder in order to edit the endpoints utilized by the components. While working on your backend request handling and response formatting, you can reference the frontend to view how it parses the responses. 

After you complete your endpoints, ensure you return to and update the frontend to make request and handle responses appropriately: 
- Correct endpoints
- Update response body handling 

## Optional: Styling

In addition, you may want to customize and style the frontend by editing the CSS in the ```stylesheets``` folder. 

## Optional: Game Play Mechanics

Currently, when a user plays the game they play up to five questions of the chosen category. If there are fewer than five questions in a category, the game will end when there are no more questions in that category. 

You can optionally update this game play to increase the number of questions or whatever other game mechanics you decide. Make sure to specify the new mechanics of the game in the README of the repo you submit so the reviewers are aware that the behavior is correct. 


  # API Reference
  
  API references To understand how API it works Read this [API_README.md](../API_README.md)

# Screenshoots
These are screenshoots of the project [Click Here](../screenshoots/README.md)

# Deployment N/A

# Authors
* Farhan Madka worked on the API and test suite to integrate with the frontend
* Udacity provided the starter files for the project including frontend
  
