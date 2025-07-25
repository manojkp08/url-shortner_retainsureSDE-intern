import pytest
from app.main import app
from app.models import url_mappings, click_counts

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_shorten_url(client):
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    assert response.status_code == 201
    assert "short_code" in response.json

def test_redirect(client):
    # First shorten a URL
    shorten_resp = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = shorten_resp.json["short_code"]

    # Test redirect
    redirect_resp = client.get(f'/{short_code}')
    assert redirect_resp.status_code == 302  # Redirect status

def test_invalid_url(client):
    response = client.post('/api/shorten', json={"url": "not-a-url"})
    assert response.status_code == 400

def test_stats(client):
    shorten_resp = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = shorten_resp.json["short_code"]

    stats_resp = client.get(f'/api/stats/{short_code}')
    assert stats_resp.status_code == 200
    assert stats_resp.json["clicks"] == 0  # No clicks yet