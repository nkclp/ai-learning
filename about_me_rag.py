from openai import OpenAI

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com/v1"
)

# 1. 读取 关于我.txt 文件
with open("关于我.txt", "r", encoding="utf-8") as f:
    file_content = f.read()

print(f"✅ 文件已读取，共 {len(file_content)} 个字符")

# 2. 问答函数（直接把整个文件给 AI）
def ask_question(question):
    full_prompt = f"""
你是我的个人助理。请根据下面的【文档内容】回答问题。

【文档内容】
{file_content}

【问题】
{question}

规则：
1. 如果文档中有答案，用原文回答
2. 如果文档中没有答案，回答"文档中没有相关信息"
3. 回答要简洁准确
"""
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": full_prompt}
        ]
    )
    
    return response.choices[0].message.content

# 3. 测试问答
while True:
    question = input("\n📝 请输入问题（输入 q 退出）：")
    if question == "q":
        break
    answer = ask_question(question)
    print(f"🤖 答案：{answer}")