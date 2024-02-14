# Variables

DEFAULT_COLOR = \e[0m

BLUE = \e[34m

YELLOW = \033[33m

PROJECT_TITLE = furniture_shop

DOCKER_CONTAINER_NAME = ${PROJECT_TITLE}.api


# Functions

define docker_exec
	docker exec -it ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
endef

define docker_row_exec
	docker exec ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
endef


# Run

run:
	docker compose up --build

restart:
	docker compose down
	docker compose up --build -d

down:
	docker compose down

clean:
	docker compose down -v


# Migrations

migrations:
	$(call docker_exec,poetry run alembic revision --autogenerate)

migrate:
	$(call docker_exec,poetry run alembic upgrade head)

row-migrate:
	poetry run alembic upgrade head


# Tests

black:
	poetry run black . -l 79 tests src

lint:
	poetry run flake8 --config setup.cfg src tests

typechecks:
	poetry run mypy --config setup.cfg src tests

unittests:
	poetry run pytest -s -v tests/unit

integration_tests:
	$(call docker_exec,cd tests/slow/integration && poetry run pytest -s -vv .)

e2e_tests:
	$(call docker_exec,cd tests/slow/e2e && poetry run pytest -s -vv .)

test: lint typechecks unittests integration_tests e2e_tests


# CI Tests

ci_lint:
	flake8 --config setup.cfg src tests

ci_typechecks:
	mypy --config setup.cfg src tests

ci_unittests:
	pytest -s tests/unit

ci_integration_tests:
	poetry run pytest -s tests/slow/integration

ci_e2e_tests:
	poetry run pytest -s tests/slow/e2e


# CLI Tests

cli_integration_tests:
	$(call docker_row_exec,cd tests/slow/integration && poetry run pytest -s -v .)

cli_e2e_tests:
	$(call docker_row_exec,cd tests/slow/e2e && poetry run pytest -s -v .)

cli_test: lint typechecks unittests restart cli_integration_tests cli_e2e_tests

git_add_all:
	git add .

pre-commit: black git_add_all cli_test
