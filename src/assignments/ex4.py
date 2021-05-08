def func1(k):
    if k % 3 == 0:
        symbol = "◆ "
    elif k % 2 == 0:
        symbol = "□ "
    else:
        symbol = "■ "
    return symbol


def func2(k, x):
    list1 = x*(2*k-1)
    return list1


def func3(k, n, y):
    list2 = "  "*(n-k) + y
    return list2


n = int(input("数字を入力してください=>"))
for k in range(1, n+1):
    x = func1(k)
    y = func2(k, x)
    print(func3(k, n, y))
