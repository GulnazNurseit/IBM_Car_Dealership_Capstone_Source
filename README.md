# Car Dealership Review Portal — IBM Full Stack Capstone

An original implementation starter for the IBM full-stack capstone. Includes Django (user accounts, car makes/models, Django templates and proxy API), React frontend, Express + MongoDB dealer/review API, sentiment service, Docker Compose, and CI workflow.

**Status:** Source project prepared; not deployed. CI workflow is configured but has not executed on GitHub. No browser screenshots, live deployment URL or verified student lab completion are included. Screenshots must be captured from the running app, not fabricated.

## Local startup (Docker recommended)
```bash
docker compose up --build
```
Open http://localhost:8000/ for Django pages, http://localhost:5173/ for the React app, http://localhost:3000/fetchDealers for Express API, and http://localhost:5000/analyze/great for sentiment. Start the Docker daemon before running. Sample dealers and initial reviews are seeded into MongoDB at startup.

Create admin user:
```bash
docker compose exec django python manage.py createsuperuser
```
Login and register are supported by Django sessions and CSRF verification. The site can be used with the Django templates alone; the React client is an additional UI.

## Without Docker
Install Python 3.11+, Node 20+, MongoDB. In `server` run `pip install -r requirements.txt`, `python manage.py migrate`, `python manage.py runserver`. In `services/dealers` run `npm install && npm start` (set `MONGO_URL`), in `services/sentiment` run `pip install -r requirements.txt && python app.py`, and in `frontend` run `npm install && npm run dev`. Set service URLs in `.env` or use Docker.

## Course evidence checklist
See `SUBMISSION_GUIDE.md` for the exact filenames to capture. GitHub public URL, GitHub Actions screenshots, deployment URL and live app screenshots require your account access and an actual deployment. Do not claim those items are complete until checked.

## Security notes
Local debug setup is for coursework, not production. Set a strong `DJANGO_SECRET_KEY`, disable `DJANGO_DEBUG` and configure `DJANGO_ALLOWED_HOSTS`, CSRF origins and TLS when deploying. Default sample content is fictional. No IBM Watson service credentials are included; sentiment uses an explicitly labeled local heuristic service.
