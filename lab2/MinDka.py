#!/usr/bin/env python3
# Dominik Matijaca 0036524568

states = input().split(",")
words = input().split(",")
accept = input().split(",")
start = input()

flow = {}

for i in states:
    flow[i] = {j: None for j in words}

while True:
    try:
        i, n = input().split("->")
        s, w = i.split(",")
        flow[s][w] = n

    except EOFError:
        break

avail = set()
q = [start]

while q:
    c = q.pop(0)

    if c in avail:
        continue

    avail.add(c)

    for k, v in flow[c].items():
        q.append(v)

states = [i for i in states if i in avail]
accept = [i for i in accept if i in avail]

groups = []
next = [[i for i in states if i not in accept], list(accept)]

def find(x):
    global groups
    for i in range(len(groups)):
        if x in groups[i]:
            return i

while len(groups) != len(next):
    groups = next
    next = []

    for g in groups:
        splits = [[] for _ in range(len(groups) ** len(words))]

        for i in g:
            index = 0

            for j in words:
                index *= len(groups)
                index += find(flow[i][j])
            
            splits[index].append(i)
        
        for i in splits:
            if len(i):
                next.append(i)

groups = next

states = sorted([i[0] for i in groups])
accept = [i for i in accept if i in states]

if start not in states:
    start = groups[find(start)][0]

print(','.join(states))
print(','.join(words))
print(','.join(accept))
print(start)

for i in states:
    for j in words:
        if flow[i][j] not in states:
            flow[i][j] = groups[find(flow[i][j])][0]

        print(i + "," + j + "->" + flow[i][j])
