USER="`id -u`:`id -g`"

run:
	@PWD=`pwd` docker compose up --wait -d 
	@docker compose logs -f app

requirements:
	docker compose exec app bash -c 'source .venv/bin/activate && pip install pip-tools && pip-compile requirements.in'

linting:
	black .

pytest:
	docker compose exec app bash -c 'source .venv/bin/activate && pytest'

freeze-requirements:
	docker compose exec app bash -c 'source .venv/bin/activate && pip freeze > requirements.txt'

logs-all:
	@docker compose logs -f

logs-redis:
	@docker compose logs -f redis

logs-worker:
	@docker compose logs -f worker worker-beat

stop:
	@docker compose stop

remove:
	@docker compose down -v

migration:
ifneq ($(name),)
	docker compose exec app bash -c 'source .venv/bin/activate && alembic revision -m $(name)'
else
	@echo "make migration name=<name>"
endif

migrate:
	docker compose exec app bash -c 'source .venv/bin/activate && alembic upgrade head'

migrate-down:
	docker compose exec app bash -c 'source .venv/bin/activate && alembic downgrade -1'

open-adminer:
	@open "http://localhost:3005/?pgsql=postgres&username=root"
