# Fluxo do Sistema

## Cenario principal

1. O operador abre a tela `frontend/index.html`.
2. Seleciona o colaborador no campo Employee.
3. Clica em Start break para registrar o inicio da pausa.
4. Clica em End break quando o colaborador retorna.
5. O registro aparece no historico com nome, tipo, data e hora.
6. O operador faz login para exportar relatorio ou limpar o historico.

## Fluxo atual do frontend

```text
Usuario
  -> seleciona colaborador
  -> aciona inicio/fim
  -> Python via Pyodide cria registro
  -> localStorage salva historico
  -> tabela renderiza registros
  -> operador exporta/limpa quando autenticado
```

## Fluxo futuro com backend

```text
Frontend
  -> POST /api/breaks
  -> Backend Flask valida dados
  -> SQLite armazena registro
  -> GET /api/breaks atualiza historico
  -> relatorios podem ser gerados no servidor
```

## Regras de negocio

- Todo registro precisa de colaborador.
- O tipo do registro deve ser inicio ou fim do break.
- Acoes administrativas devem exigir operador autenticado.
- Historico deve preservar data e hora do evento.
