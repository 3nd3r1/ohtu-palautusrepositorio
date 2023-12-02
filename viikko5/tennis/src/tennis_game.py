from enum import Enum


class TennisScore(Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3
    Advantage = 4
    Win = 5

    def __str__(self):
        return f"{self.name.lower().capitalize()}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class TennisPlayer:
    def __init__(self, player_name, score):
        self.player_name = player_name
        self.score = score

    def increment_score(self):
        self.score = TennisScore(self.score.value + 1)


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = TennisPlayer(player1_name, TennisScore.Love)
        self.player2 = TennisPlayer(player2_name, TennisScore.Love)

    def won_point(self, player_name):
        player = self.player1 if player_name == self.player1.player_name else self.player2
        other_player = self.player2 if player_name == self.player1.player_name else self.player1

        if other_player.score == TennisScore.Advantage:
            other_player.score = TennisScore.Forty
        elif player.score == TennisScore.Forty and other_player.score < TennisScore.Forty:
            player.score = TennisScore.Win
        else:
            player.increment_score()

    def get_score(self):
        # Player 1 and Player 2 have the same score
        if self.player1.score == self.player2.score:
            if self.player1.score < TennisScore.Forty:
                return f"{str(self.player1.score)}-All"
            return "Deuce"

        # Player 1 or Player 2 have a different score less than Advantage
        if self.player1.score < TennisScore.Advantage and self.player2.score < TennisScore.Advantage:
            return f"{str(self.player1.score)}-{str(self.player2.score)}"

        # Player 1 or Player 2 have won
        if self.player1.score == TennisScore.Win or self.player2.score == TennisScore.Win:
            if self.player1.score == TennisScore.Win:
                return f"Win for {self.player1.player_name}"
            return f"Win for {self.player2.player_name}"

        # Player 1 or Player 2 have an Advantage
        if self.player1.score == TennisScore.Advantage:
            return f"Advantage {self.player1.player_name}"
        return f"Advantage {self.player2.player_name}"
