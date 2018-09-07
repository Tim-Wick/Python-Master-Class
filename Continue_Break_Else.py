#####continue and break usage#####

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    #skips item using continue
    if item == "spam":
        #continue
        #break skips the remainder of the items
        break
    print("Buy " + item)

#####practicing with break#####

meal = ["egg", "bacon", "spam", "sausages"]

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break

if nasty_food_item:
    print("Can I have anything without spam in it?")

#Bug; if no spam, nasty_food_item is never defined

#####fixing previous bug#####

meal = ["egg", "bacon", "spam", "sausages"]
#fixes previous bug and initializes nasty_food_item
nasty_food_item = ""
for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
#break supersedes the else
else:
    print("I'll have a plate of that then")
if nasty_food_item:
    print("Can I have anything without spam in it?")

#####practice questions#####

#print numbers up to divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

#prints number BUT those divisible by 3 or 5
for number in range(20):
    if number % 3 == 0 or number % 5 == 0:
        continue
    print(number)
