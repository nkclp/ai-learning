# 让用户依次输入5个分数（用循环）
# 把每个分数存到一个列表里计算并输出：平均分、最高分、最低分、及格人数（>=60）
# 输出每个分数对应的等级（优秀/良好/及格/不及格）



scores = []
for i in range(1,6):
    b = int(input(f"请输入第{i}个分数:"))
    scores.append(b)

print(f"平均分:{sum(scores) / len(scores)}")
print(f"最高分:{max(scores)}")
print(f"最低分:{min(scores)}")

people = 0
for c in scores:
    if c >= 60:
        people = people + 1
print(f"及格人数为：{people}人")

for c in scores:
    if c >= 90:
        level = "优秀"
    elif c >= 80:
        level = "良好"
    elif c >= 60:
        level = "及格"
    else:
        level = "不及格"
    print(f"{c}分——{level}")
    