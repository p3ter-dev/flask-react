Full Stack Web Application
This is my first full stack web application designed using Flask for the backend and React for the frontend.

Project Structure:

backend:

using flask

frontend:

using react

Features:

Backend: Implemented with Flask, a lightweight WSGI web application framework in Python.

Frontend: Developed using React, a JavaScript library for building user interfaces.

Installation:

Prerequisites:

Python 3.x

Node.js and npm

Backend Setup:

Navigate to the backend directory:

cd backend

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

pip install -r requirements.txt

Run the Flask application:

export FLASK_APP=app.py

export FLASK_ENV=development

flask run


Frontend Setup:

Navigate to the frontend directory:

cd frontend

Install the required packages:

npm install


Run the React application:

npm start

Usage:

Backend: The Flask server will be running on http://127.0.0.1:5000/.

Frontend: The React development server will be running on http://localhost:3000/.

Contributing:

Fork the repository

Create your feature branch:

git checkout -b feature/your-feature

Commit your changes:

git commit -m 'Add some feature'

Push to the branch:

git push origin feature/your-feature

Create a new Pull Request

Acknowledgments:

Inspired by the need to learn full stack development using Flask and React.

