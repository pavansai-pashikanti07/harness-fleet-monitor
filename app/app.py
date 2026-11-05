import os
import socket
from datetime import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Application Configuration from Environment Variables
APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "Development")
APP_COLOR = os.getenv("APP_COLOR", "#10b981")  # Default: Vibrant Emerald Green
DEPLOYED_BY = os.getenv("DEPLOYED_BY", "Harness CD")

# In-memory flag to simulate failure for testing Harness Auto-Rollback
is_healthy = True

@app.route("/")
def index():
    hostname = socket.gethostname()
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    return render_template(
        "index.html",
        version=APP_VERSION,
        environment=APP_ENVIRONMENT,
        color=APP_COLOR,
        hostname=hostname,
        server_time=server_time,
        client_ip=client_ip,
        deployed_by=DEPLOYED_BY,
        healthy=is_healthy
    )

@app.route("/healthz")
def healthz():
    """Kubernetes liveness and readiness probe endpoint."""
    if is_healthy:
        return jsonify({
            "status": "UP",
            "version": APP_VERSION,
            "environment": APP_ENVIRONMENT,
            "hostname": socket.gethostname()
        }), 200
    else:
        return jsonify({
            "status": "DOWN",
            "error": "Simulated outage for Harness rollback testing"
        }), 500

@app.route("/api/info")
def info():
    """Metadata API for Harness pipeline verification."""
    return jsonify({
        "app_name": "harness-demo-fleet",
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
        "hostname": socket.gethostname(),
        "color": APP_COLOR,
        "deployed_by": DEPLOYED_BY
    })

@app.route("/api/toggle-health", methods=["POST"])
def toggle_health():
    """Toggle health state to test canary/rollback failure scenarios."""
    global is_healthy
    is_healthy = not is_healthy
    return jsonify({"healthy": is_healthy})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

