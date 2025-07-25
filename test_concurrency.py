# test_concurrency.py
import threading
import requests

def test_concurrent_shorten():
    def worker():
        response = requests.post(
            "http://localhost:5000/api/shorten",
            json={"url": "https://www.nvidia.com/en-us/geforce/campaigns/back-to-school/?nvid=nv-int-drvr-637258"}
        )
        assert response.status_code == 201

    # Create 50 threads
    threads = [threading.Thread(target=worker) for _ in range(50)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    # Verify all short codes are unique
    stats = requests.get("http://localhost:5000/api/stats").json()
    assert len(stats["urls"]) == 50  # All 50 requests succeeded uniquely