locations = {0: "You're at home",
             1: "You're at Road",
             2: "You're at Hill",
             3: "You're at Building",
             4: "You're at Valley",
             5: "You're at Forest"}

directions = [{"Q": 0},
              {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
              {"N": 5, "Q": 0},
              {"W": 1, "Q": 0},
              {"N": 1, "W": 2, "Q": 0},
              {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    available_exits = ", ".join(directions[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    travel = input("Available exits are " + available_exits + " w ").upper()
    print()
    if travel in directions[loc]:
        loc = directions[loc][travel]
    else:
        print("You cannot go in that direction")
