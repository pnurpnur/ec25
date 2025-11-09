
def place_number(p, rows):
    for j in range(len(rows)):
        if rows[j][0] == 0 and p < rows[j][1]:
            rows[j][0] = p
            return rows
        if rows[j][2] == 0 and p > rows[j][1]:
            rows[j][2] = p
            return rows
    rows.append([0, p, 0])
    return rows

def get_rows(parts):
    rows = [[0, int(parts[0]), 0]]

    for p in parts[1:]:
        rows = place_number(int(p), rows)

    return rows

def get_quality(i):
    split = i.split(':')
    parts = split[1].split(',')
    rows = get_rows(parts)
    answer = '';
    for index in range(len(rows)):
        answer += str(rows[index][1])
    return answer

def task_b(i):
    lines = [x for x in i.splitlines() if x.strip()]
    swords = []
    for l in lines:
        swords.append(int(get_quality(l)))
    return max(swords) - min(swords)

def swords_with_info(i):
    lines = [x for x in i.splitlines() if x.strip()]
    swords = []
    for l in lines:
        split = l.split(':')
        id = split[0]
        parts = split[1].split(',')
        rows = get_rows(parts)
        q = '';
        ns = [];
        for index in range(len(rows)):
            q += str(rows[index][1])
            n = '';
            if (rows[index][0] > 0):
                n += str(rows[index][0])
            n += str(rows[index][1])
            if (rows[index][2] > 0):
                n += str(rows[index][2])
            ns.append(int(n))
        swords.append((q, ns, id))
    return swords

def sort_swords(i):
    swords = swords_with_info(i)
    sorted_swords = sorted(swords, key=lambda sword: (-int(sword[0]), [-x for x in sword[1]], -int(sword[2])))
    return sorted_swords

def task_c(i):
    swords = sort_swords(i)
    sum = 0
    for index in range(len(swords)):
        sum += (index+1)*int(swords[index][2]);
    return sum

#i = "58:5,3,7,8,9,10,4,5,7,8,8"
#i = "90:7,9,3,3,9,5,1,8,4,6,8,4,3,6,7,3,5,3,6,1,2,3,9,5,6,1,4,4,2,7"
#print(get_quality(i))

with open("5/c.txt", "r") as file:
    i = file.read()

#print(task_b(i))
print(task_c(i))
