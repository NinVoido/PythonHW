_chars = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def add(a: str, b: str) -> int:
    a = a[::-1]
    b = b[::-1]
    ans = 0

    for i in range(min(len(a), len(b))):
        ans += (_chars[a[i]] + _chars[b[i]]) * 10**i

    if min(len(a), len(b)) == len(a):
        for i in range(len(a), len(b)):
            ans += _chars[b[i]] * 10**i
    else:
        for i in range(len(b), len(a)):
            ans += _chars[a[i]] * 10**i

    return ans

a = input('Здравствуйте! Я складываю два числа. Введите числа, сумму которых хотите найти.\n')
b = input()

print(str(add(a, b)) + ' Это сумма Ваших чисел.')
