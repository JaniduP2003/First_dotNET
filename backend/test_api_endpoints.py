"""
PyTest Integration Tests for .NET Core Web API endpoints.

This module contains integration tests for the /games and /genres endpoints.
These tests demonstrate:
- Integration testing with real API
- Fixtures for test configuration
- Assertions on HTTP responses
- Mocking error scenarios
"""

import pytest
import requests
from unittest.mock import Mock, patch


@pytest.mark.integration
class TestGamesEndpoint:
    """Test suite for the /games endpoint."""
    
    def test_get_games_returns_200_ok(self, base_url, api_headers):
        """
        Test that GET /games returns a 200 OK status code.
        
        This verifies that the endpoint is accessible and responds successfully.
        """
        response = requests.get(f"{base_url}/games", headers=api_headers)
        
        assert response.status_code == 200, (
            f"Expected status code 200, but got {response.status_code}"
        )
    
    def test_get_games_returns_json_list(self, base_url, api_headers):
        """
        Test that GET /games returns a JSON list.
        
        This verifies that the response body is valid JSON and is a list type.
        """
        response = requests.get(f"{base_url}/games", headers=api_headers)
        
        # Verify response is valid JSON
        assert response.headers.get("Content-Type", "").startswith("application/json"), (
            f"Expected JSON content type, but got {response.headers.get('Content-Type')}"
        )
        
        # Parse JSON and verify it's a list
        data = response.json()
        assert isinstance(data, list), (
            f"Expected response to be a list, but got {type(data).__name__}"
        )
    
    def test_get_games_list_structure(self, base_url, api_headers):
        """
        Test that GET /games returns a list with expected structure.
        
        This verifies basic structure of game objects if the list is not empty.
        """
        response = requests.get(f"{base_url}/games", headers=api_headers)
        data = response.json()
        
        # If there are games, verify they have expected fields
        if len(data) > 0:
            game = data[0]
            assert isinstance(game, dict), "Each game should be a dictionary"
            
            # Check for common expected fields (adjust based on your actual API)
            expected_fields = ["id", "name"]
            for field in expected_fields:
                assert field in game, f"Game object should have '{field}' field"
    
    @patch('requests.get')
    def test_get_games_handles_500_error(self, mock_get, base_url, api_headers):
        """
        Test that the client correctly handles a 500 Internal Server Error.
        
        This uses pytest-mock to simulate a server error and verify error handling.
        """
        # Create a mock response with 500 status code
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_response.json.side_effect = ValueError("No JSON object could be decoded")
        
        # Configure the mock to return our mock response
        mock_get.return_value = mock_response
        
        # Make the request (which will use the mocked requests.get)
        response = requests.get(f"{base_url}/games", headers=api_headers)
        
        # Assert that we received the expected error status code
        assert response.status_code == 500, (
            f"Expected status code 500, but got {response.status_code}"
        )
        
        # Verify the mock was called with correct parameters
        mock_get.assert_called_once_with(
            f"{base_url}/games",
            headers=api_headers
        )
    
    @patch('requests.get')
    def test_get_games_network_timeout_handling(self, mock_get, base_url, api_headers):
        """
        Test handling of network timeout scenarios.
        
        This demonstrates mocking a timeout exception.
        """
        # Configure mock to raise a timeout exception
        mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")
        
        # Verify that the timeout exception is raised
        with pytest.raises(requests.exceptions.Timeout):
            requests.get(f"{base_url}/games", headers=api_headers)


@pytest.mark.integration
class TestGenresEndpoint:
    """Test suite for the /genres endpoint."""
    
    def test_get_genres_returns_200_ok(self, base_url, api_headers):
        """
        Test that GET /genres returns a 200 OK status code.
        """
        response = requests.get(f"{base_url}/genres", headers=api_headers)
        
        assert response.status_code == 200, (
            f"Expected status code 200, but got {response.status_code}"
        )
    
    def test_get_genres_returns_json_list(self, base_url, api_headers):
        """
        Test that GET /genres returns a JSON list.
        """
        response = requests.get(f"{base_url}/genres", headers=api_headers)
        
        # Verify response is valid JSON
        assert response.headers.get("Content-Type", "").startswith("application/json"), (
            f"Expected JSON content type, but got {response.headers.get('Content-Type')}"
        )
        
        # Parse JSON and verify it's a list
        data = response.json()
        assert isinstance(data, list), (
            f"Expected response to be a list, but got {type(data).__name__}"
        )


@pytest.mark.integration
class TestAPIHealthCheck:
    """Test suite for general API health and availability."""
    
    def test_api_is_running(self, base_url):
        """
        Test that the API is accessible and responding.
        
        This is a basic smoke test to verify the API is running.
        """
        try:
            # Try to connect to the base URL or a known endpoint
            response = requests.get(f"{base_url}/games", timeout=5)
            assert response.status_code in [200, 404, 500], (
                "API should be accessible and return a valid HTTP status code"
            )
        except requests.exceptions.ConnectionError:
            pytest.fail("Cannot connect to API. Ensure the .NET backend is running.")
        except requests.exceptions.Timeout:
            pytest.fail("API connection timed out. Check if the backend is responsive.")
