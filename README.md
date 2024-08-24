# Flask app with two or mor databases conections

in the file setting, you find a  SQLALCHEMY_DATABASE_URI and SQLALCHEMY_BINDS.
SQLALCHEMY_DATABASE_URI this is for a set you principal databases like postgres o mysql and
SQLALCHEMY_BINDS you put other databses.

You need put in the models inside the class the word __bind_key__ wit the same work key from SQLALCHEMY_BINDS

For this example you have 

settings.py
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/db'
SQLALCHEMY_BINDS = {
        'cache': 'sqlite:///cache_task.db'
    }
```
a postgres and sqlite databases 

The models

internal/models/postgres/models.py
```python
class MyModelPostgres(db.Model):
    __tablename__ = 'otro'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
```
as you can see this is the noraml way but in the sencond databases

internal/models/sqlite/models.py
```python
class MyModleSqlite(db.Model):
    __bind_key__ = 'cache'
    __tablename__ = 'cache_memory'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
```
you need used *__bind_key__* and this value is the same in SQLALCHEMY_BINDS dictionary

so that it hoy made many conection with many databases only need put more in SQLALCHEMY_BINDS

## Task

Thin APP used flask schedule for run a task in with diferent schedule you find this in task.py
and handle_task.py

## Compile and run

To compile locally, run the following command

1. Install Virtualenv and activate it
```sh
$ virtualenv -p python3 venv
```
```sh
$ source venv/bin/activate
```
2. Install requirements.txt
```sh
$ pip3 install -r requirements.txt
```

3. run program
```shell
python wsgi.py
```

### docker compose 

For run docker compose use this comand

```shell
docker-compose up --build
```

## docs
whit swagger
http://localhost:3000/docs

## Technologies used

1. Python
2. Docker