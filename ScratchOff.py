import random
from time import sleep


class ScratchOff:
    def __init__(self, name, price, jackpot) -> None:
        self.name = name
        self.price = price
        self.jackpot = jackpot

    def play(self, amount, cash):  # 🧠~ Values are assumed to be clean and sanitized

        # 🤖~ Short "scratching" animation. end="" keeps the cursor on the line;
        # flush=True shows each dot immediately instead of buffering the line.
        print()
        print("Scratching", end="", flush=True)
        for _ in range(6):
            sleep(0.4)
            print(".", end="", flush=True)
        print()

        # 🧠~ Rolling the odds
        earnings = 0

        # 🧠~ Initializing the loop
        for scratcher in range(amount):
            # 🧠~ Roll for the jackpot chance to determine if a jackpot is eligible
            jackpot_high = random.randint(0, 100)
            jackpot_low = random.randint(0, 100)

            # 🧠~ Establish the win/lose brackets and weights for each
            winning_brackets = ["High Gain", "Mid Gain", "Low Gain"]
            winning_brackets_weight = [10, 20, 70]
            losing_brackets = ["High Loss", "Mid Loss", "Some Loss", "Low Loss"]
            losing_brackets_weight = [92, 5, 2, 1]

            # 🧠~ Rolling for the win/lose bracket
            win_bracket = random.choices(
                winning_brackets, weights=winning_brackets_weight, k=1
            )[0]
            lose_bracket = random.choices(
                losing_brackets, weights=losing_brackets_weight, k=1
            )[0]

            # 🧠~ Check if the jackpot high/low rolls match for a jackpot chance
            if jackpot_high != jackpot_low:
                if win_bracket == "High Gain":
                    max_gains = self.jackpot * 0.75
                    min_gains = self.jackpot * 0.50
                elif win_bracket == "Mid Gain":
                    max_gains = self.jackpot * 0.50
                    min_gains = self.jackpot * 0.25
                else:
                    max_gains = self.jackpot * 0.25
                    min_gains = self.jackpot * 0
            else:
                if win_bracket == "High Gain":
                    max_gains = self.jackpot * 1
                    min_gains = self.jackpot * 0.75
                elif win_bracket == "Mid Gain":
                    max_gains = self.jackpot * 0.75
                    min_gains = self.jackpot * 0.25
                else:
                    max_gains = self.jackpot * 0.25
                    min_gains = self.jackpot * 0

            # 🧠~ Working with the lose bracket
            if lose_bracket == "High Loss":
                max_losses = 100
                min_losses = 75
            elif lose_bracket == "Mid Loss":
                max_losses = 74
                min_losses = 50
            elif lose_bracket == "Some Loss":
                max_losses = 49
                min_losses = 25
            else:
                max_losses = 24
                min_losses = 0

            # 🧠~ Calculating the value won and the amount lost
            amount_won = random.uniform(min_gains, max_gains)
            percent_loss = random.randint(min_losses, max_losses)
            actual_won = amount_won - (amount_won * (percent_loss / 100))

            # print("*" * 20)
            # print("DEBUG")
            # print(f"Current Earnings: {earnings}")
            # print(f"Won: ${amount_won:.2f} |  Loss Percentage: {percent_loss}% | Actual: ${actual_won:.2f}")
            # print("*" * 20)

            # 🧠~ Making sure the value isn't negative
            if actual_won < 0:
                actual_won = 0

            # 🧠~ Adding the won amount to earnings
            earnings += actual_won

        # 🤖~ Brief pause for suspense, then hand the total to the results screen.
        sleep(1)
        return float(earnings)
