
# 📌 Client Favorites API

API RESTful para cadastro de clientes e seus produtos favoritos, com integração a uma API externa de produtos.

---

## ✅ Tecnologias utilizadas

- **Python 3.12**
- **FastAPI**
- **SQLAlchemy**
- **Alembic (Migrations)**
- **PostgreSQL 16**
- **Docker / Docker Compose**
- **aiohttp (para requisição externa de produtos)**

---

## ✅ Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ✅ Configuração do projeto

O projeto já vem com um `docker-compose.yml` que orquestra:

- Banco de dados PostgreSQL
- API FastAPI

---

## ✅ Variáveis de Ambiente

As principais configurações estão definidas diretamente no `.env`.  
A variável mais importante é:

| Variável | Valor |
|---|---|
| `DATABASE_URL` | `postgresql+psycopg2://postgres:postgres@db:5432/client_favorites` |
| `SECRET_KEY` | `super-secret` |

---

## ✅ Como rodar o projeto

### 🚀 Primeira vez (build + run + migrations):

```bash
make build/run
make migrations
make logs
```

### ✅ Ou, se quiser tudo em um só comando (recomendado):

```bash
make services/run
```

Esse comando vai:

1. Subir os containers
2. Aplicar todas as migrations do Alembic
3. Exibir os logs da API ao vivo

---

## ✅ Comandos úteis (Makefile)

| Ação | Comando |
|---|---|
| Subir os containers | `make run` |
| Subir e fazer rebuild | `make build/run` |
| Parar o projeto | `make stop` |
| Reiniciar | `make restart` |
| Criar uma nova migration | `make migrate msg="mensagem da migration"` |
| Aplicar as migrations pendentes | `make migrations` |
| Ver logs da API | `make logs` |

---

## ✅ Testando a API

A API sobe por padrão em:

```
http://localhost:8000
```

Swagger/OpenAPI disponível em:

```
http://localhost:8000/docs
```

---