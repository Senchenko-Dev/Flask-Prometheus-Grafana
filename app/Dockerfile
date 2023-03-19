
FROM python:3.8-alpine

MAINTAINER Senchenko Nikita 'www.staif123@gmail.com'

RUN pip install --upgrade pip

RUN pip install Flask

RUN pip install prometheus-flask-exporter

RUN adduser -D myuser

USER myuser

WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["app.py"]
