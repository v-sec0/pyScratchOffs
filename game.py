from ScratchOff import ScratchOff

# Define scratch-offs
low = ScratchOff("Poor Man's Delight", 9.99, 250)
mid = ScratchOff("Money Multiplier", 19.99, 500)
high = ScratchOff("Uncle Sam Grand Slam", 49.99, 1000)
collection = { "1": low, "2": mid, "3": high }

# Game settings
starting_balance = 100

def list_scratchers(cash):

  if cash < collection["1"].price:
    print(f"\nYou went broke! You were left with ${cash:.2f}!")
    exit()

  index = 1
  print("=" * 48)
  for scratcher in collection:
    print(f"ID: {index} | Name: {collection[scratcher].name} | Price: ${collection[scratcher].price}")
    index += 1
  print("=" * 48)

def select_scratcher(cash):

  print(f"Current Balance: ${cash:.2f}. You have enough to afford the cheapest card!")

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

          amount = input(f"How many {card}s would you like to buy? ({cash//price:.0f} max | c to cancel): ")

          if amount == "c":
            break

          if not amount.isnumeric or int(amount) < 0:
            print("Please enter a valid amount!")
            continue

          amount = int(amount)

          if (amount * price) > cash:
            print("You cannot afford this!")
            continue

          cost = (amount * price)
          remaining_balance = cash - cost

          print(f"\nYou purchased {amount} card(s) for ${cost:.2f} leaving behind ${remaining_balance:.2f}")
          purchase_valid = True
          selection_valid = True
          earnings = collection[choice].play(amount, remaining_balance)

    except ValueError:
      print("Please enter a valid value!")

    except KeyboardInterrupt:
      print("\nQuitting...")
      exit()

  return earnings

def menu(cash):
  list_scratchers(cash)
  earnings = select_scratcher(cash)
  menu(earnings)

def main():
  menu(starting_balance)

main()
