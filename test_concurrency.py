import threading
import requests
import subprocess
import time
import pytest

@pytest.fixture(scope="module")
def flask_server():
    # Start Flask server in background
    server = subprocess.Popen(
        ["python", "-m", "flask", "--app", "app.main", "run"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(3)  # Wait for server to start
    yield
    server.terminate()  # Cleanup after tests

def test_concurrent_shorten(flask_server):
    def worker():
        try:
            response = requests.post(
                "http://localhost:5000/api/shorten",
                json={"url": "https://example.com"},
                timeout=5
            )
            assert response.status_code == 201
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Request failed: {e}")

    threads = [threading.Thread(target=worker) for _ in range(10)]
    [t.start() for t in threads]
    [t.join() for t in threads]