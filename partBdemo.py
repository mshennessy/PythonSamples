# Sample code for paper C part b showing multiple (but not all) options
# G Hennessy CUS

import random

item_list=[]
item_prices=[]

# for test - make your life easier 
item_list=["apple","banana","orange"]
item_prices=[2.4,    1.7,     1.9]

print("Welcome to the shop")

# b i
# Boolean to control while loop
keepGoing = True
while keepGoing:   
    userItem=input("Enter item")
    if userItem.lower() == "stop":
        keepGoing = False
    else:   
        item_list.append(userItem)
        itemPrice=float(input("Enter price"))
        item_prices.append(itemPrice)
        # running total
        print("Your current total is €", sum(item_prices))

print("Grand total is €",sum(item_prices))
total = 0
for x in item_prices:
    total+=x

print("Total", total)
print(item_list,item_prices)

# b ii
# using random.choice()
print ("Random item is", random.choice(item_list))
# using random.randint()
#print ("Random item is", item_list[random.randint(1,len(item_list))-1])

# b iii
# Cheapest item
# 1 find min value in item_prices   ... min()
# 2 find the index of that min value (where it is in the list) ... list.index()
# 3 use the number from step 2 to find the corresponding item in item_list ... [minindex]

minPrice = min(item_prices)                  # Step 1
minPriceIndex = item_prices.index(minPrice)  # Step 2
cheapestItem=item_list[minPriceIndex]        # Step 3

print("Cheapest item is",cheapestItem)

# This is most expensive done in fewer lines (with the same steps)                 # Step 1
maxPriceIndex = item_prices.index(max(item_prices)) # Steps 1 and 2 
print("Most expensive item is",item_list[maxPriceIndex]) # Step 3 inside print()

# or all in 1 line ...
print("Most expensive item is",item_list[item_prices.index(max(item_prices))])