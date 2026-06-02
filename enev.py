#1到100的偶数和
total = 0
for i in range(2,101, 2): # 从2开始，每次+2
    total = total + i

print(f"1到100的偶数和是:{total}")
