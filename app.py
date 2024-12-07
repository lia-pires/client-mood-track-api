from api.v1.routes import v1_blueprint
from flask import Flask, jsonify, request


app = Flask(__name__)


app.register_blueprint(v1_blueprint)


@app.before_request
def handle_versioning():
    api_version = request.headers.get("API-Version", "v1")

    if api_version == "v1":
        request.url_rule.rule = f"/v1{request.url_rule.rule}"
    else:
        return jsonify({"error": "Invalid API version"}), 400
