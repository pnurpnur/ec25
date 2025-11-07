import math

l = """102
75
50
35
13"""

def last_turns(numbers, turns):
    # Hent første og siste tall
    first = numbers[0]
    last = numbers[-1]
    ratio = first / last

    return math.floor(ratio * turns)

def reach_turns(numbers, turns):
    # Hent første og siste tall
    first = numbers[0]
    last = numbers[-1]
    ratio = first / last

    return math.ceil(turns / ratio)

def last_turns_pair(numbers, turns):
    # Hent første og siste tall
    first = int(numbers[0])
    last = int(numbers[-1])

    mult = 1;
    prev = first;
    for l in numbers:
        if not '|' in l:
            continue
        parts = l.split('|')
        mult *= prev / int(parts[0])
        prev = int(parts[1])

    mult *= prev / last

    return int(mult * turns)

#with open("4/b.txt", "r") as file:
#    l = file.read()

# Del opp på linjeskift og konverter til heltall
#numbers = [int(x) for x in l.splitlines() if x.strip()]

#print(last_turns(numbers, 2025))

#print(reach_turns(numbers, 10000000000000))

#Nå er det stringer
l = """5
7|21
18|36
27|27
10|50
10|50
11"""

with open("4/c.txt", "r") as file:
    l = file.read()

input = [x for x in l.splitlines() if x.strip()]
print(last_turns_pair(input, 100))
