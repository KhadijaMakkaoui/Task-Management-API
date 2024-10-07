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

**Entity Relationship Diagram(ERD)**
[ERD](https://app.diagrams.net/#G1lekn2Wom29qhsDX8EC3E5F7yG98U_a2S#%7B%22pageId%22%3A%22C5RBs43oDa-KdzZeNtuy%22%7D)

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
    pip install djangorestframework
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

### Task URLs (CRUD Operations):
GET /tasks/ → List all tasks.

POST /tasks/ → Create a new task.

GET /tasks/<id>/ → Retrieve a specific task.

PUT /tasks/<id>/ or PATCH /tasks/<id>/ → Update a 
specific task.

DELETE /tasks/<id>/ → Delete a specific task.

User URLs (CRUD Operations):

GET /users/ → List all users.

POST /users/ → Create a new user.

GET /users/<id>/ → Retrieve a specific user.

PUT /users/<id>/ or PATCH /users/<id>/ → Update a 
specific user.

DELETE /users/<id>/ → Delete a specific user.

Custom Action URLs (Using @action):

PATCH /tasks/<id>/mark_complete/ → Mark a task as 
complete.

PATCH /tasks/<id>/mark_incomplete/ → Revert a task to incomplete.

##  Setting Up JWT Authentication 
1. Install Required Packages:
```bash
pip install djangorestframework-simplejwt
```
2. Configure JWT in Django:
```bash
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # By default, require users to be logged in
    ],}
```

