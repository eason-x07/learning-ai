student = {
    "name": "Eason",
    "year": 1,
    "major": "CS",
    "hobby": "sleep"
}

print(student["name"])
print(student["year"])
print(student["hobby"])

student["food"] = "nasi lemak"
print(student)


def greet(name):
    print(f"Hello, {name}!")

greet("Eason")

greet(student["name"])

greet("Happy")

food = input("你最喜欢吃什么？")
student["food"] = food
print(student)

student["year"] = 2
print(student)
