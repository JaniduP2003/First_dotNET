"""
Game Service Module - A simple service for managing game data.

This module demonstrates a basic service class that can be tested with PyTest.
"""

import requests
from typing import List, Dict, Optional


class GameService:
    """Service class for managing game operations."""
    
    def __init__(self, base_url: str = "http://localhost:8080"):
        """
        Initialize the GameService.
        
        Args:
            base_url: The base URL of the game API
        """
        self.base_url = base_url
    
    def get_all_games(self) -> List[Dict]:
        """
        Fetch all games from the API.
        
        Returns:
            List of game dictionaries
        """
        response = requests.get(f"{self.base_url}/games")
        response.raise_for_status()
        return response.json()
    
    def get_game_by_id(self, game_id: int) -> Optional[Dict]:
        """
        Fetch a specific game by ID.
        
        Args:
            game_id: The ID of the game to fetch
            
        Returns:
            Game dictionary or None if not found
        """
        try:
            response = requests.get(f"{self.base_url}/games/{game_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            return None
    
    def calculate_game_score(self, base_score: int, multiplier: float) -> float:
        """
        Calculate a game score with a multiplier.
        
        Args:
            base_score: The base score
            multiplier: The score multiplier
            
        Returns:
            Calculated score
        """
        if base_score < 0:
            raise ValueError("Base score cannot be negative")
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative")
        return base_score * multiplier
    
    def format_game_name(self, name: str) -> str:
        """
        Format a game name (capitalize words).
        
        Args:
            name: The game name to format
            
        Returns:
            Formatted game name
        """
        if not name:
            return ""
        return name.title()
    
    def is_game_expensive(self, price: float, threshold: float = 50.0) -> bool:
        """
        Check if a game is expensive based on a threshold.
        
        Args:
            price: The game price
            threshold: The price threshold (default: 50.0)
            
        Returns:
            True if expensive, False otherwise
        """
        return price > threshold
    
    def get_game_count(self) -> int:
        """
        Get the total count of games.
        
        Returns:
            Number of games
        """
        games = self.get_all_games()
        return len(games)
