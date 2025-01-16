Project Setup Instructions

Overview

This project consists of two parts:

Frontend Development: A responsive webpage with features like a fixed navbar, collapsible left menu, dynamic resizing based on screen width, and a footer.

Django Chat Application: A real-time chat application with user authentication, chat interface, and WebSocket integration.

Steps to Set Up the Django Project:

Clone the Repository:

git clone <repository_url>
cd <repository_folder>

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Setup the Database:

Run migrations to create the database schema.

python manage.py migrate

Create a superuser (admin):

python manage.py createsuperuser

Start the Development Server:

python manage.py runserver

Access the application at: http://127.0.0.1:8000/
