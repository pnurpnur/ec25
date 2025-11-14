

names = ['Ny', 'Nyrix', 'Shaem', 'Thar', 'Tharn', 'Sarn', 'Nar', 'Draith', 'Lorn', 'Jar', 'Glaur', 'Gaer', 'Rav', 'Jaer']
rules = {'Q': ['u'], 's': ['s', 'w', 'c', 'i', 'm', 'k', 'a', 'j', 't'], 'k': ['y'], 'e': ['r', 'm', 'v'], 'D': ['r'], 'o': ['r', 'v'], 'R': ['a'], 'r': ['t', 'i', 'w', 'c', 'm', 'k', 'a', 'j', 'n', 'v'], 'J': ['a'], 'l': ['y', 'o', 'w', 'c', 'i', 'm', 'k', 'a', 'j', 't', 'v'], 'x': ['a', 'w', 'c', 'i', 'm', 'k', 'j', 't'], 'd': ['o'], 'G': ['l', 'a'], 'L': ['o'], 'a': ['e', 'l', 'r', 'x', 'v', 'i', 'u'], 'N': ['y', 'a'], 'v': ['w', 'c', 'i', 'm', 'k', 'a', 'j', 't'], 'B': ['e'], 'n': ['d', 'a', 'w', 'c', 'i', 'm', 'k', 'j', 't'], 'y': ['n', 'v', 'r', 'x'], 'T': ['h'], 'm': ['i', 'w', 'c', 'm', 'k', 'a', 'j', 't'], 'j': ['o'], 'H': ['e'], 'h': ['y', 'a', 'w', 'c', 'i', 'm', 'k', 'j', 't', 'v'], 't': ['h'], 'S': ['h', 'a'], 'c': ['a'], 'i': ['s', 'n', 'r', 'l', 'x', 't'], 'w': ['y'], 'u': ['v', 'r']}

def task_c(names, rules):
    valids = []
    visited = []
    for n in names:
        check_valid(n[-1], n, valids, visited)
    return valids

def check_valid(char, name, valids, visited):
    if char in rules:
        for n in rules[char]:
            new = name + n
            if new in visited:
                break
            visited.append(new)
            if len(new) == 12:
                break
            if len(new) >= 7:
                valids.append(new)
            check_valid(n, new, valids, visited)



valids = task_c(names, rules)

print(len(valids))
