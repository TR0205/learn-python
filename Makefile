install:
	@make build
	@make up
build:
	docker compose build
ps:
	docker compose ps
up:
	docker compose up -d
stop:
	docker compose stop
down:
	docker compose down --remove-orphans
down-v:
	docker compose down --remove-orphans --volumes
restart:
	@make down
	@make up
py:
	docker compose exec python bash
