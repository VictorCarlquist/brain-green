FROM python:3.11-slim

# Env vars
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /srv
COPY . .

EXPOSE 8000

ARG PROJECT_NAME=BRAIN
ARG DATABASE_NAME=BRAIN
ARG DATABASE_USER=postgres
ARG DATABASE_PASSWORD=postgres
ARG DATABASE_HOST=localhost
ARG DATABASE_PORT=5432
ARG BRAIN_DATABASE_NAME=db
ARG BRAIN_DATABASE_PORT=5432
ARG BRAIN_DATABASE_USER=post
ARG BRAIN_DATABASE_PASSWORD=pass
ARG BRAIN_DATABASE_HOST=localhost
ARG PROJECT_HOST=BRAIN.BRAIN.io
ARG REDIS_DATABASE_URL=redis://localhost:6379/0
ARG SECRET_KEY=secret

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "-c", "./backend/gunicorn.py", "backend.wsgi"]
