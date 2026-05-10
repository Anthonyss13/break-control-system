# Break Control System

A break time tracking system developed for a company that needed a simple and organized way to register, monitor, and export employee break records.

The project started as a lightweight web interface that allows operators to register break start and end times, maintain local history records, and export reports. The repository structure also includes a Flask backend foundation to evolve the system into a centralized API with an SQLite database.

## Objective

Companies with shift-based teams need to track when each employee starts and finishes their break. This system helps operators to:

- select employees;
- register break start and end times;
- view daily history records;
- export reports;
- clear records using an operator password
- prepare the system for future API and database integration.

## Structure

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

## Current Features

- Responsive frontend built with HTML, CSS, and Python using Pyodide
- Local browser persistence using `localStorage`.
- Operator login for sensitive actions.
- History export to report files.
- Flask API foundation for record registration and queries.

## Running the Frontend

Open the file `frontend/index.html` in your browserr.

> Note: Pyodide is loaded through a CDN, so an internet connection is required during the first load.

## Running the Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

On Windows PowerShell:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

The API will be available at `http://localhost:5000`.

## Docker

```bash
docker compose up --build
```

## Suggested Roadmap

- Integrate the frontend with the Flask API..
- Add real operator authentication.
- Create a daily dashboard per employee.
- Generate CSV/XLSX reports on the backend.
- Add automated tests.
- Publish the interface using GitHub Pages or another static hosting service.

## License

This project is licensed under the MIT License MIT.
