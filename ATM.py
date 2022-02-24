import sys

#This is the account balance 
account_balance = float(500.25)

def print_balance():
  """This is the printbalance function, when called it prints the account balance"""
  print(account_balance)

def deposit(amount):
  """Deposit function, it prints the deposit statement and displays the amount deposited and new balance"""
  #This declairs the account_balance variable to global. It is no longer local to the function.
  global account_balance
  print("Deposit was $%.2f, current balance is $%.2f" % (amount, account_balance + amount))
  account_balance = account_balance + amount
  print(amount)

def withdrawal(amount):
  """Withdraw function - this is to do the action of removing funds, also lets the user know
     if they try to take out more then they have in thier balance"""
  #This declairs the account_balance variable to global. it is no longer local to the function.
  global account_balance
  if amount > account_balance:
      print("$%.2f is greater than your account balance of $%.2f" % (amount, account_balance))
  else:
      print("Withdrawal amount was $%.2f current balance is $%.2f" % (amount, account_balance - amount))
      account_balance = account_balance - amount

def print_summary():
  #this function prints out the thank you message
    print('Thank you for banking with us.')

#This takes the users response to "What would you like to do?"
user_response = input ("What would you like to do?\n")

#The user has four choices
#D = deposit
#W = withdrawl
#B = print balance
#Q = quit

#This prompts the script to start the deposit function when user inputs "D"
if user_response == "D":
  #Funfact: Deposit is spelt wrong here, but that's how codio had it, so I had to match it
  deposit_amount = float(input("How much would your like to deposite?\n")) 
  deposit(deposit_amount)

#This has the script call the withdrawal function when user inputs "W"
elif (user_response == "W"):
  withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  withdrawal(withdrawal_amount)

#This has the script call the print_balance function when user inputs "B"
elif (user_response == "B"):
  print_balance()

#This has the script call the print_summary function when the user inputs "Q"
elif user_response =='Q':
  print_summary()