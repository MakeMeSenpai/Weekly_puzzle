# there is a 66.6% chance, we have the wrong bag. but lets make an algorithm to prove this
from random import randint
one = 0
two = 0
three = 0

print("Individual Cases:")
# we will test 10,000 cases
for i in range(10000):
    choice = randint(1, 3)
    if 1 == choice:
        one += 1
    elif 2 == choice:
        two += 1
    else:
        three += 1
    # displays each cases data
    print(str(i) + " " + str(choice))

# gets the average score


print("Results")
print("Bag 1:" + str(one),"Bag 2:" + str(two),"Bag 3:" + str(three))
print("However, because we choose a bag with a white marble, this changes the results")
print("Wrong Bag:" + str(one), "Correct Bag:" + str(two + three))
