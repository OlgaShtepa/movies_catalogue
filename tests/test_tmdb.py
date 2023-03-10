import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_get_single_movie(monkeypatch):
   # Create a mock response for the requests.get method
   mock_response = Mock()
   mock_response.json.return_value = {"id": 1234, "title": "Test Movie"}
   mock_get = Mock(return_value=mock_response)

   # Patch the requests.get method with the mock function
   monkeypatch.setattr("tmdb_client.requests.get", mock_get)

   # Call the function under test
   movie = tmdb_client.get_single_movie(1234)

   # Check that the function returned the expected movie
   assert movie["id"] == 1234
   assert movie["title"] == "Test Movie"


def test_get_single_movie_cast(monkeypatch):
   # Create a mock response for the requests.get method
   mock_response = Mock()
   mock_response.json.return_value = {"cast": [{"name": "Actor 1"}, {"name": "Actor 2"}]}
   mock_get = Mock(return_value=mock_response)

   # Patch the requests.get method with the mock function
   monkeypatch.setattr("tmdb_client.requests.get", mock_get)

   # Call the function under test
   cast = tmdb_client.get_single_movie_cast(1234)

   # Check that the function returned the expected cast list
   assert len(cast) == 2
   assert cast[0]["name"] == "Actor 1"
   assert cast[1]["name"] == "Actor 2"


def test_get_movie_images(monkeypatch):
   # Create a mock response for the requests.get method
   mock_response = Mock()
   mock_response.json.return_value = {"backdrops": [{"file_path": "/backdrop.jpg"}, {"file_path": "/backdrop2.jpg"}]}
   mock_get = Mock(return_value=mock_response)



from unittest.mock import Mock

import tmdb_client

def test_call_tmdb_api(monkeypatch):
    # Create a mock response object
    mock_response = {'results': [{'id': 123, 'title': 'Mock Movie'}]}

    # Create a mock API function that returns the mock response
    def mock_get(*args, **kwargs):
        return Mock(status_code=200, json=lambda: mock_response)

    # Use monkeypatch to replace the requests.get function with our mock API function
    monkeypatch.setattr('requests.get', mock_get)

    # Call the API function with a mock endpoint
    response = tmdb_client.call_tmdb_api('mock/endpoint')

    # Assert that the response is the same as the mock response
    assert response == mock_response
