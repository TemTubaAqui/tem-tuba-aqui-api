## TemTubaAqui API

### Requisitos

- Docker
- Docker Compose

### Setup com docker

- Clone o repositório
- Execute a aplicação usando uma das opções abaixo:
  - Docker:
    - `docker-compose up --build`
  - Ou Makefile:
    - `make dinfra`
    - `make server`

### Setup sem docker

- Clone o repositório
- #### Setup da venv (opcional)
  - `python -m venv venv`
  - `source venv/bin/activate`
- #### Instalação das dependências
  - `pip install -r requirements/dev.txt`
- #### Setup da infraestrutura (docker)
  - `docker compose up -d redis minio db --build`
  - ou
  - `make dinfra`
- #### Iniciar aplicação
  - `./no-docker.sh`

### Uso

A API estará disponível em `http://localhost:8000`

#### Credenciais do usuário root:

- email: `root@email.com`
- senha: `root`

#### Endpoints importantes:

- `/admin`: Django Admin (root user)
- `/api/v1/redoc`: Documentação da API utilizando `redoc`.
- `/api/v1/swagger`: Documentação da API utilizando `swagger`.
- `/api/v1/beaches`: Listagem de praias com informações de ataques

### Postman

O repositório possui um arquivo de collection do Postman. Para utilizá-lo, clique em `file > import` e selecione o arquivo `TTA.postman_collection.json` na raiz do repositório.
