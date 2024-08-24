FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV PYTHONUNBUFFERED=1
COPY . .

CMD ["gunicorn","--reload", "wsgi:app", "--bind", "0.0.0.0:3000", "--log-level", "debug"]