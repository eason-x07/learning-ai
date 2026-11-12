import json

def get_grade(score):
    if score >= 80:
        return 'A'
    elif 60 <= score < 80:
        return 'B'
    else:
        return 'C'

try:
    with open("grade_data.json", "r", encoding="utf-8") as f:
        scores = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    scores = {}
    
while True:
    name = input("学生名字（直接回车结束）：")
    if name == "":
        break
    try:
        score = int(input("分数："))
    except ValueError:
        print("请输入数字！")
        continue
    scores[name] = score

with open("grade_data.json", "w", encoding="utf-8") as f:
    json.dump(scores, f, ensure_ascii=False, indent=4)

if len(scores) == 0:
    print("无任何学生成绩记录。")
else:
    total = 0
    failed_students = 0
    print("=====成绩单=====")
    for name, score in scores.items():
        grade = get_grade(score)
        print(f"{name}: {score} ({grade})")
        total += score
        if score < 60:
            failed_students += 1
    print("------------------")
    average = total / len(scores)
    print(f"平均分：{average:.1f}")
    print(f"不及格人数：{failed_students}")
