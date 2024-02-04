# Variables

DEFAULT_COLOR=\e[0m

BLUE=\e[34m

YELLOW=\033[33m

DOCKER_CONTAINER_NAME=furniture_shop.api


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



# CI Tests

ci_lint:
	flake8 --config setup.cfg src tests

ci_typechecks:
	mypy --config setup.cfg src tests

ci_unittests:
	pytest -s tests/unit

ci_integration_tests:
	poetry run pytest -s tests/integration


# Tests

black:
	poetry run black . -l 79

lint:
	poetry run flake8 --config setup.cfg src tests

typechecks:
	poetry run mypy --config setup.cfg src tests

unittests:
	poetry run pytest -s tests/unit

integration_tests:
	$(call docker_exec,poetry run pytest -s tests/integration)


# todo: add coverage

test: lint typechecks unittests integration_tests
