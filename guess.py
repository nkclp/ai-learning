#程序随机一个 1-100 的数字，用户一直猜，猜对为止。
import random

secret = random.randint(1,100)
guess =0

while guess != secret:
    guess = int(input("猜一个数字(1-100):"))
    if guess < secret:
        print("太小了")
    elif guess > secret:
        print("太大了")

print(f"恭喜！答案是{secret}")
