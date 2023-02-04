include .env
include app.mk


export
.PHONY: up down stop prune ps shell drush logs bash extract

default: dw-up

bash:
	docker exec -ti $(PROJECT_NAME)_app /bin/bash

# $(filter-out $@,$(MAKECMDGOALS))
	
build:
	@echo "Stopping containers for $(PROJECT_NAME)..."
	@docker-compose -f docker/dw/docker-compose.yml build

airflow-init:
	@echo "Initializing airflow for $(PROJECT_NAME)"
	@docker-compose -f docker/airflow/docker-compose.yml up airflow-init

airflow-up:
	@echo "Stopping airflow for $(PROJECT_NAME)"
	@docker-compose -f docker/airflow/docker-compose.yml up -d

airflow-stop:
	@echo "Stopping airflow for $(PROJECT_NAME)"
	@docker-compose -f docker/airflow/docker-compose.yml stop

dw-up:
	@echo "Starting up  DataWarehouse containers for $(PROJECT_NAME)"
	@docker-compose -f docker/postgres/docker-compose.yml up -d

dw-kill:
	@echo "Stopping DataWarehouse containers for $(PROJECT_NAME)..."
	@docker-compose -f docker/postgres/docker-compose.yml kill

dw-stop:
	@echo "Stopping DataWarehouse containers for $(PROJECT_NAME)..."
	@docker-compose -f docker/dw/docker-compose.yml stop

logs:
	@echo "Stopping containers for $(PROJECT_NAME)..."
	@docker-compose -f docker/dw/docker-compose.yml logs -f

prune:
	@echo "Removing containers for $(PROJECT_NAME)..."
	@docker-compose -f docker/postgres/docker-compose.yml down -v

flyway-migrate:
	@echo "Starting Flyway container for database migration"
	@docker-compose -f docker/flyway/docker-compose.yml -f docker/flyway/docker-compose-migrate.yml up

flyway-info:
	@echo "Starting Flyway container for details and status information about migrations"
	@docker-compose -f docker/flyway/docker-compose.yml -f docker/flyway/docker-compose-info.yml up

flyway-baseline:
	@echo "Starting Flyway container to baseline your DB"
	@docker-compose -f docker/flyway/docker-compose.yml -f docker/flyway/docker-compose-baseline.yml up

flyway-validate:
	@echo "Starting Flyway container to baseline your DB"
	@docker-compose -f docker/flyway/docker-compose.yml -f docker/flyway/docker-compose-validate.yml up

flyway-repair:
	@echo "Starting Flyway container to baseline your DB"
	@docker-compose -f docker/flyway/docker-compose.yml -f docker/flyway/docker-compose-repair.yml up

update-requirements:
	pip freeze > requirements.txt