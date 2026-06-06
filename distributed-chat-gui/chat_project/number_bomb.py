class NumberBombGame:
    def __init__(self, total_rounds=3):
        self.total_rounds = total_rounds
        self.active = False
        self.players = []
        self.round_number = 0
        self.setter = None
        self.guesser = None
        self.bomb = None
        self.low = 1
        self.high = 100
        self.current_guesses = 0
        self.scores = {}

    def handle(self, username, message, online_users):
        parts = message.strip().split()
        if len(parts) < 2:
            return [self.help_text()]

        action = parts[1].lower()
        if action == "start":
            return self.start(username, online_users)
        if action == "bomb":
            return self.set_bomb(username, parts)
        if action == "guess":
            return self.guess(username, parts)
        if action == "score":
            return [self.scoreboard()] if self.active or self.scores else ["Game: no score yet."]
        if action == "stop":
            self.reset()
            return ["Game: Number Bomb stopped."]
        return [self.help_text()]

    def start(self, username, online_users):
        if len(online_users) < 2:
            return ["Game: at least two online users are required."]

        ordered_users = [username] + [user for user in sorted(online_users) if user != username]
        self.players = ordered_users[:2]
        self.active = True
        self.round_number = 1
        self.setter = self.players[0]
        self.guesser = self.players[1]
        self.scores = {self.players[0]: 0, self.players[1]: 0}
        self._reset_round_state()

        return self._round_intro(started=True)

    def set_bomb(self, username, parts):
        if not self.active:
            return ["Game: start first with /game start."]
        if username != self.setter:
            return [f"Game: only {self.setter} can set the bomb this round."]
        if len(parts) != 3:
            return ["Game: choose a bomb with /game bomb <1-100>."]

        value = self._parse_number(parts[2])
        if value is None or value < 1 or value > 100:
            return ["Game: bomb must be a number between 1 and 100."]

        self.bomb = value
        return [f"Game: bomb is set. {self.guesser}, guess with /game guess <{self.low}-{self.high}>."]

    def guess(self, username, parts):
        if not self.active:
            return ["Game: start first with /game start."]
        if self.bomb is None:
            return [f"Game: waiting for {self.setter} to set the bomb."]
        if username != self.guesser:
            return [f"Game: only {self.guesser} can guess this round."]
        if len(parts) != 3:
            return [f"Game: guess with /game guess <{self.low}-{self.high}>."]

        value = self._parse_number(parts[2])
        if value is None:
            return ["Game: guess must be a number."]
        if value < self.low or value > self.high:
            return [f"Game: guess must be between {self.low} and {self.high}."]

        self.current_guesses += 1
        if value < self.bomb:
            self.low = value + 1
            return [f"Game: {username} guessed {value}. Safe. Range is now {self.low}-{self.high}."]
        if value > self.bomb:
            self.high = value - 1
            return [f"Game: {username} guessed {value}. Safe. Range is now {self.low}-{self.high}."]

        self.scores[username] += self.current_guesses
        messages = [f"Game: {username} hit the bomb {value} in {self.current_guesses} guesses."]

        if self.round_number >= self.total_rounds:
            messages.append(f"Game over. {self.scoreboard()}")
            self.active = False
            return messages

        self.round_number += 1
        self.setter, self.guesser = self.guesser, self.setter
        self._reset_round_state()
        messages.extend(self._round_intro(started=False))
        return messages

    def scoreboard(self):
        if not self.scores:
            return "Scoreboard: no score yet."

        parts = [f"{player} {self.scores[player]} guesses" for player in self.players]
        lowest = min(self.scores.values())
        winners = [player for player in self.players if self.scores[player] == lowest]
        winner_text = "tie" if len(winners) > 1 else winners[0]
        return f"Scoreboard: {', '.join(parts)}. Winner: {winner_text}."

    @staticmethod
    def help_text():
        return "Game: use /game start, /game bomb <number>, /game guess <number>, /game score, or /game stop."

    def reset(self):
        self.active = False
        self.players = []
        self.round_number = 0
        self.setter = None
        self.guesser = None
        self.bomb = None
        self.low = 1
        self.high = 100
        self.current_guesses = 0
        self.scores = {}

    def _round_intro(self, started):
        prefix = [f"Game: Number Bomb started. Round {self.round_number} of {self.total_rounds}."] if started else []
        return prefix + [
            f"Game: Round {self.round_number} of {self.total_rounds}. {self.setter} sets the bomb. {self.guesser} guesses."
            if not started
            else f"Game: {self.setter} sets the bomb. {self.guesser} guesses.",
            f"Private to {self.setter}: choose a bomb with /game bomb <1-100>.",
        ]

    def _reset_round_state(self):
        self.bomb = None
        self.low = 1
        self.high = 100
        self.current_guesses = 0

    @staticmethod
    def _parse_number(value):
        try:
            return int(value)
        except ValueError:
            return None
