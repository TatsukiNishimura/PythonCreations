k = int(input("数字を入力してください=>"))
for i in range(1,k+1):
    print("  "*(k-i) + "■ "*(2*i-1))