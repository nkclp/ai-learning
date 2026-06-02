from openai import OpenAI

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

# 让用户输入文字
user_input = input("请输入一段包含姓名、电话、地址的文字：")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个信息提取助手。只输出JSON，不要输出其他内容。格式：{'name': '', 'phone': '', 'address': ''}"},
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)