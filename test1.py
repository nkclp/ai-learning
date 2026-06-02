#温度转换器

temp = float(input("请输入温度"))
choice = int(input("请选择(1：转华氏度，2：转摄氏度):"))

if choice == 1:
    result = temp * 9 / 5 + 32
    print(f"{temp}摄氏度 = {result}华氏度")
elif choice == 2:
    result = (temp - 32) * 5 / 9
    print(f"{temp}华氏度 = {result}摄氏度")
else:
    print("选择无效，请输入 1 或 2")