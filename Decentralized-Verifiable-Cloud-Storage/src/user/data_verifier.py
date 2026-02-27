import requests
from src.crypto.commitment_engine import CommitmentEngine

SERVER_URL = "http://127.0.0.1:5000/get/"

engine = CommitmentEngine()

def verify_data(index: int):
    """
    Retrieve data from cloud and verify integrity & freshness.
    """
    response = requests.get(f"{SERVER_URL}{index}")

    if response.status_code != 200:
        print("Error:", response.json())
        return

    record = response.json()
    data = record["data"]
    counter = record["counter"]
    stored_commitment = record["commitment"]

    print("\nRetrieved Record:")
    print(record)

    is_valid = engine.verify_commitment(data, counter, stored_commitment)

    if is_valid:
        print("\n✅ Data Integrity Verified Successfully!")
    else:
        print("\n❌ Data Integrity Compromised!")


if __name__ == "__main__":
    index = int(input("Enter data index to verify: "))
    verify_data(index)