# Task-Management-API
**Description:** 
 - Build an API to manage tasks where users can create, update, and delete tasks, and mark tasks as complete or incomplete.

**Requirements:**
 - CRUD operations for tasks and users.
 - Endpoint for marking tasks as complete or incomplete.
 - Use Django ORM for database interactions.
 - Deploy the API on Heroku or PythonAnywhere.
**Project Managment(TRELLO)**
[KANBAN BOARD](https://trello.com/b/NsJUTf2w/capstone-alx)

### 1. Initializing Git and GitHub
Create a new directory for the project:
   ```bash
   mkdir task_management_api
   cd task_management_api
   git init
   git remote add origin [Repository Link](https://github.com/KhadijaMakkaoui/Task-Management-API.git) 
   ```

### 2. Setting Up Django Project Structure
   ```bash
    pip install django
    #Create an app for managing tasks
    python manage.py startapp tasks
```
Add the app to INSTALLED_APPS in task_management/settings.py

### 3. Creating a Virtual Environment and Installing Dependencies
```bash
#Create a virtual environment to isolate project dependencies
python -m venv venv
# Activate the virtual environment on Windows
venv\Scripts\activate
#Install required dependencies, including Django and Django REST Framework
pip install django djangorestframework
#Save dependencies to requirements.txt to simplify future setup
pip freeze > requirements.txt
#Run initial migrations for the project
python manage.py migrate
```

