# RaffCity
"RaffCity is a Progressive Web App (PWA) designed to simplify urban mobility. The application allows users to explore bus stops and points of interest in a city, save their favorite locations, and get notified when they are near a registered stop. The system uses GPS geolocation to detect the user's position in real time and display saved stops on an interactive map powered by Leaflet.js."

## Features
User registration and login with session management
- Interactive map powered by Leaflet.js and OpenStreetMap
- Real-time GPS geolocation to detect nearby stops
- Save and remove favorite bus stops from your profile
- Automatic notification when the user is near a registered stop
- Progressive Web App (PWA) — installable on any device
- Offline support via Service Worker
- Password reset via email

## Technologies
- Python — backend language
- Flask — web framework
- SQLite — database
- SQLAlchemy — ORM for database management
- Flask-Login — user session management
- Flask-Mail — email sending
- Flask-WTF — form validation
- Flask-Bootstrap — UI components
- Leaflet.js — interactive maps
- OpenStreetMap — map tiles
- HTML5, CSS3, JavaScript — frontend
- Service Worker — PWA and offline support

## Requirements
- Linux (Ubuntu 18.04 or later)
- Python 3.6 or later
- pip
- virtualenv

## Installation
1. Clone the repository:
git clone https://github.com/yourusername/RaffCity.git
cd RaffCity

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install the required dependencies:
pip install Flask Flask-Login Flask-SQLAlchemy "Flask-Migrate==3.1.0" Flask-Mail Flask-WTF Flask-Bootstrap email-validator python-dotenv PyJWT "dominate==2.6.0"

4. Configure the environment variables in the `.flaskenv` file:
FLASK_APP=raffcity.py
MAIL_SERVER=localhost
MAIL_PORT=25
MAIL_USE_TLS=1
MAIL_USERNAME=your@email.com
MAIL_PASSWORD=yourpassword

5. Initialize the database:
flask db init
flask db migrate -m "init"
flask db upgrade

6. Run the application:
flask run --host=localhost
```

7. Open your browser and navigate to:
http://localhost:5000


## Usage
1. Register a new account from the registration page
2. Log in with your credentials
3. Navigate to Explore to view the interactive map with your saved stops
4. To save a new stop, navigate to:
http://localhost:5000/location/<stop_name> and click the Save button
5. Navigate to Profile to view all your saved stops
6. To add a new stop to the database, run the following command from the terminal:
python3 << 'EOF'
from app import db
from app.models import Location
l = Location(name="Stop Name", latitude=40.000, longitude=14.000, body="Description", address="Address", city="City", country="Country")
db.session.add(l)
db.session.commit()
EOF
7. To view all stops in the database, open the file app.db with DB Browser for SQLite

## Author
- Raffaele Calcagno — GitHub
University of Naples Parthenope — Web Technologies 2024/2025
Professor: Raffaele Montella

## License
This project is licensed under the Apache 2.0 License.
