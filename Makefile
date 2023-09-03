all: FORCE
	docker compose up --build

dall: FORCE
	docker compose up -d --build

db: FORCE
	docker compose up db --build

ddb: FORCE
	docker compose up -d db --build

infra: FORCE
	docker compose up redis minio db --build

dinfra: FORCE
	docker compose up -d redis minio db --build

worker: FORCE
	docker compose up worker --build

dworker: FORCE
	docker compose up -d worker --build

server: FORCE
	docker compose up server --build

dserver: FORCE
	docker compose up -d server --build

app: FORCE
	docker compose up server worker --build

dapp: FORCE
	docker compose up -d server worker --build

jupyter: FORCE
	docker compose exec server python manage.py shell_plus --notebook

migrations: FORCE
	docker compose exec server python manage.py makemigrations

migrate: FORCE
	docker compose exec server python manage.py migrate

clean: FORCE
	docker compose down

FORCE: ;