from openai import OpenAI

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个数学助手。先写出推理过程，再给出答案。"},
        {"role": "user", "content": "小明有8个糖果，给了小红3个，又买了5个，然后吃了2个，还剩几个？请一步步思考。"}
    ]
)

print(response.choices[0].message.content)