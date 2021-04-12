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
    print(label)
    if label != values[i]["contents"]:
        values[i]["label"] = label
        choices.remove(label)
        i -= 1

print(values)