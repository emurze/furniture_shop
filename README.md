# Furniture Shop

### Docs

* Pydantic

* SqlAlchemy

### Clean Architecture and DDD


### Env example

.env/.app.env

```text
PROJECT_TITLE = furniture_shop
SECRET_KEY = )t*wypdmr7l!&m$@sn*-n8s5g*z-skhiu3n%q@6m7p6t&x_f9
LOG_LEVEL = info

WORKDIR = /service/

DB_NAME = learning
DB_USER = adm1
DB_PASS = 12345678
DB_HOST = ${PROJECT_TITLE}.db
DB_PORT = 5432

TEST_DB_NAME = test_learning
TEST_DB_USER = test_adm1
TEST_DB_PASS = 12345678
TEST_DB_HOST = ${PROJECT_TITLE}.db
TEST_DB_PORT = 5432
```

.env/.db.env

```text
POSTGRES_DB = learning
POSTGRES_USER = adm1
POSTGRES_PASSWORD = 12345678

TEST_POSTGRES_DB = test_learning
TEST_POSTGRES_USER = test_adm1
TEST_POSTGRES_PASSWORD = 12345678
```

.env/.pgadmin.env

```text
PGADMIN_DEFAULT_EMAIL = adm1@adm1.com
PGADMIN_DEFAULT_PASSWORD = 12345678
```
