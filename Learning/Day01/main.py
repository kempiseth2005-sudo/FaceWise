# Lesson 1 — Variables
# A variable stores information.
name = "FaceFit"
age = 22
height = 1.68

print(name)
print(age)
print(height)

# --------------------------------------------------------
# Lesson 2 — Lists
# A list stores multiple values.

landmarks = [10, 20, 30, 40, 50, 60]
facePoints = [
    (100, 200),
    (300, 400),
    (500, 600)
]
print(landmarks[1])
print(landmarks[3])


print(facePoints[0])
print(facePoints[1])
print(facePoints[2])

# --------------------------------------------------------
# Lesson 3 — Dictionaries
# A dictionary stores information using key → value.

faceInfo = {
    "Weight": 79,
    "Height": 1.68,
    "Age": 22,
    "Gender": "Male"
}
print("Weight:", faceInfo["Weight"])
print("Height:", faceInfo["Height"])
print("Age:", faceInfo["Age"])
print("Gender:", faceInfo["Gender"])

# --------------------------------------------------------
# Lesson 4 — if / else
# Python can make decisions.

face_width = 80
face_height = 100

if (face_width > face_height):
    print("Face is wide")
else:
    print("Face is long")


# --------------------------------------------------------
# Lesson 5 — Functions
# A function is a reusable piece of code.

def say_hello ():
    print("Hello, World!")
    
say_hello();

# Functions can receive data:

def calculateRadio (width, height): 
    radio = width / height
    return radio;
    

radio = calculateRadio (100, 50)
print(radio)

# --------------------------------------------------------
# Lesson 6 — import
# Python allows you to use libraries.

import math

result = math.sqrt(16)
print(result)