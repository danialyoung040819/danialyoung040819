import unittest

from chat_project.commands import CommandRegistry


class CommandRegistryTest(unittest.TestCase):
    def test_time_command_returns_labelled_value(self):
        registry = CommandRegistry(now_provider=lambda: "2026-06-06 14:30:00")

        response = registry.handle("/time", ["alice", "bob"])

        self.assertEqual(response, "Server time: 2026-06-06 14:30:00")

    def test_who_command_lists_connected_users(self):
        registry = CommandRegistry(now_provider=lambda: "unused")

        response = registry.handle("/who", ["alice", "bob"])

        self.assertEqual(response, "Online users: alice, bob")

    def test_poem_command_returns_short_poem(self):
        registry = CommandRegistry(now_provider=lambda: "unused")

        response = registry.handle("/poem", ["alice"])

        self.assertIn("Roses are red", response)
        self.assertIn("Chats travel through", response)

    def test_search_command_requires_a_keyword(self):
        registry = CommandRegistry(now_provider=lambda: "unused")

        response = registry.handle("/search", ["alice"])

        self.assertEqual(response, "Usage: /search <keyword>")

    def test_search_command_returns_matching_help_text(self):
        registry = CommandRegistry(now_provider=lambda: "unused")

        response = registry.handle("/search tkinter", ["alice"])

        self.assertEqual(
            response,
            "Search result for 'tkinter': Tkinter is Python's built-in GUI toolkit.",
        )

    def test_unknown_command_returns_helpful_message(self):
        registry = CommandRegistry(now_provider=lambda: "unused")

        response = registry.handle("/missing", ["alice"])

        self.assertEqual(
            response,
            "Unknown command. Try /time, /who, /poem, or /search <keyword>.",
        )


if __name__ == "__main__":
    unittest.main()
