from openai import OpenAI
import glob

API_KEY = "sk-f3e5fcd2e9ec462b9d31f1c3cd62c585"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com/v1"
)

# 1. 读取当前文件夹下所有 .txt 文件
all_text = ""
for file_path in glob.glob("*.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        all_text += f"\n\n【文件 {file_path} 的内容】\n"
        all_text += f.read()

print(f"已读取 {len(glob.glob('*.txt'))} 个文件")

# 2. 让 AI 基于这些文件内容回答
def ask_from_files(question):
    prompt = f"""
你是一个基于文档的问答助手。请根据下面【所有文档内容】回答问题。

【所有文档内容】
{all_text}

【问题】
{question}

规则：
1. 只根据文档内容回答
2. 如果文档中没有相关信息，回答"文档中找不到答案"
3. 回答要简洁
"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 3. 测试
while True:
    q = input("\n问问题（q 退出）：")
    if q == "q": break
    print("答：", ask_from_files(q))