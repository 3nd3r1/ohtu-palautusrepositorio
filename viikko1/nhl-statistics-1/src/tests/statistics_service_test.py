import unittest
from player import Player
from statistics_service import StatisticsService, SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_with_existing_player_returns_correct_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
    
    def test_search_with_nonexistent_player_returns_none(self):
        player = self.stats.search("Who?")
        self.assertIsNone(player)
    
    def test_team_with_existing_team_returns_correct_players(self):
        players = self.stats.team("EDM")
        self.assertCountEqual([player.name for player in players], ["Semenko", "Kurri", "Gretzky"])
    
    def test_team_with_nonexistent_team_returns_empty_list(self):
        players = self.stats.team("Who?")
        self.assertEqual(len(players), 0)
    
    def test_top_sort_by_points_returns_correct_players(self):
        players = self.stats.top(1, SortBy.POINTS)
        self.assertListEqual([player.name for player in players], ["Gretzky", "Lemieux"])

    def test_top_sort_by_goals_returns_correct_players(self):
        players = self.stats.top(1, SortBy.GOALS)
        self.assertListEqual([player.name for player in players], ["Lemieux", "Yzerman"])
    
    def test_top_sort_by_assists_returns_correct_players(self):
        players = self.stats.top(1, SortBy.ASSISTS)
        self.assertListEqual([player.name for player in players], ["Gretzky", "Yzerman"])


