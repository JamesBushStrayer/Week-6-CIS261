# James Alan Bush (SU200619708)
# CIS261 Week - 6 Invoice Line Item Calculator Application

def get_price():
  while True:
    try:
      price = float(input("Enter price: "))
      return price
    except ValueError:
      print("Invalid decimal number. Please try again.")


def get_quantity():
  while True:
    try:
      quantity = int(input("Enter quantity: "))
      return quantity
    except ValueError:
      print("Invalid integer. Please try again.")


def display_heading():
  print("The Invoice Line Item Calculator")


def main():
  display_heading()
  while True:
    price = get_price()
    quantity = get_quantity()
    print(f"PRICE: ${price:.2f}")
    print(f"QUANTITY: {quantity}")
    total = price * quantity
    print(f"TOTAL: ${total:.2f}")

    another_item = input("Enter another line item? (y/n): ").lower()
    if another_item == 'n':
      print("Bye!")
      break


if __name__ == "__main__":
  main()
