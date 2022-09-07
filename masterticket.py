SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# Create the calculate_price function. It takes a number of tickets and returns number_of_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    # Create a new constant for the 2 dollar service charge
    #Add the service charge to our result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run this code continuously until all tickets are sold
while tickets_remaining >= 1:

# Output how many tickets are remaining using the tickets_remaining variable
    print("There are {} tickets remaining.".format(tickets_remaining))

# Gather the user's name and assign it to a new variable
    name = input("Please enter your name. ")

# Prompt the user by name and ask how many tickets they would like
    num_tickets = input("How many tickets would you like, {}? ".format(name))

# Expect a ValueError to happen and handle it appropriately...remember to test it out!
    try:
        num_tickets = int(num_tickets)
# Raise a ValueError if the request is for more tickets than are available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
# Include the error text in the output
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:
# Calculate the price (number of tickets * price) and assign it to a variable
        amount_due = calculate_price(num_tickets)
    
# Output the price to the screen
        print("Your total is ${}".format(amount_due))
    
# Prompt user if they want to proceed. Y/N?
    
# If they want to proceed
# print out to the screen "SOLD!" to confirm purchase
# TODO: Gather credit card information
# and then decrement the number of ticket remaining by the number of tickets purchased
# Otherwise...
# Thank them by name
        response = input("Would you like to proceed? (Enter Y/N)")
        if response.lower() == 'y':
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you {}!".format(name))
    
# Notify user that the tickets are sold out
print("Sorry, all the tickets have been sold out!")