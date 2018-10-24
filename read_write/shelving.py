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
