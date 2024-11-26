while True:
    num_tickets = input("How many tickets do you need? ")
    try:
        num_tickets = int(num_tickets)
    except ValueError as e:
        print(f"Error {e}. Please try again")
    else:
        for i in range(num_tickets):
            print(f"Ticket {i+1} is printing")
        break