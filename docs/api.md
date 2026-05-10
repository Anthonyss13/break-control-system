# API

Base URL local: `http://localhost:5000`

## Health check

```http
GET /health
```

Resposta:

```json
{
  "status": "ok",
  "service": "break-control-system"
}
```

## Listar registros

```http
GET /api/breaks
```

Resposta:

```json
[
  {
    "id": 1,
    "employee_name": "Anthony",
    "record_type": "start",
    "record_date": "2026-05-10",
    "record_time": "14:30:00",
    "created_at": "2026-05-10 14:30:00"
  }
]
```

## Criar registro

```http
POST /api/breaks
Content-Type: application/json
```

Corpo:

```json
{
  "employee_name": "Anthony",
  "record_type": "start"
}
```

`record_type` aceita `start` ou `end`.

Resposta:

```json
{
  "id": 1,
  "employee_name": "Anthony",
  "record_type": "start",
  "record_date": "2026-05-10",
  "record_time": "14:30:00"
}
```

## Limpar registros

```http
DELETE /api/breaks
```

Resposta:

```json
{
  "status": "cleared"
}
```
