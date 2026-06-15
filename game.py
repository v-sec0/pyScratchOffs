from Player import Player
from ScratchOff import ScratchOff
from display import PAD, clear, color, rule, banner, say, screen

# 🧠~ Define scratch-offs
low = ScratchOff("Poor Man's Delight", 9.99, 250)
mid = ScratchOff("Money Multiplier", 19.99, 500)
high = ScratchOff("Uncle Sam Grand Slam", 49.99, 1000)
collection = {"1": low, "2": mid, "3": high}

# 🤖~ Emoji per card, keyed by the same IDs as `collection`. Kept here (not on
# the ScratchOff class) so the game logic stays untouched.
emojis = {"1": "💸", "2": "💰", "3": "🏆"}

# 🧠~ Define player class object
default = Player(100.00, 0.00, 0.00)


def select_scratcher():

    selection_valid = False
    earnings = 0

    while not selection_valid:
        try:
            # 🧠~ Loop through the scratcher collection and list each option
            index = 1
            clear()
            banner("🎰  SCRATCH-OFF SIMULATOR")
            for scratcher in collection:
                card = collection[scratcher]
                emoji = emojis[scratcher]
                price = f"${card.price:.2f}"
                # 🤖~ Pad to width 8 FIRST, then color — coloring first would
                # make the hidden codes count toward the width and break alignment.
                price_col = color(f"{price:>8}", "green")
                print(f"{PAD}{index} │ {emoji} {card.name:<22}{price_col}")
                index += 1
            rule()
            print(f"{PAD}Wallet: {color(f'${default.wallet:.2f}', 'green')}")
            rule()

            # 🧠~ Allow the user to select a scratcher
            choice = input("\nSelect a scratcher (q to quit) > ")

            if choice.lower() == "q":
                say("Quitting...", "yellow")
                exit()

            if str(choice) not in collection:
                say("Please make a valid selection!", "red")
            else:
                purchase_valid = False

                while not purchase_valid:
                    try:
                        card = collection[choice].name
                        price = collection[choice].price

                        # 🧠~ Verify at least one unit of the selected card can be bought
                        if price > default.wallet:
                            say("You cannot afford this!", "red")
                            break

                        amount = input(
                            f"How many {card}s would you like to buy? "
                            f"({default.wallet // price:.0f} max | c to cancel): "
                        )

                        if amount == "c":
                            break

                        if not amount.isnumeric or int(amount) < 0:
                            say("Please enter a valid amount!", "red")
                            continue

                        amount = int(amount)

                        if (amount * price) > default.wallet:
                            say("You cannot afford this!", "red")
                            continue

                        cost = amount * price
                        default.wallet -= cost
                        default.spent += cost

                        spent = color(f"${cost:.2f}", "yellow")
                        left = color(f"${default.wallet:.2f}", "green")
                        print()
                        say(f"You purchased {amount} card(s) for {spent} leaving behind {left}")
                        purchase_valid = True
                        selection_valid = True
                        earnings = collection[choice].play(amount, default.wallet)
                        default.wallet += earnings
                        default.earned += earnings
                    except ValueError:
                        say("Please enter a valid value", "red")

                    except KeyboardInterrupt:
                        print()
                        say("Quitting...", "yellow")
                        exit()
        except ValueError:
            say("Please enter a valid value!", "red")

        except KeyboardInterrupt:
            print()
            say("Quitting...", "yellow")
            exit()

    # 🤖~ Hand this round's winnings back so the results screen can show them.
    return earnings


def menu():

    cashout = False
    while not cashout:
        # 🧠~ If the balance is below the cheapest card, end the game.
        if default.wallet < collection["1"].price:
            screen(
                "💀  BROKE",
                [
                    f"You went broke! Left with {color(f'${default.wallet:.2f}', 'red')}",
                    f"Spent {color(f'${default.spent:.2f}', 'yellow')}  ·  "
                    f"Earned {color(f'${default.earned:.2f}', 'green')}",
                ],
            )
            exit()

        # 🧠~ Select and play scratcher(s)
        earned = select_scratcher()

        # 🤖~ If the round dropped the wallet below the cheapest card, loop back
        # so the broke screen at the top ends the game.
        if default.wallet < collection["1"].price:
            continue

        # 🧠~ Check if the player would like to cashout
        try:
            # 🤖~ Fresh bordered results screen — winnings + balance only.
            screen(
                "🎰  RESULTS",
                [
                    f"Earned this round: {color(f'${earned:.2f}', 'green')}",
                    f"Wallet: {color(f'${default.wallet:.2f}', 'green')}",
                ],
            )

            valid_cashout_opt = False
            while not valid_cashout_opt:
                cashout_opt = input("\nWould you like to cashout? (y/n) > ")

                if cashout_opt.lower() == "y":
                    cashout = True
                    valid_cashout_opt = True
                elif cashout_opt.lower() == "n":
                    cashout = False
                    valid_cashout_opt = True
                else:
                    say("Invalid choice!", "red")

        except ValueError:
            say("Since you're unable to decide, the game will continue.", "yellow")
            continue
        except KeyboardInterrupt:
            print()
            say("Quitting...", "yellow")
            exit()

    # 🤖~ Cashed out — show the final status screen and quit.
    screen(
        "🤑  CASHED OUT",
        [
            f"Final balance: {color(f'${default.wallet:.2f}', 'green')}",
            f"Spent {color(f'${default.spent:.2f}', 'yellow')}  ·  "
            f"Earned {color(f'${default.earned:.2f}', 'green')}",
        ],
    )
    exit()


def main():
    menu()


main()
