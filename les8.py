#1
"""
def f(n):
    if n[0] > n[1]:
        return f(n[1:])
    if n[1] >= n[2] >= n[3]:
        del n[1]
        return f(n)
    return n


arr = [6, 2, 5, 4, 2, 5, 6]
print(f(arr))
"""
#3
"""
def perevorot(n):
    return int(str(n)[::-1])
count = 0
for x in range(1, 1050):
    if x + perevorot(x) == 1050:
        count += 1
print("3:", count)
"""