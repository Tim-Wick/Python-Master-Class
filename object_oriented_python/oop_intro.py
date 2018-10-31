class Kettle(object):

    # Classes can also have consistent attributes across all instances
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

# Can add attributes to single instances of classes
kenwood.power = 1.5
print(kenwood.power)
# print(hamilton.power)

print("Switch to atomid power")
Kettle.power_source = "atomic"
print("Kettle power: ", Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print("kenwood power: ", kenwood.power_source)
print("hamilton power: ", hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
