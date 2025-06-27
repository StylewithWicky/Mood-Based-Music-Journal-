# Mood-Based-Music-Journal-
🎧 Mood-Based Music Journal 🎭
A full-stack web application that allows users to log their emotions, reflect through journaling, and receive personalized music recommendations based on their mood.
Built using React, Flask, JWT Authentication, and optionally integrates with external music APIs (like Spotify).

📸 Demo
Add a screenshot or video here when deployed

📁 Folder Structure
bash
Copy
Edit
Mood-Based-Music-Journal/
│
├── Backend/
│   ├── app.py
│   ├── models.py
│   ├── controllers/
│   ├── auth/
│   ├── config.py
│   ├── seed.py
│   └── requirements.txt
│
├── Frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── Css/
│   │   └── App.js
│   ├── package.json
│   └── README.md
│
├── README.md (this file)
🌐 Live Demo (optional)
🔗 Hosted on Render/Netlify/Vercel

🚀 Features
✅ User login/logout with secure JWT authentication

✅ Mood journaling form with dropdown + textarea

✅ Calendar for logging moods by date

✅ Glassmorphism UI design with responsive layout

✅ Song recommendation based on mood

✅ Spotify preview & redirect to full track

✅ Avatar-inspired anime aesthetic (optional)

🧠 Technologies Used
🔧 Backend
Flask

Flask SQLAlchemy

Flask-CORS

Flask-JWT-Extended

PostgreSQL or SQLite

Marshmallow (optional for serialization)

🎨 Frontend
React

Formik + Yup

Axios

CSS3 + Glass UI (custom styles)

React Router DOM

🧰 Installation & Setup
⚙️ Backend Setup
bash
Copy
Edit
cd Backend
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# Create DB and run seed data
flask db init
flask db migrate
flask db upgrade
python seed.py

# Start server
flask run
🖼 Frontend Setup
bash
Copy
Edit
cd Frontend
npm install
npm start
🔐 Authentication
🔑 Uses JWT tokens stored in localStorage

✅ Login form accepts email and password

✅ Protected routes show mood form only when token is valid

📬 API Endpoints
✅ POST /auth/login
Request: { "email": "...", "password": "..." }

Response: { "token": "..." }

✅ POST /moods
Logs a new mood entry.

json
Copy
Edit
{
  "mood": "Happy",
  "journal_entry": "I had a good day.",
  "user_id": 1,
  "emotion_type_id": 1
}
✅ GET /recommendation?mood=Happy
Returns a song recommendation:

json
Copy
Edit
{
  "song": "Good Life",
  "artist": "OneRepublic",
  "url": "https://open.spotify.com/track/...",
  "preview_url": "https://...",
  "cover_art": "https://link-to-album-cover.jpg"
}
🖼 UI Design
🎨 Avatar-inspired UI with glass cards

🎭 Mood selector & journal in a blur-glass container

📅 Calendar shown beside form

🎵 Song card with album art, preview, and Spotify link

📦 Environment Variables (optional for external APIs)
Create a .env file in your backend and include:

ini
Copy
Edit
SPOTIFY_CLIENT_ID=...
SPOTIFY_CLIENT_SECRET=...
JWT_SECRET_KEY=...
DATABASE_URL=sqlite:///moods.db
🚀 Deployment
✅ Render for Backend
Set build command: pip install -r requirements.txt

Set start command: gunicorn app:app

✅ Netlify/Vercel for Frontend
Use npm run build and connect to GitHub repo

🧪 Future Improvements
🌍 Internationalization & language selector

👥 User profile & mood history dashboard

📈 Mood graph / data visualization

💡 AI-generated journaling prompts

🙌 Author
StylewithWicky
Reach out on GitHub or LinkedIn

📄 License
MIT License © 2025










