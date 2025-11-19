"""
PyTest Configuration and Fixtures.

This file contains reusable fixtures that can be used across all test files.
"""

import pytest
import requests
from game_service import GameService


@pytest.fixture
def base_url():
    """
    Fixture providing the base URL of the running API.
    
    This can be overridden by setting the BASE_URL environment variable.
    """
    return "http://localhost:8080"


@pytest.fixture
def api_headers():
    """
    Fixture providing common headers for API requests.
    """
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture
def game_service(base_url):
    """
    Fixture providing a GameService instance.
    
    This fixture demonstrates dependency injection and reusable test objects.
    """
    return GameService(base_url=base_url)


@pytest.fixture
def sample_game_data():
    """
    Fixture providing sample game data for testing.
    
    This demonstrates providing test data through fixtures.
    """
    return {
        "id": 1,
        "name": "Test Game",
        "genre": "Action",
        "price": 59.99,
        "releaseDate": "2024-01-01"
    }


@pytest.fixture
def sample_games_list():
    """
    Fixture providing a list of sample games.
    
    Useful for testing list operations and iterations.
    """
    return [
        {"id": 1, "name": "Game One", "genre": "Action", "price": 59.99},
        {"id": 2, "name": "Game Two", "genre": "RPG", "price": 49.99},
        {"id": 3, "name": "Game Three", "genre": "Strategy", "price": 39.99},
        {"id": 4, "name": "Game Four", "genre": "Sports", "price": 69.99},
    ]


@pytest.fixture
def mock_api_response(mocker):
    """
    Fixture that provides a mock API response.
    
    This demonstrates fixture-level mocking.
    """
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    return mock_response


@pytest.fixture(scope="session")
def test_config():
    """
    Session-scoped fixture for test configuration.
    
    This is created once per test session and shared across all tests.
    """
    return {
        "timeout": 5,
        "retry_count": 3,
        "test_mode": True
    }


@pytest.fixture
def temp_game_data(tmp_path):
    """
    Fixture that creates temporary test data using tmp_path.
    
    Demonstrates working with temporary files in tests.
    """
    data_file = tmp_path / "game_data.txt"
    data_file.write_text("Sample game data for testing")
    return data_file


# Pytest hooks for custom behavior
def pytest_configure(config):
    """Add custom markers."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
