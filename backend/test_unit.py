"""
Unit Tests for Game Service.

This module demonstrates key PyTest features:
- Assertions
- Fixtures
- Parameterized tests
- Mocking
- Custom markers
"""

import pytest
from unittest.mock import Mock, patch
import requests
from game_service import GameService


# ============================================================================
# SECTION 1: Basic Assertions and Fixtures
# ============================================================================

@pytest.mark.unit
class TestGameServiceBasics:
    """Test game service calculation methods with parameterization."""
    
    @pytest.mark.parametrize("base_score,multiplier,expected", [
        (100, 1.0, 100.0),
        (100, 2.0, 200.0),
        (50, 1.5, 75.0),
        (0, 10.0, 0.0),
        (200, 0.5, 100.0),
    ])
    def test_calculate_game_score(self, game_service, base_score, multiplier, expected):
        """Test game score calculation with various inputs."""
        result = game_service.calculate_game_score(base_score, multiplier)
        assert result == expected
        assert result >= 0
    
    @pytest.mark.parametrize("base_score,multiplier", [
        (-10, 2.0),
        (100, -1.5),
    ])
    def test_calculate_game_score_negative_values(self, game_service, base_score, multiplier):
        """Test that negative values raise ValueError."""
        with pytest.raises(ValueError):
            game_service.calculate_game_score(base_score, multiplier)
    
    @pytest.mark.parametrize("name,expected", [
        ("super mario", "Super Mario"),
        ("the witcher", "The Witcher"),
        ("DOOM", "Doom"),
        ("", ""),
        ("call of duty", "Call Of Duty"),
    ])
    def test_format_game_name(self, game_service, name, expected):
        """Test game name formatting with various inputs."""
        result = game_service.format_game_name(name)
        assert result == expected
    
    @pytest.mark.parametrize("price,threshold,expected", [
        (60.0, 50.0, True),
        (40.0, 50.0, False),
        (50.0, 50.0, False),
        (100.0, 99.99, True),
        (0.0, 10.0, False),
    ])
    def test_is_game_expensive(self, game_service, price, threshold, expected):
        """Test expensive game detection with various thresholds."""
        result = game_service.is_game_expensive(price, threshold)
        assert result == expected
        assert isinstance(result, bool)


# ============================================================================
# SECTION 3: Mocking Tests
# ============================================================================

@pytest.mark.unit
class TestGameServiceMocking:
    """Demonstrate mocking of external API calls."""
    
    @patch('game_service.requests.get')
    def test_get_all_games_mocked(self, mock_get, game_service):
        """Test fetching all games with mocked API response."""
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 1, "name": "Game 1"},
            {"id": 2, "name": "Game 2"},
        ]
        mock_get.return_value = mock_response
        
        # Execute
        result = game_service.get_all_games()
        
        # Assert
        assert len(result) == 2
        assert result[0]["name"] == "Game 1"
        assert result[1]["name"] == "Game 2"
        mock_get.assert_called_once_with("http://localhost:8080/games")
    
    @patch('game_service.requests.get')
    def test_get_game_by_id_success(self, mock_get, game_service):
        """Test fetching a game by ID with successful response."""
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "Test Game"}
        mock_get.return_value = mock_response
        
        # Execute
        result = game_service.get_game_by_id(1)
        
        # Assert
        assert result is not None
        assert result["id"] == 1
        assert result["name"] == "Test Game"
        mock_get.assert_called_once_with("http://localhost:8080/games/1")
    
    @patch('game_service.requests.get')
    def test_get_game_by_id_not_found(self, mock_get, game_service):
        """Test fetching a non-existent game returns None."""
        # Setup mock to raise HTTPError
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404")
        mock_get.return_value = mock_response
        
        # Execute
        result = game_service.get_game_by_id(999)
        
        # Assert
        assert result is None
    
    @patch('game_service.requests.get')
    def test_get_game_count_mocked(self, mock_get, game_service):
        """Test game count with mocked API response."""
        # Setup mock
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"id": 1, "name": "Game 1"},
            {"id": 2, "name": "Game 2"},
            {"id": 3, "name": "Game 3"},
        ]
        mock_get.return_value = mock_response
        
        # Execute
        count = game_service.get_game_count()
        
        # Assert
        assert count == 3
        assert isinstance(count, int)
    
    def test_mock_with_pytest_mock(self, mocker, game_service):
        """Demonstrate using pytest-mock plugin for mocking."""
        # Create mock using pytest-mock
        mock_get = mocker.patch('game_service.requests.get')
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "name": "Mocked Game"}]
        mock_get.return_value = mock_response
        
        # Execute
        result = game_service.get_all_games()
        
        # Assert
        assert len(result) == 1
        assert result[0]["name"] == "Mocked Game"
        mock_get.assert_called_once()


# ============================================================================
# SECTION 4: Fixture Usage Examples
# ============================================================================

@pytest.mark.unit
class TestFixtureUsage:
    """Demonstrate various fixture usage patterns."""
    
    def test_using_sample_game_data(self, sample_game_data):
        """Test using fixture-provided sample data."""
        assert sample_game_data["id"] == 1
        assert sample_game_data["name"] == "Test Game"
        assert sample_game_data["price"] > 0
        assert "genre" in sample_game_data
    
    def test_using_games_list(self, sample_games_list):
        """Test using fixture-provided list of games."""
        assert len(sample_games_list) == 4
        assert all("name" in game for game in sample_games_list)
        assert all("price" in game for game in sample_games_list)
        
        # Find most expensive game
        most_expensive = max(sample_games_list, key=lambda g: g["price"])
        assert most_expensive["price"] == 69.99
    
    def test_using_test_config(self, test_config):
        """Test using session-scoped configuration fixture."""
        assert test_config["timeout"] == 5
        assert test_config["retry_count"] == 3
        assert test_config["test_mode"] is True
    
    def test_using_temp_file(self, temp_game_data):
        """Test using temporary file fixture."""
        content = temp_game_data.read_text()
        assert "Sample game data" in content
        assert temp_game_data.exists()


# ============================================================================
# SECTION 5: Complex Assertions
# ============================================================================

@pytest.mark.unit
class TestComplexAssertions:
    """Demonstrate various assertion techniques."""
    
    def test_multiple_assertions(self, sample_game_data):
        """Test with multiple related assertions."""
        # Type assertions
        assert isinstance(sample_game_data, dict)
        assert isinstance(sample_game_data["id"], int)
        assert isinstance(sample_game_data["price"], float)
        
        # Value assertions
        assert sample_game_data["id"] > 0
        assert len(sample_game_data["name"]) > 0
        assert sample_game_data["price"] >= 0
    
    def test_collection_assertions(self, sample_games_list):
        """Test assertions on collections."""
        # Length assertions
        assert len(sample_games_list) == 4
        
        # Membership assertions
        game_names = [g["name"] for g in sample_games_list]
        assert "Game One" in game_names
        assert "Game Five" not in game_names
        
        # All/any assertions
        assert all(game["price"] > 0 for game in sample_games_list)
        assert any(game["genre"] == "RPG" for game in sample_games_list)
    
    def test_approximate_comparisons(self, game_service):
        """Test floating point comparisons with approximation."""
        result = game_service.calculate_game_score(100, 3.333)
        
        # Use pytest.approx for floating point comparisons
        assert result == pytest.approx(333.3, rel=1e-2)
        assert isinstance(result, float)
    
    def test_string_assertions(self, game_service):
        """Test string-related assertions."""
        formatted = game_service.format_game_name("the legend of zelda")
        
        assert formatted.startswith("The")
        assert "Legend" in formatted
        assert formatted.endswith("Zelda")
        assert formatted.count(" ") == 3
        assert len(formatted) > 0


# ============================================================================
# SECTION 6: Exception Testing
# ============================================================================

@pytest.mark.unit
class TestExceptionHandling:
    """Demonstrate testing exception scenarios."""
    
    def test_value_error_with_context(self, game_service):
        """Test ValueError with context manager."""
        with pytest.raises(ValueError) as exc_info:
            game_service.calculate_game_score(-10, 2.0)
        
        assert "negative" in str(exc_info.value).lower()
        assert exc_info.type is ValueError
    
    def test_multiple_exceptions(self, game_service):
        """Test multiple exception scenarios."""
        # Test negative base score
        with pytest.raises(ValueError, match="Base score cannot be negative"):
            game_service.calculate_game_score(-10, 2.0)
        
        # Test negative multiplier
        with pytest.raises(ValueError, match="Multiplier cannot be negative"):
            game_service.calculate_game_score(100, -1.0)


# ============================================================================
# SECTION 7: Markers and Test Organization
# ============================================================================

@pytest.mark.slow
@pytest.mark.unit
def test_marked_as_slow(game_service):
    """Example of a test marked as slow."""
    result = game_service.calculate_game_score(1024, 1.0)
    assert result == 1024.0


@pytest.mark.integration
def test_marked_as_integration(game_service):
    """Example of a test marked as integration."""
    # This would typically make real API calls
    # For now, we'll just verify the service is configured
    assert game_service.base_url == "http://localhost:8080"


# ============================================================================
# SECTION 8: Setup and Teardown Examples
# ============================================================================

class TestSetupTeardown:
    """Demonstrate setup and teardown methods."""
    
    def setup_method(self):
        """Setup before each test method."""
        self.test_data = {"count": 0}
    
    def teardown_method(self):
        """Cleanup after each test method."""
        self.test_data = None
    
    def test_first(self):
        """First test with setup."""
        assert self.test_data["count"] == 0
        self.test_data["count"] += 1
    
    def test_second(self):
        """Second test - count is reset due to setup_method."""
        assert self.test_data["count"] == 0
