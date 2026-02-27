from flask import Flask, request, jsonify
from src.crypto.commitment_engine import CommitmentEngine

app = Flask(__name__)

# Simulated cloud storage (in-memory database)
cloud_storage = []
engine = CommitmentEngine()


@app.route("/")
def home():
    return "Decentralized Verifiable Cloud Storage Server Running"


@app.route("/upload", methods=["POST"])
def upload_data():
    """
    Owner uploads streaming data to cloud.
    Cloud stores data + commitment proof.
    """
    data = request.json.get("data")

    if not data:
        return jsonify({"error": "No data provided"}), 400

    commitment_record = engine.create_commitment(data)
    cloud_storage.append(commitment_record)

    return jsonify({
        "message": "Data uploaded successfully",
        "record": commitment_record
    })


@app.route("/get/<int:index>", methods=["GET"])
def get_data(index):
    """
    User retrieves data + commitment proof from cloud.
    """
    if index < 0 or index >= len(cloud_storage):
        return jsonify({"error": "Invalid index"}), 404

    return jsonify(cloud_storage[index])


@app.route("/all", methods=["GET"])
def get_all_data():
    """
    Retrieve all stored streaming data blocks.
    """
    return jsonify(cloud_storage)


if __name__ == "__main__":
    app.run(debug=True)