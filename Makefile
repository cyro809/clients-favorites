

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