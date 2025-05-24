print("Welcome to Hurricane Box Office!")

#INPUTS
custName = input("Enter your first name: ") 
#USE input() TO GET TEXT FROM THE USER

numTickets = int(input("Hi, " + custName + "! How many tickets do you want? ")) 
#USE int(input()) TO GET WHOLE NUMBERS FROM THE USER.

#SADLY, input() CAN'T HANDLE COMMAS LIKE print() DOES, SO WE HAVE TO USE + SIGNS AND ADD THE SPACES OURSELVES
                                                                                
ticketPrice = float(input("Enter the ticket price: $")) 
#USE float(input()) TO GET DECIMAL NUMBERS FROM THE USER

#ALGORITHM
subTotal = numTickets * ticketPrice
HST = 0.13 * subTotal
totalPrice = subTotal + HST

#WHY DIDN'T I SEE ANY OUTPUT?
print("Your subtotal is $" + str(subTotal))
print("HST was $" + str(HST))
print("Total price was $" + str(totalPrice))