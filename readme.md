# Django Internship Assignment Project

This project demonstrates backend skills using Django REST Framework, JWT authentication, Celery with Redis, and Telegram Bot integration.


## Features

- Public and Protected REST APIs
- JWT Authentication
- Background task handling with Celery and Redis
- Telegram Bot storing user data in Django DB
- Environment variables using `.env` with `python-decouple`

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2. Create Virtual Environment and Activate

python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Setup .env File
Create a .env file based on .env.example:

SECRET_KEY=your_actual_secret_key
DEBUG=True
TELEGRAM_BOT_TOKEN=your_actual_telegram_token