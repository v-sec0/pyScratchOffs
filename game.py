from Player import Player
from ScratchOff import ScratchOff

# Define scratch-offs
low = ScratchOff("Poor Man's Delight", 9.99, 250)
mid = ScratchOff("Money Multiplier", 19.99, 500)
high = ScratchOff("Uncle Sam Grand Slam", 49.99, 1000)
collection = {"1": low, "2": mid, "3": high}

# Define player settings
default = Player(100.00, 0.00, 0.00)


def list_scratchers():

    index = 1
    print("=" * 48)
    for scratcher in collection:
        print(
            f"ID: {index} | Name: {collection[scratcher].name} | Price: ${collection[scratcher].price}"
        )
        index += 1
    print("=" * 48)


def select_scratcher():

    print(
        f"Current Balance: ${default.wallet:.2f}. You have enough to afford the cheapest card!"
    )

    selection_valid = False
    earnings = 0

    while not selection_valid:
        try:
            choice = input("Please select a scratcher via ID (q to quit): ")

            if choice.lower() == "q":
                print("Quitting...")
                exit()

            if str(choice) not in collection:
                print("Please make a valid selection!")
            else:
                purchase_valid = False

                while not purchase_valid:
                    card = collection[choice].name
                    price = collection[choice].price

                    amount = input(
                        f"How many {card}s would you like to buy? ({default.wallet // price:.0f} max | c to cancel): "
                    )

                    if amount == "c":
                        break

                    if not amount.isnumeric or int(amount) < 0:
                        print("Please enter a valid amount!")
                        continue

                    amount = int(amount)

                    if (amount * price) > default.wallet:
                        print("You cannot afford this!")
                        continue

                    cost = amount * price
                    default.wallet -= cost
                    default.spent += cost

                    print(
                        f"\nYou purchased {amount} card(s) for ${cost:.2f} leaving behind ${default.wallet:.2f}"
                    )
                    purchase_valid = True
                    selection_valid = True
                    earnings = collection[choice].play(amount, default.wallet)
                    default.wallet += earnings
                    default.earned += earnings

        except ValueError:
            print("Please enter a valid value!")

        except KeyboardInterrupt:
            print("\nQuitting...")
            exit()


def menu():

    while True:
        # If balance is less than the cost of the cheapest card, end game.
        if default.wallet < collection["1"].price:
            print(f"\nYou went broke! You were left with ${default.wallet:.2f}!")
            print(
                f"You spent a total of ${default.spent:.2f} and earned a total of ${default.earned:.2f}\n"
            )
            exit()
        # List scratchers
        list_scratchers()
        # Select and play scratcher(s)
        select_scratcher()


def main():
    menu()


main()
