#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 113:
        i = i + 1
        i = i - 1
    print("{:c}".format(i), end="")

