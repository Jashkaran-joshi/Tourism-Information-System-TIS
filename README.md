

# **Tourism-Information-System-TIS**

Voyageur is a dynamic and user-friendly travel web application built to simplify the process of exploring destinations, finding deals, and managing travel-related information. Whether you are a travel enthusiast or a casual traveler, Voyageur makes it easy to discover new places, check their prices, and plan your next adventure.
With its clean interface and robust backend, the project also focuses on making content management simple for admins, allowing quick updates to deals, news, and services without hassle.

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Testing](#testing)

## **Features**
- **Travel Deals**: View the latest travel deals with updated prices and offers.  
- **Services Overview**: Explore available travel services in a simplified layout.  
- **Travel News**: Stay informed with news and updates related to travel.  
- **Destination & Pricing**: Browse destinations and check their pricing easily.  
- **Feedback System**: Submit feedback to help improve the platform.  
- **Contact Us**: Users can directly reach out for inquiries or support.  
- **Admin-Friendly Management**: Admins can easily add, edit, and update travel-related data.  
- **User-Friendly Interface**: Simple navigation with a responsive design using HTML, CSS, JavaScript, and Bootstrap.  
- **Database Support**: Secure data handling with SQLite3 integration.  
- **Future Trip Planner**: (Planned) Allow users to plan entire trips including travel, hotels, and food options.

## **Technologies Used**
- **Backend**: Django (Python) v5.x, Django ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap v5.x (or any integrated UI libraries)
- **Database**: PostgreSQL v16.x (SQLite v3.x for development)
- **Version** Control: Git v2.x
- **Deployment**: Nginx v1.25.x, Gunicorn v21.x
- **Testing**: Django's built-in testing framework (Django 5.x)

## **Project Structure**
```
Tourism-Information-System-TIS/ Home/
│
├── manage.py               # Django project manager script
├── db.sqlite3              # SQLite database (development database)
│
├── about/                  # App handling About page content and logic
├── contact/                # App handling Contact Us page and inquiries
├── Home/                   # Main app managing the homepage/landing page
├── media/                  # Directory for user-uploaded media files
├── news/                   # App displaying travel-related news and updates
├── services/               # App showcasing available travel services
├── static/                 # Static files (CSS, JS, images, Bootstrap)
├── templates/              # HTML templates for all Django apps
└── travello/               # Core Django project configuration and settings
```


## **Installation**
Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/Jashkaran-joshi/Tourism-Information-System-TIS.git
cd Tourism-Information-System-TIS
cd Home
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure the Database**
Update the `DATABASES` configuration in `Home/settings.py` to match your database setup.

### **5. Apply Migrations**
```bash
python manage.py migrate
```

### **6. Create Superuser**
```bash
python manage.py createsuperuser
```

### **7. Run the Application**
```bash
python manage.py runserver
```
Visit `http://localhost:8000` to access the app.

## **Configuration**
Create a `.env` file for sensitive environment configurations:
```bash
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL=postgres://user:password@localhost:5432/your_db_name
```

Make sure to configure settings for production, including static files, security, and email backend.

## **Testing**
You can run the unit tests with Django's built-in testing framework:

```bash
python manage.py test
```

This will run all the tests located in the `tests.py` files of your Django apps.
