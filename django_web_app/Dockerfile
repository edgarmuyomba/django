FROM python:3.10.11-alpine
ENV PYTHONUNBUFFERED=1

RUN mkdir /django_web_app
COPY . /django_web_app
WORKDIR /django_web_app

EXPOSE 8000

RUN python -m pip install -r requirements.txt
RUN python manage.py migrate