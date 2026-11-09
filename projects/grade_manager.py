def get_grade(score):
    if score >= 80:
        return 'A'
    elif 60 <= score < 80:
        return 'B'
    else:
        return 'C'
    
scores = {}
while True:
    name = input("学生名字（直接回车结束）：")
    if name == "":
        break
    score = int(input("分数："))
    scores[name] = score

if len(scores) == 0:
    print("未输入任何学生成绩。")
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
