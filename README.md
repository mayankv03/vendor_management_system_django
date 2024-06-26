
# Vendor Management System

## Overview

Vendor Management System is a Django-based web application designed to manage vendors and purchase orders. It includes features for handling vendor details, tracking purchase orders, and calculating performance metrics such as on-time delivery rate and quality rating average.

## Features

- CRUD operations for Vendors and Purchase Orders
- API endpoints for integration with other systems
- Performance metrics calculation for vendors
- Token-based authentication using JWT
- Static files for frontend styling and scripts
- Template rendering for views

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/mayankv03/vendor_management_system_django.git
   cd vendor_management_system_django
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the Django project**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**

   Open a web browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure

```
vendor_management_system/
├── vendor_management_system/
│   ├── __init__.py
│   └── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── vendors/
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api.py
│   │   ├── test_models.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   └── signals.py
│   ├── urls.py
│   ├── views.py
├── manage.py
└── requirements.txt
└── README.md
```

## API Endpoints

### Vendor Endpoints

- **POST /api/vendors/**: Create a new vendor
- **GET /api/vendors/**: List all vendors
- **GET /api/vendors/{id}/**: Retrieve a vendor by ID
- **PUT /api/vendors/{id}/**: Update a vendor by ID
- **DELETE /api/vendors/{id}/**: Delete a vendor by ID

### Purchase Order Endpoints

- **POST /api/purchase_orders/**: Create a new purchase order
- **GET /api/purchase_orders/**: List all purchase orders
- **GET /api/purchase_orders/{po_id}/**: Retrieve a purchase order by ID
- **PUT /api/purchase_orders/{po_id}/**: Update a purchase order by ID
- **DELETE /api/purchase_orders/{po_id}/**: Delete a purchase order by ID

### Vendor Performance Endpoints

- **GET /api/vendors/{vendor_id}/performance**: Retrieve a vendor's performance
metrics.
- **POST /api/purchase_orders/{po_id}/acknowledge**: Update acknowledgment_date and trigger the recalculation
of average_response_time

### Authentication

- **POST /api/token/**: Obtain a new JWT token
- **POST /api/token/refresh/**: Refresh an existing JWT token

## Running Tests

To run tests, use the Django management command:

```bash
python manage.py test
```

This will execute all tests in the `vendors/tests/` directory.


## Contact

For any questions or feedback, please contact:

- Name: Mayank Vishwakarma
- Email: mayankat03@gmail.com