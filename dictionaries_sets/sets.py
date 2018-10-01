### Sets are mutable, unordered, and without duplicates ###

farm_animals = {"Sheep", "Cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

wild_animals = set(["lion", "tiger", "panther", "elephant"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

### Two different ways to create sets ###

farm_animals.add("horse")
print(farm_animals)

## Need to use set command to create empty set ###

## Can make sets w/ lists, tuples, or ranges ###

even = set(range(0, 40, 2))
print(even)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuples = (4, 6, 9, 16, 25)
squares = set(squares_tuples)
print(squares)
print(len(squares))

### .union combines but no duplicates ###

print(even.union(squares))
print(len(even.union(squares)))

print("=" * 40)

### .intersection/& prints only values in both sets ###

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

## can subtract sects. A-B = takes things out of A that are also in B ###

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("Squares minus even")
print(squares.difference(even))
print(squares - even)

print("=" * 40)

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

## .symmetric_difference takes out numbers that are in both ###

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(squares.symmetric_difference(even))

## remove items from set w/ .remove or .discard # .remove throws error if item does not exist, .discard does not ###

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
try:
    squares.remove(8)
except KeyError:
    print("The item is not a member of the set")

## a set is a subset if it contains all items in another set. superset contains all the other set's members ###

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")


## frozen sets are immutable ###

even = frozenset(range(0, 100, 2))

print(even)
#even.add(3)

get_vowels = set(input("Please type a sentence: "))
vowels = {"a", "e", "i", "o", "u", " "}

print(sorted(get_vowels - vowels))
