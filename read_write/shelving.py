import shelve

with shelve.open("ShelfTest") as fruit:
    fruit["Orange"] = "A sweet, orange fruit"
    fruit["Apple"] = "Good for cider"
    fruit["Lemon"] = "A sour yellow fruit"
    fruit["Grape"] = "A sweet, purple fruit"
    fruit["Lime"] = "A sour green fruit"

    print(fruit["Lemon"])
    print(fruit["Grape"])

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["color"] = "red"
    bike["engine_size"] = 250

    print(bike["engine_size"])
    print(bike["color"])

    
    import shelve

with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
fruit["Orange"] = "A sweet, orange fruit"
fruit["Apple"] = "Good for cider"
fruit["Lemon"] = "A sour yellow fruit"
fruit["Grape"] = "A sweet, purple fruit"
fruit["Lime"] = "A sour green fruit"

print(fruit["Lemon"])
print(fruit["Lime"])

fruit["Lime"] = "Great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])

while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    description = fruit.get(shelf_key, "We don't have a " + shelf_key)
    print(description)

fruit.close()

print(fruit)

import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambles eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup

    ##Doesn't work to update###
    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list


with shelve.open("recipes", writeback=True) as recipes:
    # recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")


    for snack in recipes:
        print(snack, recipes[snack])
