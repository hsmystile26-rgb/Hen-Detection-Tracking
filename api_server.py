from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hen Detection API is running"

@app.route("/predict", methods=["POST"])
def predict():
    # Later we will connect this to your model
    return jsonify({"status": "API connected successfully"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
