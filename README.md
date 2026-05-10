# Break Control System

Sistema de controle de ponto de break criado para uma empresa que precisava registrar, acompanhar e exportar pausas dos colaboradores de forma simples e organizada.

O projeto nasceu como uma interface web leve para operadores registrarem entrada e saida de break, manterem historico local e exportarem relatorios. A estrutura do repositorio tambem inclui uma base de backend em Flask para evoluir o sistema para uma API centralizada com banco SQLite.

## Objetivo

Empresas com equipes em turno precisam saber quando cada colaborador inicia e finaliza o break. Este sistema ajuda o operador a:

- selecionar o funcionario;
- registrar inicio e fim do break;
- consultar o historico do dia;
- exportar relatorio;
- limpar registros com senha de operador;
- preparar uma futura integracao com API e banco de dados.

## Estrutura

```text
break-control-system/
├── backend/
│   ├── app.py
│   ├── database/
│   ├── routes/
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── assets/
├── screenshots/
├── docs/
│   ├── system-flow.md
│   └── api.md
├── .gitignore
├── README.md
├── LICENSE
└── docker-compose.yml
```

## Funcionalidades atuais

- Frontend responsivo em HTML, CSS e Python via Pyodide.
- Persistencia local no navegador usando `localStorage`.
- Login de operador para acoes sensiveis.
- Exportacao de historico para arquivo de relatorio.
- Base de API Flask para cadastro e consulta de registros.

## Como executar o frontend

Abra o arquivo `frontend/index.html` no navegador.

> Observacao: o Pyodide e carregado via CDN, entao o navegador precisa de internet no primeiro carregamento.

## Como executar o backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

No Windows PowerShell:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

A API ficara disponivel em `http://localhost:5000`.

## Docker

```bash
docker compose up --build
```

## Roadmap sugerido

- Integrar o frontend com a API Flask.
- Adicionar autenticacao real de operador.
- Criar dashboard diario por colaborador.
- Gerar relatorios CSV/XLSX no backend.
- Adicionar testes automatizados.
- Publicar a tela em GitHub Pages ou outro hosting estatico.

## Licenca

Este projeto esta sob a licenca MIT.
