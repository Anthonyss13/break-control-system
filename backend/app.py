from flask import Flask, jsonify
from flask_cors import CORS

from database.db import init_db
from routes.breaks import breaks_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()
    app.register_blueprint(breaks_bp, url_prefix="/api")

    @app.get("/health")
    def health_check():
        return jsonify({"status": "ok", "service": "break-control-system"})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
