# Variables

DEFAULT_COLOR = \e[0m

BLUE = \e[34m

YELLOW = \033[33m

PROJECT_TITLE = furniture_shop

DOCKER_CONTAINER_NAME = ${PROJECT_TITLE}.api


# Functions

define docker_exec
	docker exec ${DOCKER_CONTAINER_NAME} bash -c "$(1)"
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
	poetry run isort
	poetry run black . -l 79

lint:
	poetry run flake8 --config setup.cfg src tests

typechecks:
	poetry run mypy --config setup.cfg src tests

unittests:
	poetry run pytest -s tests/unit

integration_tests:
	$(call docker_exec,poetry run pytest -s tests/integration)


cli_run_daemon:
	@docker compose up -d --build

cli_integration_tests: cli_run_daemon integration_tests down


# todo: add coverage

test: lint typechecks unittests integration_tests
