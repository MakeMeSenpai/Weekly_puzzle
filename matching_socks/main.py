from math import ceil
from random import shuffle

# creates our socks
socks = [
  "green", "green", "green", "green", "green", "green", "green", "green", "green", "green",
  "black", "black", "black", "black", "black", "black", "black", "black", "black", "black",
  "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"
]

# this was added last, as to interate over this process 1,000 times
counts = []
for i in range(1000):
    # randomizes our socks
    shuffle(socks)
    # print(i, socks)

    # we then need to cycle threw to see when we get a sock
    count = 1
    ourSock = socks[0]
    while ourSock != socks[count]:
        count += 1
    
    # adds to counts
    counts.append(count)

# print(counts)
answer = sum(counts)/len(counts)
print("On Average you would need to grab", answer, "socks to get one pair that matches. But lets grab", ceil(answer), "just in case!")
