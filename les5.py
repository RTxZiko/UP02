# 1
"""
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(5))
"""
# 2
"""
def remove_vowels(string):
    glasnie = ["a","e ", "i"," o","u"]
    vivod = ''

    for bukva in string:
        if bukva not in glasnie:
            vivod += bukva
    if vivod == string:
        return vivod
    elif vivod == '':
        return vivod
    else:
        return remove_vowels(vivod)
print(remove_vowels("nurgun"))
"""
"""
# 3
def pascal(n):
    if n == 0:
        return [1]

    pred_row = pascal(n - 1)
    current_row = [1]

    for i in range(1, len(pred_row)):
        current_row.append(pred_row[i - 1] + pred_row[i])

    current_row.append(1)
    return current_row


print(pascal(5))
"""