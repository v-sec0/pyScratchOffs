"""Presentation helpers shared across the game (colors, layout, clearing).

This is pure "look" code — no game logic lives here. game.py imports from this
file so all the styling stays in one place.
"""

WIDTH = 48  # 🤖~ width of the bordered box
PAD = "  "  # 🤖~ indent used INSIDE the box (cards, wallet, status lines)


def clear():
    # 🤖~ Clear scrollback (3J), home the cursor (H), wipe the screen (2J) so no
    # old screen lingers at the top.
    print("\033[3J\033[H\033[2J", end="")


# 🤖~ ANSI color codes — each is just a number the terminal understands.
COLORS = {"red": "31", "green": "32", "yellow": "33", "cyan": "36", "bold": "1"}


def color(text, name):
    # 🤖~ Wrap text so the terminal prints it colored, then resets to normal.
    return f"\033[{COLORS[name]}m{text}\033[0m"


def rule():
    # 🤖~ A full-width divider line.
    print(color("=" * WIDTH, "cyan"))


def banner(title):
    # 🤖~ Center the title on the plain text FIRST, then color it — coloring
    # first would let the hidden codes throw off the centering.
    rule()
    print(color(title.center(WIDTH), "cyan"))
    rule()


def say(text="", name=None):
    # 🤖~ Print one message line (no indent). `name` optionally colors it.
    if name:
        text = color(text, name)
    print(text)


def screen(title, lines):
    # 🤖~ Clear to a fresh bordered screen that shows only the given status
    # lines (each indented inside the box, like the card listing).
    clear()
    banner(title)
    for line in lines:
        print(PAD + line)
    rule()
