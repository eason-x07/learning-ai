def get_grade(score):
    if score >= 80:
        return 'A'
    elif 60 <= score < 80:
        return 'B'
    else:
        return 'C'
    
scores = {
    "Eason": 85,
    "Alice": 92,
    "Bob": 58,
    "Cindy": 73
}

for name, score in scores.items():
    grade = get_grade(score)
    print(f"{name}: {score} ({grade})")

failed_students = 0
for score in scores.values():
    if score < 60:
        failed_students += 1
print(f"不及格人数：{failed_students}")
