import argparse
import socket
import threading

try:
    from .commands import CommandRegistry
    from .number_bomb import NumberBombGame
except ImportError:
    from commands import CommandRegistry
    from number_bomb import NumberBombGame


class ChatServer:
    def __init__(self, host="127.0.0.1", port=5000, now_provider=None):
        self.host = host
        self.port = port
        self.command_registry = CommandRegistry(now_provider=now_provider)
        self.number_bomb_game = NumberBombGame()
        self._server_socket = None
        self._accept_thread = None
        self._running = threading.Event()
        self._lock = threading.RLock()
        self._clients = {}

    def start(self):
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind((self.host, self.port))
        self._server_socket.listen()
        self.port = self._server_socket.getsockname()[1]
        self._running.set()
        self._accept_thread = threading.Thread(target=self._accept_loop, daemon=True)
        self._accept_thread.start()

    def stop(self):
        self._running.clear()
        if self._server_socket:
            try:
                self._server_socket.close()
            except OSError:
                pass

        with self._lock:
            clients = list(self._clients.values())
            self._clients.clear()

        for client in clients:
            try:
                client.close()
            except OSError:
                pass

        if self._accept_thread and self._accept_thread.is_alive():
            self._accept_thread.join(timeout=1)

    def serve_forever(self):
        self.start()
        print(f"Chat server listening on {self.host}:{self.port}")
        try:
            while self._running.is_set():
                threading.Event().wait(0.5)
        except KeyboardInterrupt:
            print("\nStopping server...")
        finally:
            self.stop()

    def _accept_loop(self):
        while self._running.is_set():
            try:
                client_socket, _address = self._server_socket.accept()
            except OSError:
                break
            thread = threading.Thread(target=self._handle_client, args=(client_socket,), daemon=True)
            thread.start()

    def _handle_client(self, client_socket):
        username = None
        try:
            self._send(client_socket, "Enter username:")
            username = self._read_line(client_socket)
            if not username:
                return
            username = username.strip()

            with self._lock:
                if not username or username in self._clients:
                    self._send(client_socket, "Username already taken. Disconnecting.")
                    return
                self._clients[username] = client_socket

            self._send(client_socket, f"Welcome, {username}!")
            self._broadcast(f"System: {username} joined the chat.", exclude=username)

            while self._running.is_set():
                message = self._read_line(client_socket)
                if message is None:
                    break
                message = message.strip()
                if not message:
                    continue
                if message == "/quit":
                    self._send(client_socket, "Goodbye.")
                    break
                if message.startswith("/game"):
                    self._broadcast_game_messages(self.number_bomb_game.handle(username, message, self.online_users()))
                elif message.startswith("/"):
                    self._send(client_socket, self.command_registry.handle(message, self.online_users()))
                else:
                    self._broadcast(f"{username}: {message}", exclude=username)
        except OSError:
            pass
        finally:
            if username:
                removed = False
                with self._lock:
                    if self._clients.get(username) is client_socket:
                        del self._clients[username]
                        removed = True
                if removed:
                    self._broadcast(f"System: {username} left the chat.", exclude=username)
            try:
                client_socket.close()
            except OSError:
                pass

    def online_users(self):
        with self._lock:
            return list(self._clients.keys())

    def _broadcast(self, message, exclude=None):
        with self._lock:
            recipients = [
                (username, client)
                for username, client in self._clients.items()
                if username != exclude
            ]

        for _username, client in recipients:
            try:
                self._send(client, message)
            except OSError:
                pass

    def _broadcast_game_messages(self, messages):
        for message in messages:
            self._broadcast(message)

    @staticmethod
    def _send(client_socket, message):
        client_socket.sendall((message + "\n").encode("utf-8"))

    @staticmethod
    def _read_line(client_socket):
        data = b""
        while not data.endswith(b"\n"):
            chunk = client_socket.recv(1)
            if not chunk:
                return None if not data else data.decode("utf-8").strip()
            data += chunk
        return data.decode("utf-8").strip()


def main():
    parser = argparse.ArgumentParser(description="Start the chat server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    ChatServer(host=args.host, port=args.port).serve_forever()


if __name__ == "__main__":
    main()
