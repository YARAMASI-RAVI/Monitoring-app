from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "OK"}

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return jsonify({
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
