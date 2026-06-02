from openai import OpenAI

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"  # 换成你自己的

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

# 让用户输入问题
user_input = input("请输入你的问题：")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
    {"role": "system", "content": "你是一个专业、耐心的电商客服，回答要简洁、礼貌，不超过3句话。"},
    {"role": "user", "content": user_input}
]
)

print("\nAI回答：")
print(response.choices[0].message.content)