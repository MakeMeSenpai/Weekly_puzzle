from random import choice
"""I create a random configuration so that when comming up with a 
solution, any switch can match any light bulb during testing. This
problem was hard to translate to code, but why I think it's important
as finding out how to solve real world/challenging problems threw
 programming can help the world become a better place threw technology """

# Enough ranting, let's set the light bulbs to random value
values = [
    {"id": 1, "on": False, "heat": False},
    {"id": 2, "on": False, "heat": False},
    {"id": 3, "on": False, "heat": False}]
bulbA = choice(values)
values.remove(bulbA)
bulbB = choice(values)
values.remove(bulbB)
bulbC = values[0]

# matches our 3 switches to the lightbulbs
def match(id):
    if id == bulbA["id"]:
        return bulbA
    elif id == bulbB["id"]:
        return bulbB
    else:
        return bulbC
"""now this may seem a little redundant, but it's just to
    ensure we can match objects together without actually knowing
    what they are"""
switches = 3
bulbs = []
for switch in range(switches):
    bulbs.append(match(switch+1))

# turns lights on and off
def isOn(bulb):
    if bulb["on"]:
        bulb["heat"] = True
        bulb["on"] = False
        return bulb
    bulb["on"] = True
    return bulb

# To find out which one is which, we will turn on switch1 and switch2
isOn(bulbs[0])
isOn(bulbs[1])


# then turn off switch1 after 10 minutes causing heat - I'm not gonna make you wait 10 mins for a result, so I skipped the timer
isOn(bulbs[0])

'''So now when we match the bulbs, 
(switch1 = bulb[0], switch2 = bulb[1], switch3 = bulb[2])
lightbulbs are still bulbA, bulbB, bulbC
'''
a=b=c=""
#  we check for the off lightbulb that's hot
if bulbA == bulbs[0]:
    a = "Switch1 turns on BulbA."
if bulbB == bulbs[0]:
    a = "Switch1 turns on BulbB."
if bulbC == bulbs[0]:
    a = "Switch1 turns on BulbC."

#  the one left on is switch 2
if bulbA == bulbs[1]:
    b = "Switch2 turns on BulbA."
if bulbB == bulbs[1]:
    b = "Switch2 turns on BulbB."
if bulbC == bulbs[1]:
    b = "Switch2 turns on BulbC."

# leaving the one that's cold as switch3
if bulbA == bulbs[2]:
    c = "Switch1 turns on BulbA."
if bulbB == bulbs[2]:
    c = "Switch1 turns on BulbB."
if bulbC == bulbs[2]:
    c = "Switch1 turns on BulbC."

# finally we return our results
print("Results!", a, b, c)