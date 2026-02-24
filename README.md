# 🎯 Django Quiz Application

A full-stack, category-based Quiz Web Application built using Django.  
Users can register, log in, take timed quizzes, and track their previous scores.

---

## 🚀 Live Demo

🔗 https://quiz-app-o808.onrender.com/

---

## 📌 Features

- 🔐 User Authentication (Register, Login, Logout)
- 📂 Category-Based Quiz System
- 📝 Dynamic Question Rendering
- ⏳ Global Quiz Timer with Auto Submit
- 📊 User Score Tracking & History
- 🗂️ Django Admin Panel for Question Management
- 🎯 Automatic Result Calculation
- 🛡️ CSRF Protection
- 📱 Responsive UI

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django ORM

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite (Development)
- PostgreSQL (Production)

### Deployment
- Render
- Gunicorn
- Whitenoise

---

## 📂 Project Structure

```
quiz_app/
│
├── quiz/                # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│
├── quiz_app/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone the Repository

```
git clone https://github.com/hk-vishwakarma/quiz-app.git
cd quiz-app
```

### 2️⃣ Create Virtual Environment

```
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## 🧠 Database Models

### Category
- name

### Question
- category (ForeignKey)
- question
- option1
- option2
- option3
- option4
- answer

### UserScore
- user (ForeignKey)
- category (ForeignKey)
- score
- total
- date

---

<!-- ## ⏳ Quiz Timer

The application includes a JavaScript-based global countdown timer that:

- Starts automatically when quiz begins
- Displays remaining time
- Automatically submits the quiz when time expires

--- -->

## 📊 User Score Tracking

- Stores quiz attempts in database
- Displays previous scores
- Tracks category-wise performance
- Saves attempt date and time

---

## 🔒 Security

- CSRF Protection
- Secure authentication
- Session-based quiz handling
- Environment variables for SECRET_KEY and DATABASE

---

## 🌍 Deployment

Deployed on Render using:

```
gunicorn quiz_app.wsgi
```

Includes:
- PostgreSQL Database
- Whitenoise for static files
- Environment variables for production

---

## 🚀 Future Enhancements

- Quiz timer to auto submit the quiz with specific time limit
- Leaderboard system
- Per-question timer
- AJAX-based quiz navigation
- Difficulty levels
- Performance analytics dashboard

---

## 👨‍💻 Author

Your Name  
GitHub: https://github.com/hk-vishwakarma  
LinkedIn: https://linkedin.com/in/hemant-kumar-vishwakarma

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.