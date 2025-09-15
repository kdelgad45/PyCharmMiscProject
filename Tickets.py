# Create the starting code  
def get_tickets_purchase():
    # Ask the user on how many tickets they want to buy/
    num_tickets = input("Hello how many tickets would you like to buy you can only buy at least up to 4 tickets.)?")  
    return int(num_tickets)

# Create the ticket selling process
def sell_tickets():
    # Create variables
    total_tickets_bought = 10
    remaining_tickets_bought = total_tickets_bought
    total_buyers_bought = 0
    while remaining_tickets_bought > 0:
        print(f"Currently, {remaining_tickets_bought} tickets are remaining.")
        try:
            num_tickets = get_tickets_purchase()

            if num_tickets < 1 or num_tickets > 4:
                print("Invalid number of tickets. You can buy between 1 and 4 tickets.")
            elif num_tickets > remaining_tickets:
                print(f"Not enough tickets remaining. Only {remaining_tickets_bought} tickets are left.")
            else:
                remaining_tickets_bought -= num_tickets
                total_buyers_bought += 1
                print(f"Purchase successful! {remaining_tickets_bought} tickets are now remaining.")
        except ValueError:(
                print("Invalid input. Please enter a whole number."))

        print(f"\nAll tickeys have been sold! The total number of buyers are: {total_tickets_bought}.")

# Start the application
sell_tickets()
