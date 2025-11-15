i = [1,5,2,6,8,4,1,7,3]
n = 8

def pass_center(input, nails):
    center = nails / 2
    counter = 0
    for index, i in enumerate(input[:-1]):
        if abs(i - input[index+1]) == center:
            counter += 1
    return counter

i = [1,32,12,28,16,32,16,32,16,30,14,30,17,1,17,2,21,4,20,1,17,32,16,32,19,32,18,1,15,28,12,28,9,25,9,25,9,26,10,26,10,27,11,29,13,29,10,26,10,30,14,30,17,1,17,1,14,27,9,25,9,27,11,25,9,25,9,25,9,25,9,25,7,27,11,27,11,27,11,26,9,25,9,25,5,21,2,20,4,20,4,20,7,23,4,23,7,26,10,25]
n = 32
print(pass_center(i, n))

def find_knots(input, nails):
    center = nails / 2
    passings = {}
    knots = {}
    centers = 0
    for index, i in enumerate(input[:-1]):
        pair = [i, input[index+1]]
        if i > input[index+1]:
            pair = [input[index+1], i]
        if pair[1] - pair[0] == 1:
            continue
