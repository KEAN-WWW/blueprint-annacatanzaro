"""This is a test script to test flask application"""
import pytest
from wsgi import app



@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """flask unit testing for content in default page"""
    response = client.get('/')  # Simulate visiting the homepage
    assert response.status_code == 200  # Check if connection is OK
    assert b'Blueprint' in response.data  # Check that keyword 'Blueprint' exists in content


def test_about_page_content(client):
    """flask unit testing for content in about page"""
    response = client.get('/about')  # Simulate visiting the about page
    assert response.status_code == 200  # Check if connection is OK
    assert b'Blueprint' in response.data  # Check that keyword 'Blueprint' exists in content
