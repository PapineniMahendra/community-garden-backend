# 🌱 Community Gardening App

A Django REST Framework backend for organizing and managing community gardening events. This project allows users to register, join gardening events, comment, and receive updates—all via a clean RESTful API.

---

## 🚀 Features

- ✅ User Registration & JWT Authentication
- ✅ User Profiles with Skills & Bio
- ✅ Create, View, Edit, and Cancel Gardening Events
- ✅ Join or Leave Events (with Capacity Enforcement)
- ✅ Comment on Event Pages
- ✅ Event Notifications API
- ✅ Weather Forecast Integration (optional)
- ✅ Role-Based Permissions (Organizer/Admin/Participant)
- ✅ Swagger API Docs
- ✅ Token-based Authentication using JWT

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (can switch to PostgreSQL)
- **Auth**: JWT (via `djangorestframework-simplejwt`)
- **Docs**: Swagger (`drf-yasg`)
- **Extras**: Django Signals, Custom Permissions, Filters

---

## 📂 Project Structure

community_garden/
├── garden/ # Main Django app
│ ├── models.py # UserProfile, Event, Participation, Comment
│ ├── views.py # API views (ViewSets + ProfileView)
│ ├── serializers.py # DRF serializers
│ ├── permissions.py # Custom permission classes
│ ├── filters.py # Event filters
│ ├── urls.py # App-specific routes
│ ├── signals.py # Auto-create profiles & notifications
│ ├── utils/ # weather.py, notifications.py
│ └── tests/ # Unit tests
├── community_garden/ # Django project config
├── media/ # Uploaded images (profile/event)
├── templates/ # Swagger UI templates
├── static/ # Optional static files
├── manage.py
├── requirements.txt
├── .env # Secret keys and environment variables
├── README.md
└── openapi_schema.yml

yaml
Copy
Edit

---

## 🧪 Setup Instructions

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/yourusername/community-garden-app.git
cd community-garden-app
2. 🧰 Create Virtual Environment & Activate
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
3. 📦 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. 🗄️ Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. 👤 Create a Superuser
bash
Copy
Edit
python manage.py createsuperuser
6. 🚀 Run the Server
bash
Copy
Edit
python manage.py runserver
Now go to:

Admin Panel: http://127.0.0.1:8000/admin/

Swagger API: http://127.0.0.1:8000/swagger/

🔐 Authentication
Obtain token:
POST /api/token/
Body:

json
Copy
Edit
{
  "username": "yourusername",
  "password": "yourpassword"
}
Use returned access token in all requests:
Header:

makefile
Copy
Edit
Authorization: Bearer <access_token>
📬 API Endpoints (Examples)
Endpoint	Method	Description
/api/token/	POST	Login & get JWT token
/api/token/refresh/	POST	Refresh JWT
/api/profile/	GET/PUT	View or update user profile
/api/events/	GET/POST	List or create events
/api/events/<id>/join/	POST	Join or leave event
/api/events/<id>/comments/	GET/POST	Comment on an event
/api/notifications/	GET	Get notifications

🧪 Running Tests
bash
Copy
Edit
python manage.py test
📄 Environment Variables (.env)
ini
Copy
Edit
SECRET_KEY=your-django-secret-key
DEBUG=True
✅ Since you're using SQLite, DB credentials are not needed.

🧼 Code Quality
Follows PEP8

Modularized app with serializers, permissions, filters, and signals

RESTful conventions

JWT + Role-based permissions

Swagger documentation
