# Break Control System

A lightweight break time tracking system built for real operational use in a company environment.

The application was designed to help supervisors and operators register employee break start and end times quickly, without requiring a server, database setup, or complex installation process.

## Project Context

This system was created for a company that needed a practical way to monitor employee breaks during daily operations. The goal was to provide a simple, reliable, browser-based tool that could be used by real users on-site with minimal setup.

The project is intentionally maintained as a single-page application because the current business requirement is focused: record breaks, display history, protect operator actions, and export records for review.

## Features

- Employee selection
- Break start registration
- Break end registration
- Local break history
- Operator login for protected actions
- Report export
- Local browser storage using `localStorage`
- Python logic running in the browser through Pyodide

## How To Use

Open `index.html` in a web browser.

Pyodide is loaded through a CDN, so an internet connection is required during the first load.

## Current Structure

```text
break-control-system/
├── index.html
├── README.md
├── LICENSE
└── .gitignore
```

## Why The Project Is Simple

The repository is intentionally small because the production version of the tool is a single-page application. Keeping only the files that are actually needed makes the project easier to review, maintain, and deploy.

If the system grows in the future, the project can be expanded with a backend, database, authentication service, and centralized reporting.

## License

MIT
