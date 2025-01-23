from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Patient Recovery Assistant!"})

@app.route("/info")
def info():
    return jsonify({"app_name": "Patient Recovery Assistant", "version": "1.0"})

if __name__ == "__main__":
    app.run(debug=True)
