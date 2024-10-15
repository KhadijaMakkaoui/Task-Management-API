# Task-Management-API
**Description:** 
 - Build an API to manage tasks where users can create, update, and delete tasks, and mark tasks as complete or incomplete.
[Why this project?](https://docs.google.com/document/d/1Z6l5HpufAk9zf80xHqzrFSb3Xi4nLM0krLZKU5nU1ds/edit?usp=sharing)
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
### Configure PostgreSQL db
Install PostgreSQL and psycopg2
First, ensure that PostgreSQL is installed on your system. You will also need the psycopg2 package to allow Django to interact with the PostgreSQL database.
- Install psycopg2 using pip:

```bash
pip install psycopg2
```
- Modify the DATABASES setting in the settings.py file to use PostgreSQL instead of SQLite.
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
3. Usage:
You can now use the /api/token/ endpoint to obtain an access and refresh token by sending a POST request with valid user credentials (username and password).

Use the /api/token/refresh/ endpoint to refresh the access token using the refresh token.

4. Implement task filtering and sorting in Django REST Framework
   1. install django filter
```bash
   pip install django-filter
```
   2. Update settings to include DjangoFilterBackend
    Add DEFAULT_FILTER_BACKENDS to the settings.py file
   3. Define Filters and Ordering in the View
   
   4. API Requests
   Filter by status: /api/tasks/?status=pending

   Filter by priority: /api/tasks/?priority=high

   Filter by due date: /api/tasks/?due_date=2024-10-07

   Sort by due date: /api/tasks/?ordering=due_date

   Sort by priority: /api/tasks/?ordering=priority_level

   if you'd like to reverse the order, use a minus sign: /api/tasks/?ordering=-priority_level
   Filter by status and sort by due date: /api/tasks/?status=pending&ordering=due_date

# Deployment with PythonAnywhere