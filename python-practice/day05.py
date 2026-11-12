# import json    # 先导入 json 工具包，Python 自带，不用安装

# scores = {"Eason": 85, "Alice": 92, "小明": 70}

# # 存：字典 → 文件
# with open("scores.json", "w", encoding="utf-8") as f:
#     json.dump(scores, f, ensure_ascii=False, indent=2)

# # 读：文件 → 字典
# with open("scores.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)

# print(loaded["Eason"])    # 输出 85，真的变回字典了！

import json

try:
    with open("scores.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
except FileNotFoundError: 
    scores = {}

while True:
    name = input("Enter student's name: ")
    if name == "": 
        break
    score = int(input("Enter student's score: "))
    scores[name] = score

with open("scores.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False, indent=2)

print(f"Total students now: {len(scores)}")
