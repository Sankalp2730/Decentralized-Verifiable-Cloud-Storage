import requests
import time

SERVER_URL = "http://127.0.0.1:5000/upload"

def stream_data():
    """
    Simulate real-time streaming data upload to cloud server.
    """
    sample_stream = [
        "Temperature: 32°C",
        "Humidity: 60%",
        "Pressure: 1012 hPa",
        "Temperature: 33°C",
        "Humidity: 58%"
    ]

    for data in sample_stream:
        response = requests.post(SERVER_URL, json={"data": data})
        print("Uploaded:", data)
        print("Server Response:", response.json())
        print("-" * 50)
        time.sleep(2)  # simulate streaming delay


if __name__ == "__main__":
    stream_data()