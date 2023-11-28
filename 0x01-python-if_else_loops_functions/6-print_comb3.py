#!/usr/bin/python3
for x in range(0, 10):
    for y in range(1, 10):
        if y > x and x != 8:
            print("{}{}".format(x, y), end=', ')
print("89")
