
# 第一个 API 调用程序
import os
from openai import OpenAI
API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"   # ← 改成你复制的 Key，保留引号

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
)

print(response.choices[0].message.content)