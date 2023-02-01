# PROGRAM TO CALCULATE MONTHLY BUDGET 
income = int(input("Enter your monthly Budget for home: ")) # Get Budget from user
expenses = {} # create dictionary to add expense
while True: # using while loop for get items till user want
    items = input("Enter expense items (or 'done' to stop): ")
    if items == 'done': # if user print done loop will break
        break
    expense = int(input(f"Enter amount for {items}: "))
    expenses[items] = expense # store in dictionary 
total_expenses = sum(expenses.values())  # add all item amount using values()method
bal = income - total_expenses # check diff from total expenses("all item amount")
print(f"TOTAL INCOME ={income}") 

print("EXPENSES: ") 
for items, expense in expenses.items(): # display item with amount
    print(f"{items} = {expense}")
dis="AFTER EXPENSES"
 
if income > total_expenses: # income is greater than expenses
    print(dis)
    print(f"balance amount is {bal} you can save this money")
if income == total_expenses: # Income equal to expenses
    print(dis) 
    print(f"your Budget is correct equal to expense, but try save money")
if income < total_expenses: # income is less than expenses
    print(dis)
    print(f"shortage of money ={bal}")

