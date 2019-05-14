FROM python:3.6-alpine3.8
RUN apk add --no-cache --update musl-dev gcc postgresql-dev linux-headers build-base python-dev py-pip jpeg-dev zlib-dev
COPY requirements.txt /src/
WORKDIR /src/
RUN pip install -r requirements.txt
COPY issue_tracker /src/issue_tracker
COPY manage.py /src/manage.py
CMD uwsgi --http :80 --wsgi-file /src/issue_tracker/wsgi.py --processes 4
