import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the ACEest Home Route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data

def test_services_endpoint(client):
    """Test the Gym Services JSON Data"""
    response = client.get('/services')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert len(data['data']) > 0