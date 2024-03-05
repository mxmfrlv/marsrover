from typing import Optional
GREETING = "Hello"


class Greeter(object):
    """Greetings."""

    def greet(self, name: Optional[str]) -> str:
        """Return a proper greeting for a person."""
        if name == None:
            return GREETING
        return GREETING + " " + name.strip()
