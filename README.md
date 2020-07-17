# fst_backend
Backend api for FST App


# Fork and Clone
Fork and clone the repository
```
git clone https://github.com/YOUR_USERNAME_GOES_HERE/fst_backend.git
```

# Database Setup

### Install Postgres

Go to https://www.postgresql.org/

### Login to postgres

- On Ubuntu
```
sudo -i -u postgres
```

- On Windows
```
psql -U postgres
```

### Run postgresSQL (Only Ubuntu otherwise skip this step)
```
psql
```

###  Create Database
```
CREATE DATABASE fstapp;
```

### Create User
```
CREATE USER fst_admin WITH PASSWORD 'fstAPP2020';
```

### Alter roles
```
ALTER ROLE fst_admin SET client_encoding TO 'utf8';
ALTER ROLE fst_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE fst_admin SET timezone TO 'UTC';
```

###  Grant Privileges
```
GRANT ALL PRIVILEGES ON DATABASE fstapp TO fst_admin;
```

### Quit
```
\q
```

# Installing  Django

### Install  virtualenv with pip
```
pip install virtualenv
```
###  Change directory to project
```
cd  fst_backend
```
###  Create virtual  environment
```
virtualenv venv -p python3
```

### Activate virtual environment

- On Unix (Mac/Linux)
```
source venv/bin/activate
```
- On  Windows
```
venv\Scripts\activate
```

### Install requirements
```
pip  install -r requirements.txt
```

### Change directory to src folder
```
cd src
```

### Migrate Database
```
python manage.py migrate
```
### Create a superuser
```
python manage.py createsuperuser
```

### Start the server
```
python manage.py runserver
```

###  Go to browser and login  with  username and password created  with superuser

http://127.0.0.1:8000/admin





