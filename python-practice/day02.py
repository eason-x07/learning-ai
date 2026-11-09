names = ["A", "B", "C", "D"]
def greet(name):
        print(f"Hi {name}!")
for name in names:
    greet(name)

student = {
    "name": "Eason",
    "year": 1,
    "major": "CS",
    "hobby": "sleep"
}

for key, value in student.items():
    print(f"{key} : {value}")

scores = [85, 92, 78, 90, 66]
total=0
for score in scores: 
    total += score
average = total / len(scores)
print(f"Total score: {total}")
print(f"Average: {average}")
