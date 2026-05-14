# Metsenat Frontend Service

This is a standalone Next.js frontend service for the Metsenat backend API.

## Run frontend service

```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

Frontend runs on `http://localhost:3000`.

## Backend service requirement

Backend should run separately (second service) on `http://localhost:8000`.

```bash
python manage.py runserver
```

## Two-service architecture

- Service 1: `Metsenat` Django backend (API)
- Service 2: `frontend` Next.js app (UI)

The UI is connected to API endpoints under:

- `/api/v1/authentication/*`
- `/api/v1/users/*`
- `/api/v1/general/*`
- `/api/v1/appeals/*`
- `/api/v1/sponsors/*`
