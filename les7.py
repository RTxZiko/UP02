# Вложенные циклы, линейные алгоритмы
# 1
"""
for x in range(15):
    num1 = 1 * 15**4 + 2 * 15**3 + 3 * 15**2 + x * 15 + 5
    num2 = 1 * 15**4 + x * 15**3 + 2 * 15**2 + 3 * 15 + 3
    otvet = num1 + num2

    if otvet % 14 == 0:
        a = otvet // 14
        result = ""
        while a > 0:
            result = "0123456789ABCDE"[a % 15] + result
            a //= 15
        print(result)
        break
"""
# 3
"""
def operanda():
    for x in range(10):
        num1 = f"{x}B09"
        num2 = f"{x}8E8"

        otvet = int(num1, 17) + int(num2, 15)

        if otvet % 155 == 0:
            return x, otvet // 155
x, a = operanda()
print(x)
print(a)
"""
# 4
"""
for y in range(1, 8):
    for x in range(8):
        num1 = y * 14641 + 0 + 4 * 121 + x * 11 + 5
        num2 = 2 * 4096 + 5 * 512 + 3 * 64 + x * 8 + y

        otvet = num1 + num2

        if otvet % 117 == 0:
            print(x, y, otvet // 117)
            break
    else:
        continue
    break
"""