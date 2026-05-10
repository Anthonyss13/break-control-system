# Break Control System

Sistema simples de controle de break para colaboradores.

Este projeto foi criado para uma empresa que precisava registrar o inicio e o fim dos breaks da equipe em uma tela rapida, sem instalacao complexa e sem depender de um backend.

## O que o sistema faz

- seleciona o colaborador;
- registra inicio do break;
- registra retorno do break;
- mostra o historico de registros;
- protege exportacao e limpeza do historico com login de operador;
- salva os dados localmente no navegador;
- exporta relatorio para conferencia.

## Como usar

Abra o arquivo `index.html` no navegador.

O sistema usa Pyodide via CDN para executar a logica em Python dentro do navegador. Por isso, no primeiro carregamento, e preciso estar conectado a internet.

## Estrutura atual

```text
break-control-system/
├── index.html
├── README.md
├── LICENSE
└── .gitignore
```

## Observacao

Esta versao foi mantida propositalmente simples porque a aplicacao principal esta toda no `index.html`. Se no futuro o projeto precisar salvar dados em servidor, autenticar usuarios reais ou gerar relatorios centralizados, a estrutura pode crescer novamente com backend e banco de dados.

## Licenca

MIT
