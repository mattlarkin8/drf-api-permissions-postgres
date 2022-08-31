# **LAB - Class 32**

## **Project: Permissions and PostgreSQL**

### Author: Matthew Larkin

### Setup

Ensure you have properly setup your `venv`. Install dependencies from `requirements.txt`.  

Use `python manage.py runserver` to test the site deployment on your local machine.  

If you have docker, use `docker-compose up --build` to build and test a Docker deployment of the Django app.

### Tests

Testing uses the built-in django testing framework.

Run the tests with `python manage.py test`.

The last test is important because it shows that the user cannot create a new item without being logged in. That test is missing the line: `self.client.login(username='testuser', password="pass")`. Without logging in, our authentication check keeps unknown users from changing the database.
