from datetime import datetime


class CommandRegistry:
    def __init__(self, now_provider=None):
        self.now_provider = now_provider or self._default_now
        self.search_index = {
            "tkinter": "Tkinter is Python's built-in GUI toolkit.",
            "socket": "Sockets let programs send data through a network connection.",
            "server": "The server receives messages and forwards them to clients.",
            "client": "A client connects to the server to send and receive messages.",
            "gui": "A GUI lets users chat without typing in the terminal.",
        }

    def handle(self, message, online_users):
        command, _, argument = message.strip().partition(" ")
        command = command.lower()
        argument = argument.strip()

        if command == "/time":
            return f"Server time: {self.now_provider()}"
        if command == "/who":
            if online_users:
                return f"Online users: {', '.join(sorted(online_users))}"
            return "Online users: nobody"
        if command == "/poem":
            return "Roses are red\nChats travel through\nA server in Python\nConnects me and you"
        if command == "/search":
            return self._search(argument)
        return "Unknown command. Try /time, /who, /poem, or /search <keyword>."

    def _search(self, keyword):
        if not keyword:
            return "Usage: /search <keyword>"

        normalized = keyword.lower()
        result = self.search_index.get(normalized)
        if result:
            return f"Search result for '{keyword}': {result}"
        return f"Search result for '{keyword}': no built-in result found."

    @staticmethod
    def _default_now():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
