class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        national_players = list(filter(
            lambda player: player.nationality == nationality, self.reader.get_players()))
        return list(sorted(national_players, key=lambda player: player.points, reverse=True))
