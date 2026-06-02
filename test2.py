#猜数字游戏

import random

secret = random.randint(1, 100)
count = 0

while count < 7:
    guess = int(input("猜一个数字(1-100): "))
    count = count + 1
    
    if guess == secret:
        print(f"恭喜！你一共猜了{count}次，答案是{secret}")
        break
    elif guess < secret:
        print("太小了")
    else:
        print("太大了")

# 循环正常结束（没猜中，次数用完了）
if count >= 7 and guess != secret:
    print(f"你失败了，答案是{secret}")