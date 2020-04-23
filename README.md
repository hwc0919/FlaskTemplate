# Flask Template

> A Flask Template

## Build Setup

### 1. Open folder in terminal
``` bash

# create virtual environment
> python -m venv venv

# activate virtual environment
> .\venv\scripts\activate     # in Windows
> source ./activate           # in Linux

# install dependencies
(venv) > pip install -r requirements.txt

```

### 2. Configure sample.env.json

### 3. Create database
``` bash
# create a database in mysql
> mysql -u root -p
> create database <dbname>;
```

### 4. Start flask server
``` bash
(venv) > set FLASK_APP=server.py
(venv) > flask shell
>>> db.create_all()
>>> exit()
(venv) > flask run
```