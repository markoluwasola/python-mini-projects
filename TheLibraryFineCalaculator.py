# Library Fine Calculator
print("Welcome to VS library, I believe you have a book to return.")
while True:
    late = input("Is the book you are returning late? (yes/no): ").strip().lower()
    if late == "yes" or late == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no' Try again.")

if late == "no":
        print("Thank you for returning the book on time! No fine is due. We hope to see you again soon!")
else:
    while True:
        reference = input("Is the book you are returning a reference book? (yes/no): ").strip().lower()
        if reference == "yes" or reference == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    while True:
        days_late = input("How many days late is the book? ")
        try:
            days_late = int(days_late)
            break
        except ValueError:
            print("Invalid input, Please enter a numeric value. Try again.")
    
    if days_late >= 1 and days_late <= 5:
        fine1 = days_late * 0.50
        print("Thank you for using VS library, Your fine for late return is: $", round(fine1,2))
    elif days_late >= 6 and days_late <= 10: 
        fine2 = days_late * 1.00
        print("Thank you for using VS library, Your fine for late return is: $", round(fine2,2))
    elif days_late > 10 and reference == "yes":
        fine3 = days_late * 4.00
        print("Thank you for using VS library, Your fine for late return is: $", round(fine3,2))
    elif days_late > 10 and reference == "no":
        fine4 = days_late * 2.00
        print("Thank you for using VS library, Your fine for late return is: $", round(fine4,2))

#calculate the fine for a late book return based on the following rules:
#1. If the book is returned on time, there is no fine.
#2. If the book is returned late, the fine is calculated based on the number of days late and whether the book is a reference book or not:
#   a. For non-reference books:
#      - If the book is returned 1-5 days late, the fine is $0.50 per day.      
#      - If the book is returned 6-10 days late, the fine is $1.00 per day.
#      - If the book is returned more than 10 days late, the fine is $2.00 per day.
#   b. For reference books:     
#      - If the book is returned 1-5 days late, the fine is $0.50 per day.
#      - If the book is returned 6-10 days late, the fine is $1.00 per day.
#      - If the book is returned more than 10 days late, the fine is $
#4.00 per day.       
