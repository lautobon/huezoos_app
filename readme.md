# Requerimientos:
- Python 3.9.13
- pip 23.1
- MySql


# Instalar ambiente virtual para trabajar con Django
```sh
pip install virtualenv
```

# Crear ambiente virtual
```sh
virtualenv <nombre>
```

# Activar ambiente virtual
```sh
source <nombre>/Scripts/activate
```

# Instalar dependencias

Desde la terminal en el root del proyecto ejecutamos:

```sh
pip install -U -r ./requirements.txt
```
# Variables locales

Crear en la carpeta huezoos_app un archivo `.env` con las siguientes variables:

```sh
DB_NAME=<DB_NAME>
DB_USER=<DB_USER>
DB_PASSWORD=<DB_PASSWORD>
DB_HOST=<DB_HOST>
DB_PORT=<DB_PORT>
SECRET_KEY=<DJANGO_SECRET_KEY>
```

# Crear bd

```sh
CREATE DATABASE huezoos_db;
```

# Iniciar bd

```sh
python manage.py makemigrations
python manage.py migrate 
```

# Popular bd

```sh
python manage.py loaddata ./fixtures/species.json
python manage.py loaddata ./fixtures/races.json
```

# Iniciar app local

```sh
python manage.py runserver
```