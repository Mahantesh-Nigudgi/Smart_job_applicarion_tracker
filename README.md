# Smart Job Application Tracker

A Django-based web application designed to help users manage and track their job applications in one place.

## 🚀 Live Demo

**Live Application:**
https://mahantesh1313.pythonanywhere.com/

---

## 📌 Project Overview

The **Smart Job Application Tracker** helps job seekers maintain their application details and track the progress of each application.

Users can register, log in, add job applications, view their applications, and delete them from their personal dashboard.

---

## ✨ Features

* 👤 User Registration
* 🔐 User Login & Logout
* 📝 Add Job Applications
* 📋 View Job Applications
* 🏢 Company Name Tracking
* 💼 Job Title & Designation
* 📍 Job Location
* 📅 Application Date
* 💰 Salary / LPA
* 📊 Application Status
* 🗑️ Delete Job Applications
* 🔒 User-specific Job Applications
* 📱 Bootstrap-based User Interface

### Application Status

* Applied
* Interview
* Selected
* Joined

---

## 🛠️ Technology Stack

* **Python**
* **Django**
* **SQLite**
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **Django Crispy Forms**
* **Crispy Bootstrap 5**
* **PythonAnywhere**

---

## 📂 Project Structure

```text
Smart_Job_Application_Tracker/
│
├── Smart_Job_Application_Tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
│
├── Tracker/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── form.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── login.html
│   ├── registration.html
│   ├── home.html
│   └── add_job.html
│
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

The application uses Django's built-in authentication system.

Users can:

1. Register an account
2. Log in
3. Access their dashboard
4. Add job applications
5. View their applications
6. Delete their applications
7. Log out

---

## 📊 Job Application Details

Each application can store:

| Field            | Description                     |
| ---------------- | ------------------------------- |
| Company Name     | Name of the company             |
| Job Title        | Position applied for            |
| Designation      | Job designation                 |
| Location         | Job location                    |
| Application Date | Date of application             |
| Status           | Current application status      |
| Salary           | Expected/ offered salary in LPA |

---

## 🔒 User Data Management

Each job application is associated with the authenticated user.

This ensures that users can manage their own job applications from their dashboard.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart_Job_Application_Tracker.git
```

### 2. Navigate to the project

```bash
cd Smart_Job_Application_Tracker
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## ☁️ Deployment

The application is deployed on **PythonAnywhere**.

### Live Website

https://mahantesh1313.pythonanywhere.com/

---

## 🔮 Future Enhancements

* ✏️ Edit job applications
* 🔎 Search and filter applications
* 📊 Dashboard statistics
* 📈 Application status charts
* 📅 Interview date tracking
* 🔔 Interview reminders
* 📧 Email notifications
* 📄 Resume management
* 🌙 Dark mode
* 📱 Improved mobile responsiveness
* 🔐 Password reset
* 👤 User profile management

---

## 🎯 Learning Outcomes

This project helped me gain practical experience with:

* Django MVC/MVT architecture
* Django ORM
* Django authentication
* Database relationships
* CRUD operations
* Django forms
* HTML templates
* Bootstrap
* SQLite
* Virtual environments
* Static files
* WSGI
* Cloud deployment
* PythonAnywhere

---

## 👨‍💻 Author

**Mahantesh Nigudgi**

### Project

**Smart Job Application Tracker**

### Live Demo

https://mahantesh1313.pythonanywhere.com/

---

## ⭐ Project Status

**Deployed and available online.**
