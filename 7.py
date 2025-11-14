names = []
rules = {}

with open("7/c.txt", "r") as file:
    names = file.readline().strip().split(',')
    for line in file:
        if line.strip():
            rule = line.split('>')
            rules[rule[0].strip()] = rule[1].strip().split(',')

def follow_rules(names, rules):
    follows = {}
    for i, n in enumerate(names):
        chars = list(n)
        ok = True
        for j, c in enumerate(chars[:-1]):
            if chars[j+1] in rules[c]:
                continue
            else:
                ok = False
                break
        if ok:
            follows[i+1] = n
    return follows

def task_c(names, rules):
    valids = set()
    visited = set()
    for n in names:
        check_valid(n[-1], n, valids, visited)
    return valids

def check_valid(char, name, valids, visited):
    if len(name) == 11:
        return

    if (char, name) in visited:
        return
    visited.add((char, name))

    if char in rules:
        for n in rules[char]:
            new = name + n
            if len(new) >= 7:
                valids.add(new)
            check_valid(n, new, valids, visited)


valid = follow_rules(names, rules)
print(valid)

sum = 0
for v in valid:
    sum += int(v)
print(sum)

valids = task_c(valid.values(), rules)
#for v in valids:
    #print(v)
print(len(valids))
