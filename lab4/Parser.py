#!/usr/bin/env python3
# Dominik Matijaca 0036524568

grammar = {
    'S': ["aAB", "bBA"],
    'A': ["bC", "a"],
    'B': ["ccSbc", ""],
    'C': ["AA"]
}

data = input()

def case(n, c):
    for i in c:
        if i.islower():
            if n >= len(data) or data[n] != i:
                return -1
            n += 1
        else:
            n = parse(n, i)
            if n == -1:
                return -1

    return n

def parse(n, x):
    print(x, end="")

    for i in grammar[x]:
        r = case(n, i)
        if r != -1:
            return r

    return -1

print("\n" + ("NE" if parse(0, next(iter(grammar.keys()))) != len(data) else "DA"))