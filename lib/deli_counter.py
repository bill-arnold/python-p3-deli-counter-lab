# deli_counter.py

def line(katz_deli):
    """Show everyone their current place in the line."""
    if not katz_deli:
        print("The line is currently empty.")
    else:
        current_line = ", ".join(f"{index + 1}. {customer}" for index, customer in enumerate(katz_deli))
        print(f"The line is currently: {current_line}")

def take_a_number(katz_deli, name):
    """Add a new customer to the end of the line and print their position."""
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    """Call out the next person in line and remove them from the front."""
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")

# Example usage:
katz_deli = []

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")

line(katz_deli)

now_serving(katz_deli)

line(katz_deli)

take_a_number(katz_deli, "Matz")

line(katz_deli)

now_serving(katz_deli)

line(katz_deli)
