
grocery_item = {} # defines empty dictionary

grocery_history = [] # defines empty list

#Variable used to check if the while loop condition is met
stop = 'go'

while stop != 'q': #creation of while loop as long as does not equal q
    item_name = input('item name: ') #accept item name
    quantity = input('Quantity purchased: ')#accept purchased quanitity
    cost = input('Price per item: ') #accept item price
  
    #This is the number and price entered by the user.
    grocery_item['name'] = item_name
    grocery_item['number'] = int(quantity)
    grocery_item['price'] = float(cost)
    #Adds the item to the grocery_history list
    grocery_history.append(grocery_item.copy())
    #Asks the user if they are done adding items to the list
    stop = input("Would you like to enter another item? \nType 'c' for continue or 'q' to quit :")

grand_total = 0

for item in (grocery_history):
  #This calculates the cost for the grocery_item.
  item_total = item['number'] * item ['price'] 
  grand_total += item_total
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  item_total = 0
print('Grand total: $%.2f' % grand_total)
