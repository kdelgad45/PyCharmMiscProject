def get_tickets_purchase():
    number_tickets = input("How many tickets would you like to purchase (1-4)?")
    return int(number_tickets)

def sell_tickets():
    total_tickets = 20
    remaining_tickets = total_tickets
    total_buyers = 0
    while remaining_tickets > 0:
        print(f"Currently, {remaining_tickets} tickets are remaining.")
        try:
            number_tickets = get_tickets_purchase()

            if number_tickets < 1 or number_tickets > 4:
                print("Invalid number of tickets. You can buy between 1 and 4 tickets.")
            elif number_tickets > remaining_tickets:
                print(f"Not enough tickets remaining. Only {remaining_tickets} tickets are left.")
            else:
                remaining_tickets -= number_tickets
                total_buyers += 1
                print(f"Purchase successful! {remaining_tickets} tickets are now remaining.")
        except ValueError:(
                print("Invalid input. PLease enter a whole number."))

        print(f"\nAll tickeys have been sold! The total number of buyers are: {total_buyers}.")

sell_tickets()