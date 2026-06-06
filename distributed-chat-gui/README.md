# Distributed Chat GUI Project

This is a from-scratch Python chat system with a Tkinter GUI. It is designed for the final project requirement: a distributed chat system where users can send and receive messages through a graphical interface instead of the terminal.

## What It Includes

- `server.py`: starts the chat server and forwards messages between clients.
- `client_core.py`: handles client connection, sending, and receiving.
- `gui_client.py`: provides the Tkinter user interface.
- `commands.py`: implements `/time`, `/who`, `/poem`, and `/search`.
- `number_bomb.py`: implements the three-round Number Bomb game.
- `tests/`: verifies the command logic and server message flow.

## Requirements

Use Python 3. Tkinter is included with most standard Python installations.

No third-party packages are required.

## How To Run

Open a terminal in the project folder:

```bash
cd distributed-chat-gui
```

Start the server:

```bash
python3 chat_project/server.py
```

Open a second terminal and start the first GUI client:

```bash
python3 chat_project/gui_client.py
```

Open a third terminal and start the second GUI client:

```bash
python3 chat_project/gui_client.py
```

In the two GUI windows:

1. Keep the host as `127.0.0.1`.
2. Keep the port as `5000`.
3. Use different names, such as `alice` and `bob`.
4. Click `Connect`.
5. Send messages between the two windows.

## GUI Features To Show

- Connect to the chat server.
- Send and receive normal chat messages.
- Show system messages when another user joins or leaves.
- Use `Time` to ask the server for the current time.
- Use `Who` to list online users.
- Use `Poem` to display a short poem.
- Use `Search` with keywords like `tkinter`, `socket`, `server`, `client`, or `gui`.
- Play the Number Bomb game.
- Disconnect from the server.

## Number Bomb Game

The app includes a two-player Number Bomb game.

Rules:

1. One player starts the game.
2. The first player sets a bomb number from 1 to 100.
3. The other player guesses numbers.
4. Every safe guess shrinks the range.
5. When the guess hits the bomb, the round ends.
6. The next round swaps the roles.
7. The game lasts three rounds.
8. The player with fewer total guesses wins.

GUI buttons:

- `Start Game`: starts a three-round game.
- `Set Bomb`: sends the number in the `Bomb` box.
- `Guess`: sends the number in the `Guess` box.
- `Score`: shows the current scoreboard.
- `Stop`: stops the current game.

The same actions can also be sent through chat commands:

```text
/game start
/game bomb 72
/game guess 50
/game score
/game stop
```

## Demo Checklist

Use this order for your app demo:

1. Start the server.
2. Open two GUI clients.
3. Connect as two different users.
4. Send a message from user 1 to user 2.
5. Send a reply from user 2 to user 1.
6. Click `Time`, `Who`, and `Poem`.
7. Search for `tkinter` or `socket`.
8. Click `Start Game`.
9. Set a bomb number in one client.
10. Guess numbers in the other client until the range shrinks and the bomb is hit.
11. Continue until three rounds finish and the scoreboard appears.
12. Disconnect one user and show the system message.

## Video Structure

The presentation should be 10 to 15 minutes.

Suggested structure:

1. Introduction, about 2 minutes:
   Explain that you built a Python distributed chat system with a GUI because the original terminal-only experience is not user-friendly.

2. App demo, about 4 minutes:
   Show the server, two GUI clients, message sending, command buttons, search, the Number Bomb game, and disconnect behavior.

3. Discussion, about 3 minutes:
   Explain the files. The server accepts clients and broadcasts messages. The client core handles networking. The GUI displays messages and buttons. The commands module handles special commands. The number bomb module manages game state, rounds, guessing ranges, and the scoreboard.

4. Analysis, about 3 minutes:
   Explain that the code is separated by responsibility. Mention improvements you could add later, such as secure messaging, file transfer, login passwords, or more games.

## How To Test

Run:

```bash
python3 -m unittest discover -s chat_project/tests -v
```

The tests check:

- command responses
- message broadcasting between two clients
- command replies staying private
- duplicate usernames being rejected
- Number Bomb range shrinking
- three-round Number Bomb scoring
