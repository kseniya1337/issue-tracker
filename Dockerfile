FROM python:3.6.4-alpine3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-dev musl-dev gcc jpeg-dev zlib-dev

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:80