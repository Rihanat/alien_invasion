class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game starts inactive.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self._read_high_score()  # 🟢 Load from file

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self):
        """Read the stored high score from a file."""
        try:
            with open('high_score.txt') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Write the high score to a file."""
        with open('high_score.txt', 'w') as f:
            f.write(str(self.high_score))