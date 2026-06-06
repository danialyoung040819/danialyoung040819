import queue
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

try:
    from .client_core import ChatClientCore
except ImportError:
    from client_core import ChatClientCore


class ChatGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Distributed Chat GUI")
        self.events = queue.Queue()
        self.client = ChatClientCore(
            on_message=lambda message: self.events.put(("message", message)),
            on_status=lambda status: self.events.put(("status", status)),
        )

        self.host_var = tk.StringVar(value="127.0.0.1")
        self.port_var = tk.StringVar(value="5000")
        self.username_var = tk.StringVar(value="alice")
        self.status_var = tk.StringVar(value="Disconnected")
        self.message_var = tk.StringVar()
        self.search_var = tk.StringVar()
        self.bomb_var = tk.StringVar()
        self.guess_var = tk.StringVar()

        self._build_layout()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self.root.after(100, self._process_events)

    def _build_layout(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        connection = ttk.Frame(self.root, padding=10)
        connection.grid(row=0, column=0, sticky="ew")
        for column in range(8):
            connection.columnconfigure(column, weight=1 if column in (1, 3, 5) else 0)

        ttk.Label(connection, text="Host").grid(row=0, column=0, padx=(0, 4))
        ttk.Entry(connection, textvariable=self.host_var, width=14).grid(row=0, column=1, sticky="ew", padx=(0, 8))
        ttk.Label(connection, text="Port").grid(row=0, column=2, padx=(0, 4))
        ttk.Entry(connection, textvariable=self.port_var, width=7).grid(row=0, column=3, sticky="ew", padx=(0, 8))
        ttk.Label(connection, text="Name").grid(row=0, column=4, padx=(0, 4))
        ttk.Entry(connection, textvariable=self.username_var, width=12).grid(row=0, column=5, sticky="ew", padx=(0, 8))
        ttk.Button(connection, text="Connect", command=self._connect).grid(row=0, column=6, padx=(0, 6))
        ttk.Button(connection, text="Disconnect", command=self._disconnect).grid(row=0, column=7)

        chat_frame = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        chat_frame.grid(row=1, column=0, sticky="nsew")
        chat_frame.columnconfigure(0, weight=1)
        chat_frame.rowconfigure(0, weight=1)

        self.chat_log = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, height=18, state="disabled")
        self.chat_log.grid(row=0, column=0, sticky="nsew")

        controls = ttk.Frame(self.root, padding=(10, 0, 10, 8))
        controls.grid(row=2, column=0, sticky="ew")
        controls.columnconfigure(0, weight=1)

        ttk.Entry(controls, textvariable=self.message_var).grid(row=0, column=0, sticky="ew", padx=(0, 8))
        ttk.Button(controls, text="Send", command=self._send_message).grid(row=0, column=1)
        self.root.bind("<Return>", lambda _event: self._send_message())

        commands = ttk.Frame(self.root, padding=(10, 0, 10, 8))
        commands.grid(row=3, column=0, sticky="ew")
        commands.columnconfigure(4, weight=1)

        ttk.Button(commands, text="Time", command=lambda: self._send_command("/time")).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(commands, text="Who", command=lambda: self._send_command("/who")).grid(row=0, column=1, padx=(0, 6))
        ttk.Button(commands, text="Poem", command=lambda: self._send_command("/poem")).grid(row=0, column=2, padx=(0, 6))
        ttk.Label(commands, text="Search").grid(row=0, column=3, padx=(4, 4))
        ttk.Entry(commands, textvariable=self.search_var, width=18).grid(row=0, column=4, sticky="ew", padx=(0, 6))
        ttk.Button(commands, text="Go", command=self._search).grid(row=0, column=5)

        game = ttk.LabelFrame(self.root, text="Number Bomb Game", padding=(10, 8, 10, 8))
        game.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 8))
        for column in range(9):
            game.columnconfigure(column, weight=1 if column in (2, 5) else 0)

        ttk.Button(game, text="Start Game", command=lambda: self._send_command("/game start")).grid(row=0, column=0, padx=(0, 6))
        ttk.Button(game, text="Stop", command=lambda: self._send_command("/game stop")).grid(row=0, column=1, padx=(0, 12))
        ttk.Label(game, text="Bomb").grid(row=0, column=2, sticky="e", padx=(0, 4))
        ttk.Entry(game, textvariable=self.bomb_var, width=8).grid(row=0, column=3, sticky="ew", padx=(0, 6))
        ttk.Button(game, text="Set Bomb", command=self._set_bomb).grid(row=0, column=4, padx=(0, 12))
        ttk.Label(game, text="Guess").grid(row=0, column=5, sticky="e", padx=(0, 4))
        ttk.Entry(game, textvariable=self.guess_var, width=8).grid(row=0, column=6, sticky="ew", padx=(0, 6))
        ttk.Button(game, text="Guess", command=self._guess).grid(row=0, column=7, padx=(0, 6))
        ttk.Button(game, text="Score", command=lambda: self._send_command("/game score")).grid(row=0, column=8)

        status = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        status.grid(row=5, column=0, sticky="ew")
        ttk.Label(status, textvariable=self.status_var).grid(row=0, column=0, sticky="w")

    def _connect(self):
        username = self.username_var.get().strip()
        if not username:
            messagebox.showerror("Missing name", "Please enter a username.")
            return
        try:
            self.client.connect(self.host_var.get().strip(), self.port_var.get().strip(), username)
        except Exception as error:
            messagebox.showerror("Connection failed", str(error))

    def _disconnect(self):
        self.client.disconnect()

    def _send_message(self):
        message = self.message_var.get().strip()
        if not message:
            return
        try:
            self.client.send_message(message)
            self._append_message(f"Me: {message}")
            self.message_var.set("")
        except Exception as error:
            messagebox.showerror("Send failed", str(error))

    def _send_command(self, command):
        try:
            self.client.send_message(command)
        except Exception as error:
            messagebox.showerror("Command failed", str(error))

    def _search(self):
        keyword = self.search_var.get().strip()
        self._send_command(f"/search {keyword}" if keyword else "/search")

    def _set_bomb(self):
        bomb = self.bomb_var.get().strip()
        if not bomb:
            messagebox.showerror("Missing bomb", "Enter a number from 1 to 100.")
            return
        self._send_command(f"/game bomb {bomb}")

    def _guess(self):
        guess = self.guess_var.get().strip()
        if not guess:
            messagebox.showerror("Missing guess", "Enter a number to guess.")
            return
        self._send_command(f"/game guess {guess}")
        self.guess_var.set("")

    def _process_events(self):
        while True:
            try:
                event_type, value = self.events.get_nowait()
            except queue.Empty:
                break
            if event_type == "message":
                self._append_message(value)
            elif event_type == "status":
                self.status_var.set(value)
        self.root.after(100, self._process_events)

    def _append_message(self, message):
        self.chat_log.configure(state="normal")
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.see(tk.END)
        self.chat_log.configure(state="disabled")

    def _on_close(self):
        self.client.disconnect()
        self.root.destroy()


def main():
    root = tk.Tk()
    root.geometry("860x590")
    ChatGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
