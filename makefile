# Variables

DEFAULT_COLOR=\e[0m

BLUE=\e[34m

YELLOW=\033[33m

DOCKER_CONTAINER_NAME=api


# Functions

define docker_exec
	docker exec -it ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
endef


# Run

run:
	docker compose up --build


# Migrations

migrations:
	$(call docker_exec,cd src && poetry run echo "hi")

migrate:
	$(call docker_exec,cd src && poetry run echo "hi")


# Restart | Down

restart:
	docker compose restart

down:
	docker compose down

clean:
	docker compose down -v


# Tests | You can run tests only if you have previously run container

black:
	poetry run black . -l 79

lint:
	poetry run flake8 --config setup.cfg src tests

types:
	poetry run mypy --config setup.cfg src tests

unittests:
	$(call docker_exec,poetry run pytest -s tests)

coverage:
	$(call docker_exec,cd src && poetry run coverage run --rcfile ../setup.cfg main.py && poetry run coverage report --rcfile ../setup.cfg)

test: lint types coverage unittests
