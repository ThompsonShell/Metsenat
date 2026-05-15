# Metsenat

## Backend service setup (Django)

1. Clone repository

```bash
git clone git@github.com:ThompsonShell/Metsenat.git
cd Metsenat
```

2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Configure backend environment

Rename `.env.example` to `.env` and set your values.

5. Apply migrations

```bash
python manage.py migrate
```

6. Run backend service

```bash
python manage.py runserver
```

Backend API URL: `http://localhost:8000/api/v1`

