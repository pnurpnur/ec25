def multiply(x, y):
    res = [x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0]]
    return res

def add(x, y):
    res = [x[0] + y[0], x[1] + y[1]]
    return res

def divide(x, y):
    res = [int(x[0] / y[0]), int( x[1] / y[1])]
    return res

def task1(r, a):
    for i in range(3):
        r = multiply(r, r)
        r = divide(r, [10, 10])
        r = add(r, a)
    return r

r = [0,0]
a = [25,9]

#a = [149,54]
#res = task1(r, a)
#print(res)

def task2 (a, size):
    counter = 0
    for i in range(size):
        y = a[1] + i*(1000/(size - 1))
        for j in range(size):
            x = a[0] + j*(1000/(size - 1))
            r = [0,0]
            #print([x,y])
            for k in range(100):
                r = multiply(r, r)
                r = divide(r, [100000,100000])
                r = add(r, [x, y])
                if (r[0] < -1000000 or r[0] > 1000000 or r[1] < -1000000 or r[1] > 1000000):
                    #print(".", end="")
                    break
            else:
                counter += 1
                #print("x", end="")
        #else:
            #print("")
    return counter

a = [35300,-64910]
#a = [-3314,68783]
#res = task2(a, 101)
a = [-3314,68783]
res = task2(a, 1001)
print(res)
