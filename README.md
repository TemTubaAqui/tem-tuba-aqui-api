## TemTubaAqui API

### Requisitos

- Docker
- Docker Compose

### Setup

- Clone o repositório
- Execute a aplicação usando uma das opções abaixo:
  - Docker:
    - `docker-compose up --build`
  - Ou Makefile:
    - `make dinfra`
    - `make server`

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
