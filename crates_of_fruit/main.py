from random import choice
values = [
    {"label": "", "contents": "apples"},
    {"label": "", "contents": "oranges"},
    {"label": "", "contents": "both"}
]

""" this code works for randomizing the labels to never match
what's inside the crate since all the crates are labeled wrong. 
However, there must be some edge case that I'm not seeing because
when running $python3 main we will sometimes get stuck printing apples"""
i = 2
choices = ["apples", "oranges", "both"]
while i != -1:
    label = choice(choices)
    if label != values[i]["contents"]:
        values[i]["label"] = label
        choices.remove(label)
        i -= 1

# this will be used later to compare our answer
print("_____Broken Labels_____")
print(values)

# we grab an item from the container labeled both
for i in range(len(values)):
    if values[i]["label"] == "both":

        # if the both crate contains apples. 
        if values[i]["contents"] == "apples":
            # then that means that the crate labeled apples has oranges
            # and the crate labeled oranges has both
            if values[i+1]["label"] == "apples":
                values[i+1]["label"] = "oranges"
                values[i+2]["label"] = "both"
            # then we set our crate labeled both to apples
            values[i]["label"] = "apples"
            break # we then break the loop

        # otherwise the crate will contain oranges, since all are labels incorrectly
        else:
            # then this means the crate labeled oranges is apples
            #  and the crate labeled apples is has both
            if values[i-1]["label"] == "oranges":
                values[i-1]["label"] = "apples"
                values[i+1]["label"] = "both"
            # note that we would need else if statements if we didn't know the indexes
            values[i]["label"] = "oranges"
            break

# Now we compare the results with the broken labels
print("_____Fixed labels_____")
print(values)

# yay! we did it. Run with $python3 main.py in crates_of_fruit directory