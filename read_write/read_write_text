jabber = open("C:\\Users\\Tim\\Desktop\\sampletext.txt","r")

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end="")

jabber.close()

with open("C:\\Users\\Tim\\Desktop\\sampletext.txt","r") as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

with open("C:\\Users\\Tim\\Desktop\\sampletext.txt","r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()

cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", "w") as city_files:
    for city in cities:
        print(city, file=city_files)

cities = []

with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip("\n"))

print(cities)
for city in cities:
    print(city)
    
    
with open("C:\\Users\\Tim\\Desktop\\sampletext.txt", "a") as jabber:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=jabber)
        print("-" * 20, file=jabber)
