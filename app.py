from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database (in-memory for now)
patients = [
    {
        "id": 1,
        "name": "John Doe",
        "age": 45,
        "heart_rate": 80,
        "blood_pressure": 120,
        "recovery_plan": "Exercise regularly, eat healthy, monitor blood pressure."
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 30,
        "heart_rate": 72,
        "blood_pressure": 115,
        "recovery_plan": "Cardio 3x per week, reduce stress, regular follow-ups."
    }
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Patient Recovery Assistant!"})

@app.route("/info")
def info():
    return jsonify({"app_name": "Patient Recovery Assistant", "version": "1.0"})

# Endpoint to get all patients
@app.route("/patients", methods=["GET"])
def get_patients():
    return jsonify({"patients": patients})

# Endpoint to get a specific patient by ID
@app.route("/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if patient:
        return jsonify(patient)
    return jsonify({"error": "Patient not found"}), 404

# Endpoint to add a new patient
@app.route("/patients", methods=["POST"])
def add_patient():
    new_patient = request.json
    new_patient["id"] = len(patients) + 1
    patients.append(new_patient)
    return jsonify({"message": "Patient added successfully!", "patient": new_patient}), 201

# Endpoint to update a patient's recovery plan
@app.route("/patients/<int:patient_id>", methods=["PUT"])
def update_patient(patient_id):
    patient = next((p for p in patients if p["id"] == patient_id), None)
    if patient:
        patient.update(request.json)
        return jsonify({"message": "Patient updated successfully!", "patient": patient})
    return jsonify({"error": "Patient not found"}), 404

# Endpoint to delete a patient
@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    global patients
    patients = [p for p in patients if p["id"] != patient_id]
    return jsonify({"message": "Patient deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
