TICKET_PRICE = 10
SERVICE_PRICE = 2
tickets_remaining = 100  

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_PRICE
    
while tickets_remaining >= 1:   
    # Output how many tickets are remaining 
    print("\nThere are {} tickets remaining".format(tickets_remaining))
    
    # Gather the user's name and assign it to a new variable
    name = input("What's your name?  ")
    
    try:
        number_of_tickets = int(input("Hey, {}! How many tickets would you like?  ".format(name)))
        if number_of_tickets > tickets_remaining:
            raise ValueError("We have only {} tickets for your request".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We had an issue. {} Please, try again...".format(err))
    else:
        total_price = calculate_price(number_of_tickets)
        print("\nOk then. The total price is ${} ".format(total_price))
        print("We add ${} for the service, ok? ".format(SERVICE_PRICE))
        check = input("Would you like to proceed? [Y or N]  ")
        
        # step to check if the answer is a valid answer
        while check.lower() != "y" and check.lower() != "n":
            check = input("Oh no! That's not  valid answer!\nPlease, try again only with Y or N! ")
        
        # step to proceed with the decision of selling or not the tickets
        if check.lower() == "y":
            print("Sold! The {} tickets are already yors!".format(number_of_tickets))
            tickets_remaining -= number_of_tickets
        elif check.lower() == "n":
            print("Thank you anyway,{}! See you later!".format(name))
print("Sorry, but all the tickets are sold out :(")