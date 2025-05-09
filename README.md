# Remind Me Later API

A Django REST API for managing reminders. The API allows users to create reminders with a message, date, time, and a notification method (email or SMS).

## Features

- Create reminders with message, date, time, and notification method
- Validation for reminder dates (must be in the future)
- Support for different notification methods (currently email and SMS)
- Cancel pending reminders
- RESTful API design with proper error handling
- API documentation with Swagger and ReDoc

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/remind-me-later.git
cd remind-me-later
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

The API will be available at http://localhost:8000/api/v1/

### API Documentation

API documentation is available at:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## API Endpoints

### Reminders

- `GET /api/v1/reminders/` - List all reminders
- `POST /api/v1/reminders/` - Create a new reminder
- `GET /api/v1/reminders/{id}/` - Retrieve a specific reminder
- `DELETE /api/v1/reminders/{id}/` - Delete a reminder
- `POST /api/v1/reminders/{id}/cancel/` - Cancel a pending reminder

## Example Request

```json
POST /api/v1/reminders/
{
    "title": "Meeting with Team",
    "message": "Don't forget the team meeting at 2PM",
    "reminder_date": "2025-05-10",
    "reminder_time": "13:45:00",
    "notification_method": "email",
    "recipient": "user@example.com"
}
```



