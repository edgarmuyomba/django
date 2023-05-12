FROM python:3.10.11-alpine
ENV PYTHONUNBUFFERED=1

RUN mkdir /tweetwave
COPY . /tweetwave
WORKDIR /tweetwave

EXPOSE 8000

RUN python -m pip install -r requirements.txt
RUN python manage.py migrate

# docker-compose up --build