from openai import OpenAI

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

user_input = input("请输入一段包含姓名和年龄的文字：")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个信息提取助手。只输出JSON，不要输出其他内容。"},
        # ↓↓↓ 下面是 Few-shot 例子 ↓↓↓
        {"role": "user", "content": "从'我叫李四，今年20岁'里提取，输出{'name': '', 'age': 0}"},
        {"role": "assistant", "content": "{'name': '李四', 'age': 20}"},
        {"role": "user", "content": "从'我叫王五，今年25岁'里提取，输出{'name': '', 'age': 0}"},
        {"role": "assistant", "content": "{'name': '王五', 'age': 25}"},
        # ↑↑↑ 例子结束 ↑↑↑
        {"role": "user", "content": f"从'{user_input}'里提取"}
    ]
)

print(response.choices[0].message.content)