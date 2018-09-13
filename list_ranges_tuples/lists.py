ip = input("Please enter an IP address: ")
print(ip.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of life"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()
print(numbers)
# .sort does not return anything, just sorts object
print(sorted(numbers))
# sorted returns object

number_in_order =  sorted(numbers)

if numbers == number_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")
