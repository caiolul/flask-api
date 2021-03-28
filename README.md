# Flask Api

## Study flask

Create containers

```sh
docker run --name name_container -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

```

Run project

Install dependencies from poetry

```sh
poetry install
```

- Windowns (cmd)

```sh
set FLASK_APP=src\app.py

set FLASK_ENV=development
```

Run database

```sh
flask db upgrade
```
