# 🐝 Online Quiz Bees – Django Web App

![License](https://img.shields.io/badge/license-MIT-green)
![Django](https://img.shields.io/badge/Django-5.2.4-darkgreen?logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-blueviolet?logo=bootstrap)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> A fully functional web-based quiz platform built with **Django** and **Bootstrap**. Users can log in, take quizzes, submit answers, and view results.

---

## 📸 Preview

![Homepage Screenshot](https://via.placeholder.com/800x300.png?text=Homepage+Screenshot)
![Quiz Screenshot](https://via.placeholder.com/800x300.png?text=Quiz+Page)
![Result Screenshot](https://via.placeholder.com/800x300.png?text=Result+Page)

---

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Pages and URLs](#pages-and-urls)
- [Admin Access](#admin-access)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

- 🏠 Homepage with quiz overview
- ✅ Authentication with login/logout
- 📝 Dynamic quiz with questions and multiple choices
- 📊 Auto-scoring with result summary
- 🧠 Admin panel to manage questions and answers

---

## 📂 Folder Structure

onlinecourse/  
├── courseapp/  
│ ├── migrations/  
│ ├── templates/  
│ │ ├── base.html  
│ │ ├── homepage.html  
│ │ ├── login.html  
│ │ ├── course_details_bootstrap.html  
│ │ └── exam_result.html  
│ ├── admin.py  
│ ├── models.py  
│ ├── views.py  
│ └── urls.py  
├── onlinecourse/  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
├── db.sqlite3  
├── manage.py  
└── README.md    


---

## ⚙️ How to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/badalrai21/django-python-quiz-web.git
cd django-python-quiz-web
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install django
```

### 4️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser (for admin login)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server
```bash
python manage.py runserver
```

### 🔒 Admin Access
To access the admin dashboard:

Start the server: python manage.py runserver

Open http://127.0.0.1:8000/admin/

Log in using your superuser credentials

Add new Courses, Questions, Choices, and Submissions

🔍 App Navigation
Page	URL	Description
Home	http://127.0.0.1:8000/	Homepage with link to quizzes
Login	/login/	Login page
Logout	/logout/	Logs out the user
Admin Panel	/admin/	Manage courses, questions, submissions
Course Quiz	/1/	Quiz page for course with ID = 1
Submit Exam	/1/submit/	Submits answers
Result View	/1/submission/1/result/	Displays result for submission


 ## 📌 Notes
Quiz can only be taken after login  

Questions and answers are defined in the admin panel  

Course ID must match an existing course in the database  

Homepage lists available courses dynamically  
  
## 🛡️ License
This project is licensed under the MIT License.

## 👨‍💻 Author 🙋‍♂️
 Made with ❤️ by Badal Kumar Rai
 GitHub: [@badalrai21](https://github.com/badalrai21).
 LinekdIn: [@BadalRai](https://www.linkedin.com/in/badal-rai)    
 Discord: Join our Discord Server [@NO2](https://discord.gg/Dnw4ZjEg)    

