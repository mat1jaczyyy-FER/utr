#!/usr/bin/env python3
# Dominik Matijaca 0036524568

inputs = [i.split(",") for i in input().split("|")]
states = input().split(",")
words = input().split(",") + ["$"]
st_words = input().split(",")
accept = input().split(",")
start = input()
st_start = input()

table = {}
for i in states:
    for j in words:
        for k in st_words:
            table[f"{i},{j},{k}"] = ["$"]

while True:
    try:
        a, b = input().split("->")
        table[a] = b.split(",")

    except EOFError:
        break

for t in inputs:
    state = start
    stack = [st_start]
    out = [f"{state}#{''.join(reversed(stack))}"]
    done = False
    loop_detect = 0

    i = 0
    while True:
        if i >= len(t) and state in accept:
            out.append("1" if state in accept else "0")
            break

        increment = True
        action = table[f"{state},{t[i] if i < len(t) else '$'},{stack[-1]}"]

        if i < len(t) and action[0] == "$":
            action = table[f"{state},$,{stack[-1]}"]
            increment = False

            if action[0] == "$":
                out.append("fail")
                out.append("0")
                break

        if action[0] != "$":
            state = action[0]
            stack.pop()
        
            if action[1] != "$":
                stack += reversed(list(action[1]))
            
            out.append(f"{state}#{'$' if not len(stack) else ''.join(reversed(stack))}")

            if increment and i < len(t):
                loop_detect = i
            
            elif out[-1] in out[loop_detect:-1]:
                out.append("0")
                break

        elif i >= len(t):
            out.append("0")
            break

        if not len(stack):
            if i < len(t):
                out.append("fail")
                out.append("0")

            else:
                out.append("1" if state in accept else "0")

            break

        if increment:
            i += 1

    print("|".join(out))