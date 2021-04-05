#!/usr/bin/env python3
# Dominik Matijaca 0036524568

tests = [i.split(",") for i in input().split("|")]
states = input().split(",")
words = input().split(",")
accept = input().split(",")
start = input()

flow = {}

for i in states:
    flow[i] = {j: [] for j in words}
    flow[i]["$"] = [i]

while True:
    try:
        a, b = [i.split(",") for i in input().split("->")]
        
        if b[0] != "#":
            flow[a[0]][a[1]] += b

    except EOFError:
        break

for case in tests:
    q = [start]

    for word in case:
        x = set()

        while q:
            i = q.pop(0)
            x.add(i)
            q += [i for i in flow[i]["$"] if i not in x]
        
        print(','.join(sorted(x)) if x else "#", end = "|")

        next = set()
        for i in x:
            next |= set(flow[i][word])
        
        q = list(next)
    
    x = set()

    while q:
        i = q.pop(0)
        x.add(i)
        q += [i for i in flow[i]["$"] if i not in x]
    
    print(','.join(sorted(x)) if x else "#")