# Healthcare Backend - Django Assignment

This is a backend system for a healthcare app, built with Django, Django REST Framework, PostgreSQL, and JWT authentication. It covers everything you'd expect — user sign-up and login, patient and doctor management, and mapping doctors to patients. The main goal is to keep things secure and organized, so only authenticated users can mess with sensitive data.

## Features

- User authentication with JWT (so, register and log in)
- Manage patients (add, view, update, delete)
- Manage doctors (same deal)
- Assign doctors to patients
- Role-based access (only logged-in users get to the important stuff)

## Project Structure

Healthcare-backend/
├── healthcare/ # Django project config
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── authentication/ # Handles registration/login
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── patients/ # All patient-related logic
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── doctors/ # All doctor-related logic
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── mappings/ # Linking doctors and patients
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── manage.py
├── requirements.txt
└── .env.example

## Getting Started

### 1. Create your virtual environment and install the dependencies

python -m venv venv
source venv/bin/activate # Linux/Mac

# or

venv\Scripts\activate # Windows

pip install -r requirements.txt

### 2. Set up your PostgreSQL database

CREATE DATABASE healthcare_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE healthcare_db TO postgres;

### 3. Configure environment variables

cp .env.example .env

# Open up .env and fill in your values

### 4. Run migrations

python manage.py makemigrations
python manage.py migrate

### 5. Fire up the server

python manage.py runserver

## API Endpoints

### Authentication

POST `/api/auth/register/` — Register a new user  
POST `/api/auth/login/` — Log in and grab your tokens

### Patients (Authentication Required)

POST `/api/patients/` — Add a new patient  
GET `/api/patients/` — Get all patients that belong to the logged-in user  
GET `/api/patients/<id>/` — Look up a specific patient  
PUT `/api/patients/<id>/` — Update a patient’s info  
DELETE `/api/patients/<id>/` — Remove a patient

### Doctors (Authentication Required)

POST `/api/doctors/` — Add a doctor  
GET `/api/doctors/` — List all doctors  
GET `/api/doctors/<id>/` — View one doctor  
PUT `/api/doctors/<id>/` — Update doctor details  
DELETE `/api/doctors/<id>/` — Delete a doctor

### Patient-Doctor Mappings (Authentication Required)

POST `/api/mappings/` — Assign a doctor to a patient  
GET `/api/mappings/` — See all doctor-patient pairs  
GET `/api/mappings/<patient_id>/` — View all doctors for a patient  
DELETE `/api/mappings/<id>/` — Unassign a doctor from a patient

## Example Request Bodies

### Register

{
"name": "John Doe",
"email": "john@example.com",
"password": "securepassword123"
}

### Login

{
"email": "john@example.com",
"password": "securepassword123"
}

### Add a Patient

{
"name": "Jane Smith",
"age": 30,
"gender": "Female",
"contact": "9876543210",
"address": "Hyderabad
}

### Add a Doctor

{
"name": "Dr. Alan Park",
"specialization": "Cardiology",
"contact": "9876543211",
"email": "dr.alan@hospital.com"
}

### Assign a Doctor to a Patient

{
"patient": 1,
"doctor": 1
}

## Auth Header

For any protected endpoint, toss your JWT token in the Authorization header, like this:
Authorization: Bearer <access_token>
