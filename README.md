# Optimal Solar Panel Selection System

## Description
The Optimal Solar Panel Selection System helps users choose the best solar panels based on their energy needs. It provides insights into panel specifications, costs, and allows for direct purchases, making it a comprehensive solution for solar energy selection and management.

## Features

- User-friendly interface for selecting solar panels based on energy requirements.
- Price comparisons and product specifications.
- Purchase and payment integration.
- Admin panel for managing products and user activity.

## Tech Stack
- Django
- SQLite 
- Bootstrap (for styling)
- JavaScript and jQuery (for interactivity)
 
 ## Installation

Clone the repository:
   ```bash
   git clone https://github.com/yourusername/project-name.git

 # Navigate into the project directory:
cd project-name

#Create a virtual environment:
python -m venv venv

#Activate the virtual environment
venv\Scripts\activate

#Install the required packages:
pip install -r requirements.txt

#Run migrations:
python manage.py migrate


```

## Usage

### Starting the Application
After following the installation steps, run the development server using:

```bash
python manage.py runserver
```

### Accessing the Web Interface
The application consists of several main pages:

Home Page: Shows a welcome message and an overview of the app’s purpose.

Solar Panel Selection Page: Navigate here to select panels based on energy requirements.

Order Confirmation Page: After selecting a panel, confirm your order on this page.

Admin Panel: If you’re an admin, log in at http://localhost:8000/admin to manage the site’s content.

### Demo Login Credentials
To explore the app without creating a new user account, use the demo credentials below:

Username: demo_user
Password: demo_password
### Main Actions
Select a Solar Panel: Browse and select from available panels based on your energy requirements.

Place an Order: Confirm your choice and place an order, which will prompt a confirmation message.

Admin Management: If logged in as an admin, add, edit, or remove products and monitor user activity.

## Project Structure
focus/
├── intro/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── intro/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
├── templates/
├── static/
├── manage.py
└── README.md

## API Documentation
- **GET /api/panels/**: Retrieves a list of available solar panels.
- **POST /api/order/**: Places an order for a selected panel.



