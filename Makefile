

run:
	docker-compose up -d
	
build/run:
	docker-compose up -d --build

services/run:
	run
	migrations
	docker-compose logs -f api

stop:
	docker-compose down

restart: stop run

migrate:
	docker-compose exec api alembic revision --autogenerate -m "$(msg)"

migrations:
	docker-compose exec api alembic upgrade head

logs:
	docker-compose logs -f api
	
test:
	ENV_FILE=.env.test docker-compose exec api pytest tests

services/test:
	docker-compose exec db psql -U postgres -c "CREATE DATABASE client_favorites_test;"
	ENV_FILE=.env.test docker-compose exec api alembic upgrade head
	test
