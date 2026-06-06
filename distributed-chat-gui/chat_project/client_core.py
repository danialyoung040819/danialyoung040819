import socket
import threading


class ChatClientCore:
    def __init__(self, on_message=None, on_status=None):
        self.on_message = on_message or (lambda message: None)
        self.on_status = on_status or (lambda status: None)
        self._socket = None
        self._receiver_thread = None
        self._connected = threading.Event()
        self.username = None

    def connect(self, host, port, username):
        if self._connected.is_set():
            raise RuntimeError("Client is already connected.")

        client_socket = socket.create_connection((host, int(port)), timeout=5)
        prompt = self._read_line(client_socket)
        if prompt != "Enter username:":
            client_socket.close()
            raise RuntimeError(f"Unexpected server prompt: {prompt}")

        client_socket.sendall((username.strip() + "\n").encode("utf-8"))
        welcome = self._read_line(client_socket)
        if not welcome or not welcome.startswith("Welcome,"):
            client_socket.close()
            raise RuntimeError(welcome or "Server closed the connection.")

        self._socket = client_socket
        self.username = username.strip()
        self._connected.set()
        self.on_status(f"Connected as {self.username}")
        self.on_message(welcome)
        self._receiver_thread = threading.Thread(target=self._receive_loop, daemon=True)
        self._receiver_thread.start()

    def send_message(self, message):
        if not self._connected.is_set() or not self._socket:
            raise RuntimeError("Connect before sending a message.")
        text = message.strip()
        if text:
            self._socket.sendall((text + "\n").encode("utf-8"))

    def disconnect(self):
        self._connected.clear()
        if self._socket:
            try:
                self._socket.sendall(b"/quit\n")
            except OSError:
                pass
            try:
                self._socket.close()
            except OSError:
                pass
        self._socket = None
        self.on_status("Disconnected")

    def _receive_loop(self):
        try:
            while self._connected.is_set() and self._socket:
                message = self._read_line(self._socket)
                if message is None:
                    break
                self.on_message(message)
        except OSError:
            pass
        finally:
            self._connected.clear()
            self.on_status("Disconnected")

    @staticmethod
    def _read_line(client_socket):
        data = b""
        while not data.endswith(b"\n"):
            chunk = client_socket.recv(1)
            if not chunk:
                return None if not data else data.decode("utf-8").strip()
            data += chunk
        return data.decode("utf-8").strip()
