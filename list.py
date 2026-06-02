#列表

a = []

for i in range(1,6):
    b = int(input(f"请输入第{i}个分数："))
    a.append(b)

print(f"\n所有分数：{a}")
print(f"最高分：{max(a)}")
print(f"最低分: {min(a)}")
print(f"平均分： {sum(a) / len(a)}")


