k = int(input("数字を入力してください=>"))
for i in range(1,k+1):
    if i%3 == 0:
        symbol = "◆ "
    elif i%2 == 0:
        symbol = "□ "
    else:
        symbol = "■ "
    print("  "*(k-i) + symbol*(2*i-1))