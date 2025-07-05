# 🧠 Online Quiz Bees 🐝

An interactive Django-based quiz application that allows users to **log in**, **take quizzes**, and **view exam results** — all built with Python, Django, and Bootstrap.

---

## 🚀 Features

- 🔐 User login & logout
- 🎓 Course detail view with quiz questions
- ✅ Submit answers and get results instantly
- 📊 Auto-scored submissions
- 🛠️ Admin panel for managing courses, questions, and choices

---

## 📸 Screenshots

| Login Page | Course Page | Result Page |
|------------|-------------|-------------|
| ![Login](screenshots/login.png) | ![Course](screenshots/course.png) | ![Result](screenshots/result.png) |

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

## 👨‍💻 Author
 Badal Kumar Rai
 GitHub: [@badalrai21](https://github.com/badalrai21).
 LinekdIn: [@BadalRai](https://www.linkedin.com/in/badal-rai)    
 Discord: Join our Discord Server [@NO2](https://discord.gg/Dnw4ZjEg)    

