import random
from time import sleep


class ScratchOff:
  def __init__(self, name, price, jackpot) -> None:
    self.name = name
    self.price = price
    self.jackpot = jackpot

  def play(self, amount, cash): # Values are assumed to be clean and sanitized

    # Rolling the odds
    print("\nScratching card(s)...")
    sleep(5)
    earnings = 0

    # Initializing the loop
    for scratcher in range(amount):

      # Roll for jackpot chance to determine if jackpot is eligible
      jackpot_high = random.randint(0,100)
      jackpot_low = random.randint(0,100)

      # Establish win-lose brackets and weights for each
      winning_brackets = ["High Gain", "Mid Gain", "Low Gain"]
      winning_brackets_weight = [10, 20, 70]
      losing_brackets = ["High Loss", "Mid Loss", "Some Loss", "Low Loss"]
      losing_brackets_weight = [92, 5, 2, 1]

      # Rolling for win-lose bracket
      win_bracket = random.choices(winning_brackets, weights=winning_brackets_weight, k=1)[0]
      lose_bracket = random.choices(losing_brackets, weights=losing_brackets_weight, k=1)[0]

      # Checking if jackpot high-low match and result in jackpot chance
      if jackpot_high != jackpot_low:
        if win_bracket == "High Gain":
          max_gains = (self.jackpot * .75)
          min_gains = (self.jackpot * .50)
        elif win_bracket == "Mid Gain":
          max_gains = (self.jackpot * .50)
          min_gains = (self.jackpot * .25)
        else:
          max_gains = (self.jackpot * .25)
          min_gains = (self.jackpot * 0)
      else:
        if win_bracket == "High Gain":
          max_gains = (self.jackpot * 1)
          min_gains = (self.jackpot * .75)
        elif win_bracket == "Mid Gain":
          max_gains = (self.jackpot * .75)
          min_gains = (self.jackpot * .25)
        else:
          max_gains = (self.jackpot * .25)
          min_gains = (self.jackpot * 0)

      # Working with lose bracket
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

      # Calculating value won and amount loss
      amount_won = random.uniform(min_gains, max_gains)
      percent_loss = random.randint(min_losses, max_losses)
      actual_won = amount_won - (amount_won * (percent_loss/100))

      # print("*" * 20)
      # print("DEBUG")
      # print(f"Current Earnings: {earnings}")
      # print(f"Won: ${amount_won:.2f} |  Loss Percentage: {percent_loss}% | Actual: ${actual_won:.2f}")
      # print("*" * 20)

      # Making sure value isn't negative
      if actual_won < 0:
        actual_won = 0

      # Adding won amount to earnings
      earnings += actual_won

    print(f"You earned ${earnings:.2f}!\n")
    sleep(5)
    return float(earnings + cash)
