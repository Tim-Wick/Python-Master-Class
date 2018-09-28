fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for cider",
         "lemon": "a sour, yellow fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green fruit"}

print(fruit)
print(fruit["lemon"])

###can mix types of values###
bike = {"make": "Honda", "model": "250 dream", "color": "red", "engine size": 250}
print(bike["engine size"])
print(bike["color"])

fruit["pear"] = "an odd shaped apple"
print(fruit)
###need to put new key in square brackets###
###can overwrite keys with new values. Even if in same entry###

fruit["pear"] = "great with tequila"
print(fruit)

### "del" deletes. Can delet whole dictionary if no enry is specified###

del fruit["lemon"]
print(fruit)

## can empty dictionary with ".clear"

fruit.clear()
print(fruit)

## will return error if key does not exist###

fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for cider",
         "lemon": "a sour, yellow fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green fruit"}

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        descritiption = fruit.get(dict_key)
        print(descritiption)
    else:
        print("Don't have a " + dict_key)

### get gets value of specified key. Return none if doesn't exist vs an error###

fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for cider",
         "lemon": "a sour, yellow fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green fruit"}

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    descritiption = fruit.get(dict_key, "We don't have a " + dict_key)
    print(descritiption)

for snack in fruit:
    print(fruit[snack])

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print("=" * 40)

## Items added to plain dictionaries are not in any guaranteed order ###

ordered_keys = list(fruit.keys())
ordered_keys.sort()

ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

fruit = {"orange": "a sweet, citrus fruit",
         "apple": "good for cider",
         "lemon": "a sour, yellow fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green fruit"}

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "Not nice with ice cream"
print(fruit_keys)

print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))

my_list = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

new_string = ""
for c in my_list:
    new_string += c + ", "

### .join is more efficient###
new_string = ", ".join(my_list)
other_new_string = ", ".join(letters)
number_string = " mississippi ".join(numbers)

print(new_string)
print(other_new_string)
print(number_string)
