import socket
import unittest

from chat_project.server import ChatServer


def read_line(sock):
    sock.settimeout(2)
    data = b""
    while not data.endswith(b"\n"):
        chunk = sock.recv(1)
        if not chunk:
            break
        data += chunk
    return data.decode("utf-8").strip()


def connect_user(port, username):
    sock = socket.create_connection(("127.0.0.1", port), timeout=2)
    assert read_line(sock) == "Enter username:"
    sock.sendall(f"{username}\n".encode("utf-8"))
    welcome = read_line(sock)
    assert welcome == f"Welcome, {username}!"
    return sock


class ChatServerTest(unittest.TestCase):
    def test_server_broadcasts_messages_between_clients(self):
        server = ChatServer(host="127.0.0.1", port=0)
        server.start()
        try:
            alice = connect_user(server.port, "alice")
            bob = connect_user(server.port, "bob")
            self.assertEqual(read_line(alice), "System: bob joined the chat.")

            alice.sendall(b"hello bob\n")

            self.assertEqual(read_line(bob), "alice: hello bob")
        finally:
            alice.close()
            bob.close()
            server.stop()

    def test_server_replies_to_command_without_broadcasting_to_others(self):
        server = ChatServer(host="127.0.0.1", port=0, now_provider=lambda: "2026-06-06 14:30:00")
        server.start()
        try:
            alice = connect_user(server.port, "alice")
            bob = connect_user(server.port, "bob")
            self.assertEqual(read_line(alice), "System: bob joined the chat.")

            alice.sendall(b"/time\n")

            self.assertEqual(read_line(alice), "Server time: 2026-06-06 14:30:00")
            bob.settimeout(0.25)
            try:
                data = bob.recv(1024)
            except socket.timeout:
                data = b""
            self.assertEqual(data, b"")
        finally:
            alice.close()
            bob.close()
            server.stop()

    def test_server_rejects_duplicate_usernames(self):
        server = ChatServer(host="127.0.0.1", port=0)
        server.start()
        try:
            first = connect_user(server.port, "alice")
            duplicate = socket.create_connection(("127.0.0.1", server.port), timeout=2)
            self.assertEqual(read_line(duplicate), "Enter username:")

            duplicate.sendall(b"alice\n")

            self.assertEqual(read_line(duplicate), "Username already taken. Disconnecting.")
        finally:
            first.close()
            duplicate.close()
            server.stop()

    def test_server_runs_number_bomb_game_commands(self):
        server = ChatServer(host="127.0.0.1", port=0)
        server.start()
        try:
            alice = connect_user(server.port, "alice")
            bob = connect_user(server.port, "bob")
            self.assertEqual(read_line(alice), "System: bob joined the chat.")

            alice.sendall(b"/game start\n")

            self.assertEqual(read_line(alice), "Game: Number Bomb started. Round 1 of 3.")
            self.assertEqual(read_line(alice), "Game: alice sets the bomb. bob guesses.")
            self.assertEqual(read_line(alice), "Private to alice: choose a bomb with /game bomb <1-100>.")
            self.assertEqual(read_line(bob), "Game: Number Bomb started. Round 1 of 3.")
            self.assertEqual(read_line(bob), "Game: alice sets the bomb. bob guesses.")
            self.assertEqual(read_line(bob), "Private to alice: choose a bomb with /game bomb <1-100>.")

            alice.sendall(b"/game bomb 72\n")
            self.assertEqual(read_line(alice), "Game: bomb is set. bob, guess with /game guess <1-100>.")
            self.assertEqual(read_line(bob), "Game: bomb is set. bob, guess with /game guess <1-100>.")

            bob.sendall(b"/game guess 30\n")
            self.assertEqual(read_line(alice), "Game: bob guessed 30. Safe. Range is now 31-100.")
            self.assertEqual(read_line(bob), "Game: bob guessed 30. Safe. Range is now 31-100.")
        finally:
            alice.close()
            bob.close()
            server.stop()


if __name__ == "__main__":
    unittest.main()
