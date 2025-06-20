
# API - Instruções de Uso

Este documento explica como utilizar as principais rotas da API para gerenciamento de clientes e favoritos. Caso tenha o postman e prefira, existe uma collection no arquivo 'client-favorites-api.postman_collection.json' com todos as rotas e exemplos configurados.

---

## Fluxo Básico de Uso da API

### 1. Criar uma Conta de Cliente (Signup)

**Endpoint:**

```
POST /api/auth/signup
```

**Payload JSON:**

```json
{
  "name": "Cyro",
  "email": "cyro@email.com",
  "password": "123456"
}
```

**Exemplo com cURL:**

```bash
curl -X POST http://localhost:8000/api/auth/signup -H "Content-Type: application/json" -d '{"name":"Cyro","email":"cyro@email.com","password":"123456"}'
```

---

### 2. Realizar Login (Obter Token JWT)

**Endpoint:**

```
POST /api/auth/token
```

**Content-Type:** `application/x-www-form-urlencoded`

**Payload:**

| Campo     | Valor          |
|-----------|----------------|
| username  | cyro@email.com |
| password  | 123456         |

**Exemplo com cURL:**

```bash
curl -X POST http://localhost:8000/api/auth/token -H "Content-Type: application/x-www-form-urlencoded" -d "username=cyro@email.com&password=123456"
```

**Resposta Esperada:**

```json
{
  "access_token": "seu_token_jwt_aqui",
  "token_type": "bearer"
}
```

---

### 3. Adicionar um Produto aos Favoritos do Cliente

**Endpoint:**

```
POST /api/clients/{client_id}/favorites
```

**Headers necessários:**

```
Authorization: Bearer {seu_token_jwt}
```

**Exemplo:**

```bash
curl -X POST http://localhost:8000/api/clients/1/favorites -H "Authorization: Bearer seu_token_jwt_aqui" -H "Content-Type: application/json" -d '{"product_id": 1}'
```

---

### 4. Listar os Favoritos de um Cliente

**Endpoint:**

```
GET /api/clients/{client_id}/favorites
```

**Headers necessários:**

```
Authorization: Bearer {seu_token_jwt}
```

**Exemplo:**

```bash
curl -X GET http://localhost:8000/api/clients/1/favorites -H "Authorization: Bearer seu_token_jwt_aqui"
```

**Resposta Esperada:**

```json
[
  {
    "id": 1,
    "client_id": 1,
    "product_id": 1
  }
]
```

---

## Observações importantes:

✅ Todas as rotas que manipulam favoritos requerem autenticação JWT.

✅ O token deve ser incluído no header **Authorization** como **Bearer Token**.

✅ Para facilitar os testes locais, as portas padrão são:
- **API:** `http://localhost:8000`
- **Banco:** PostgreSQL na porta `5432`
