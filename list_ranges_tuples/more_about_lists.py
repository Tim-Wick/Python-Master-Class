list_1 = []
list_2 = list()
# Both create empty list

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))
if list_1 == list_2:
    print("The lists are equal")

print(list("The lists are equal"))
# makes list entry of every character

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
print(even)
# Both refer to same list so action changes both #

print(another_even is even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
# makes list of list #

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
