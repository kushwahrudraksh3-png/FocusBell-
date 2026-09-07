# 🔔 FocusBell

> **A Smart Notification & Task Reminder System built with Django**

FocusBell is a web-based productivity application designed to help users manage their tasks and receive timely reminders for important activities.

The application provides a simple interface for creating and managing tasks while keeping users informed through smart notifications and reminders.

---

## 🚀 Features

* 🔐 **User Authentication**

  * User registration and login
  * Secure user account management

* ✅ **Task Management**

  * Create tasks
  * View tasks
  * Manage task details
  * Track important activities

* 🔔 **Smart Reminders**

  * Set reminders for tasks
  * Receive notifications for scheduled activities
  * Helps users avoid missing important tasks

* 👤 **User Profiles**

  * Individual user accounts
  * Profile image support

* 🎨 **Clean User Interface**

  * Simple and easy-to-use interface
  * Responsive web pages
  * Static assets for styling and frontend functionality

* 🗄️ **Database Integration**

  * Stores users and task-related information
  * SQLite database for local development

---

## 🛠️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite

### Other

* Django Templates
* Django Authentication
* Static & Media Files

---

## 📂 Project Structure

```text
FocusBell/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── emailer.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── focusbell/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│
├── static/
│
├── media/
│   └── profile_images/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/kushwahrudraksh3-png/FocusBell-.git
```

### 2. Navigate to the project

```bash
cd FocusBell-
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The repository currently contains a `requirements.txt` with Django 5.0.14 and other Python dependencies.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the terminal instructions to create the admin account.

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Admin Panel

FocusBell uses Django's admin interface for managing application data.

After creating a superuser, open:

```text
http://127.0.0.1:8000/admin/
```

Login using your superuser credentials.

---

## 🧠 How FocusBell Works

```text
             ┌───────────────────┐
             │       User        │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │   Authentication  │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │  Create / Manage  │
             │      Tasks        │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Set Reminder /    │
             │ Notification Time │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Smart Notification│
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │   User is Alerted │
             └───────────────────┘
```

---

## 📌 Main Django Applications

### `accounts`

Handles user-related functionality such as:

* User accounts
* Authentication
* Profile information
* Email-related functionality

### `tasks`

Handles the application's task-related functionality such as:

* Creating tasks
* Managing tasks
* Task-related data
* Reminder functionality

### `focusbell`

This is the main Django project configuration containing:

* Project settings
* URL configuration
* WSGI configuration
* ASGI configuration

---

## 🔮 Future Improvements

The project can be extended with:

* 📱 Mobile application
* 📧 Email reminders
* 📲 Push notifications
* 🔔 Browser notifications
* 🤖 AI-based task prioritization
* 🧠 Smart reminder scheduling
* 📊 Productivity analytics
* 🔄 Recurring tasks
* 📅 Calendar integration
* 🌐 Cloud deployment
* 🔐 OAuth / Google Login

---

## 🎯 Use Cases

FocusBell can be useful for:

* Students managing assignments and study schedules
* Developers managing development tasks
* Professionals managing daily activities
* Teams tracking important tasks
* Anyone who wants timely reminders for important activities

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new feature"
```

5. Push the branch

```bash
git push origin feature/new-feature
```

6. Open a Pull Request

---

## 👨‍💻 Author

**Rudraksh Kushwah**

GitHub: [@kushwahrudraksh3-png](https://github.com/kushwahrudraksh3-png)

---

## 📄 License

This project is intended for educational and development purposes.

---

⭐ **If you find FocusBell useful, consider giving the repository a star!**
