import os
import sys
import argparse
from pathlib import Path
from openai import OpenAI

# 加载生命周期提示词
LIFECYCLE_PROMPT_PATH = Path(__file__).parent / "arkts_lifecycle_prompt.txt"
with open(LIFECYCLE_PROMPT_PATH, "r", encoding="utf-8") as f:
    LIFECYCLE_PROMPT = f.read()

# 将 API Key 存储在环境变量 ARK_API_KEY 中
client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.environ.get("ARK_API_KEY"),
)

def parse_arkts_lifecycle(source_text, model="deepseek-v3-1-terminus"):
    """解析 ArkTS 代码或文档中的生命周期函数信息
    
    Args:
        source_text (str): ArkTS 源代码或文档文本
        model (str): 使用的模型 ID
        
    Returns:
        OpenAI.ChatCompletion: 生命周期分析结果，需要从 response.choices[0].message.content 获取 JSON
    """
    return client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": LIFECYCLE_PROMPT},
            {"role": "user", "content": source_text}
        ],
        temperature=0,  # 保持输出稳定
        # reasoning_effort="none"  # 不显示推理过程
    )

def read_input():
    """从标准输入读取多行文本，直到遇到空行"""
    print("请输入 ArkTS 代码，每行代码后按回车。")
    print("输入完成后请输入 END 并按回车结束输入。")
    print("开始输入代码：")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        except KeyboardInterrupt:  # 处理 Ctrl+C
            print("\n输入已取消")
            return ""
        except EOFError:  # 处理 Ctrl+D
            break
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="解析 ArkTS 生命周期函数")
    parser.add_argument("--model", default="deepseek-v3-1-terminus", help="使用的模型 ID")
    parser.add_argument("--file", help="可选：从文件读取 ArkTS 代码")
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            source_text = f.read()
    else:
        source_text = read_input()
    
    if not source_text:
        print("错误：没有输入任何代码")
        return 1
        
    print("\n正在分析代码...\n")
    response = parse_arkts_lifecycle(source_text, args.model)
    print(response.choices[0].message.content)
    return 0

if __name__ == "__main__":
    sys.exit(main())