# Full Stack Web Application

Welcome to my first Full Stack Web Application! This project combines the power of **Flask** for the backend and **React** for the frontend, offering a seamless web experience.

---

## Project Structure

### **Backend:**
- Built using **Flask**, a lightweight and powerful WSGI web framework for Python.

### **Frontend:**
- Developed with **React**, a popular JavaScript library for crafting dynamic user interfaces.

---

## Features
- **Modern Tech Stack**: Flask + React for a responsive and efficient application.
- **Modular Structure**: Organized backend and frontend directories for maintainability.
- **Easy Setup**: Straightforward installation and deployment process.

---

## ⚙Installation

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.x**
- **Node.js & npm**

### **Backend Setup (Flask)**
1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```sh
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```
   The backend will be running at **http://127.0.0.1:5000/**.

### **Frontend Setup (React)**
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the React development server:
   ```sh
   npm run dev
   ```
   The frontend will be running at **http://localhost:3000/**.

---

## Usage
- **Access the backend API** at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
- **Open the frontend UI** at [http://localhost:3000/](http://localhost:3000/).

---

## Contributing
Want to contribute? Follow these steps:

1. **Fork** the repository
2. **Create** a new feature branch:
   ```sh
   git checkout -b feature/your-feature
   ```
3. **Commit** your changes:
   ```sh
   git commit -m "Add some feature"
   ```
4. **Push** to your branch:
   ```sh
   git push origin feature/your-feature
   ```
5. **Create a Pull Request** 📩

---

## Acknowledgments
This project was inspired by my passion for learning **Full Stack Development** using Flask and React. I hope you find it useful.
