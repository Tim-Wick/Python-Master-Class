string = "1234567890"

for char in string:
    print(char)

#Duplicating code essentially running behind for loop##
my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))

for char in string:
    print(char)

for char in iter(string):
    print(char)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_iterator = iter(numbers_list)

for i in range(0, len(numbers_list)):
    next_item = next(my_iterator)
    print(next_item)
