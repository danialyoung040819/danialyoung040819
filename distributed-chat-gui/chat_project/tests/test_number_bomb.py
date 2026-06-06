import unittest

from chat_project.number_bomb import NumberBombGame


class NumberBombGameTest(unittest.TestCase):
    def test_start_requires_two_players_and_assigns_roles(self):
        game = NumberBombGame()

        messages = game.handle("alice", "/game start", ["alice", "bob"])

        self.assertEqual(game.round_number, 1)
        self.assertEqual(game.setter, "alice")
        self.assertEqual(game.guesser, "bob")
        self.assertEqual(
            messages,
            [
                "Game: Number Bomb started. Round 1 of 3.",
                "Game: alice sets the bomb. bob guesses.",
                "Private to alice: choose a bomb with /game bomb <1-100>.",
            ],
        )

    def test_guessing_shrinks_range_until_bomb_is_hit(self):
        game = NumberBombGame()
        game.handle("alice", "/game start", ["alice", "bob"])
        game.handle("alice", "/game bomb 72", ["alice", "bob"])

        low = game.handle("bob", "/game guess 30", ["alice", "bob"])
        high = game.handle("bob", "/game guess 80", ["alice", "bob"])
        hit = game.handle("bob", "/game guess 72", ["alice", "bob"])

        self.assertEqual(low, ["Game: bob guessed 30. Safe. Range is now 31-100."])
        self.assertEqual(high, ["Game: bob guessed 80. Safe. Range is now 31-79."])
        self.assertEqual(
            hit,
            [
                "Game: bob hit the bomb 72 in 3 guesses.",
                "Game: Round 2 of 3. bob sets the bomb. alice guesses.",
                "Private to bob: choose a bomb with /game bomb <1-100>.",
            ],
        )

    def test_three_rounds_end_with_scoreboard_lowest_total_wins(self):
        game = NumberBombGame()
        game.handle("alice", "/game start", ["alice", "bob"])
        game.handle("alice", "/game bomb 50", ["alice", "bob"])
        game.handle("bob", "/game guess 50", ["alice", "bob"])
        game.handle("bob", "/game bomb 20", ["alice", "bob"])
        game.handle("alice", "/game guess 10", ["alice", "bob"])
        game.handle("alice", "/game guess 20", ["alice", "bob"])
        game.handle("alice", "/game bomb 90", ["alice", "bob"])

        result = game.handle("bob", "/game guess 90", ["alice", "bob"])

        self.assertEqual(
            result,
            [
                "Game: bob hit the bomb 90 in 1 guesses.",
                "Game over. Scoreboard: alice 2 guesses, bob 2 guesses. Winner: tie.",
            ],
        )
        self.assertFalse(game.active)

    def test_rejects_guess_outside_current_range(self):
        game = NumberBombGame()
        game.handle("alice", "/game start", ["alice", "bob"])
        game.handle("alice", "/game bomb 72", ["alice", "bob"])
        game.handle("bob", "/game guess 30", ["alice", "bob"])

        result = game.handle("bob", "/game guess 30", ["alice", "bob"])

        self.assertEqual(result, ["Game: guess must be between 31 and 100."])


if __name__ == "__main__":
    unittest.main()
