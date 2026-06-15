# 🔔 FocusBell

FocusBell is a productivity and task management web application built with Django. It helps users organize tasks, track deadlines, receive WhatsApp reminders, and get real-time browser alarm notifications before tasks are due.

## 🚀 Features

### User Authentication

* User Registration
* User Login & Logout
* Secure Authentication System

### Task Management

* Create Tasks
* Edit Tasks
* Delete Tasks
* Mark Tasks as Completed
* Task Priority (High / Low)
* Due Date & Due Time
* Task Description

### Task Filtering & Search

* Search Tasks by Title or Description
* Filter by Status

  * Pending
  * Completed
  * Overdue
* Filter by Priority
* Filter by Date

### Reminder System

* Reminder Before X Minutes
* Alarm Enable / Disable Toggle
* Automatic Reminder Processing

### WhatsApp Notifications

* Twilio WhatsApp Integration
* Automatic Reminder Messages
* Real-time Task Notifications

### Browser Alarm System

* Popup Reminder Notification
* Alarm Sound Notification
* Real-time Reminder Alerts

### Dashboard

* Pending Tasks Overview
* Completed Tasks Overview
* Overdue Tasks Overview
* Task Statistics

---

## 🛠️ Tech Stack

### Backend

* Django
* Python

### Database

* SQLite3

### Task Queue & Scheduling

* Redis
* Celery
* Celery Beat

### Notifications

* Twilio WhatsApp API
* Browser Notification System

### Frontend

* HTML
* CSS
* JavaScript

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kushwahrudraksh3-png/FocusBell-
cd FocusBell
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## Redis Setup

Start Redis Server:

```bash
redis-server
```

Check Redis:

```bash
redis-cli ping
```

Expected Output:

```bash
PONG
```

---

## Celery Worker

```bash
celery -A focusbell worker -l info
```

---

## Celery Beat

```bash
celery -A focusbell beat -l info
```

---

## Environment Variables

Create a `.env` file:

```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+91xxxxxxxxxx
```

---

## Project Workflow

```text
Create Task
      ↓
Reminder Time Reached
      ↓
Celery Beat Scheduler
      ↓
Celery Worker
      ↓
WhatsApp Notification
      ↓
Browser Alarm Triggered
      ↓
Popup + Sound Notification
```

---

## Future Enhancements

* Snooze Reminder
* Recurring Tasks
* Email Notifications
* Dark Mode
* Task Categories
* Calendar Integration
* Analytics Dashboard

---

## Developer

Developed by **Rudraksh Kushwah**

FocusBell is designed to help users stay productive and never miss important tasks.
