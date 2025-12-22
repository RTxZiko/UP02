import csv
# 1
"""
with open("txt/59778.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    count = 0

    for i in range(len(n) - 1):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)

    a = l
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i].count(a[i][j]) == 4:
                repeat = a[i][j]
                x = []
                for j in range(len(a[i])):
                    if a[i][j] not in x and a[i][j] != repeat:
                        x.append(a[i][j])
                sum_repeat = 4 * repeat
                average_sum = sum(x) / 3
                if average_sum > sum_repeat:
                    count += 1
    print(count)
"""
# 2
"""
with open("txt/29666.csv", "r") as f:
    n = csv.reader(f)
    l = []

    for el in n:
        num = el[0] + "." + el[1]
        l.append(float(num))

    max_sum = 0
    current = l[0]

    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            current += l[i + 1]
        else:
            current = l[i + 1]
        if current > max_sum:
            max_sum = current

    print(max_sum)
"""