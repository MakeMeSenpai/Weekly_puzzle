# the distance is 100%
destination = 100

# cars can travel 50% of the way
class Car:
    def __init__(self):
        self.fuel = 50

# the car that needs to make it to it's destination
vipCar = Car()
# keeps track of our other cars fuel levels
fuel_for_temp = vipCar.fuel
# we set a count for every car needed -including the VIP(+1)
count = 1

# while we haven't hit our destination
while destination > 0:
    # Add a car to the trip
    count += 1
    # We will travel half the distance of what fuel our cars have
    fuel_for_temp = fuel_for_temp/2
    # we create a car that will refill our VIP's
    tempCar = Car()
    # we then set how much gas each car will have
    tempCar.fuel = fuel_for_temp
    print("temp fuel", tempCar.fuel)
    # We then give what gas we have left to our vip
    vipCar.fuel = vipCar.fuel/2 + tempCar.fuel
    print("vip fuel", vipCar.fuel)
    # And then travel as far as we can
    destination -= vipCar.fuel
    print("We are", destination, "away from our destination")
# Finally we print how many cars we needed in order to get to our destination
print(count)
