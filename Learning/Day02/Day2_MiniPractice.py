import numpy as np
faceWidth = np.array([200, 300])
faceHeight = np.array([200, 300])

def calculateRatio(width, height):
    ratio = width / height
    return ratio

print("Face Width:", faceWidth[0])
print("Face Height:", faceHeight[0])
print("Face Ratio:", calculateRatio(faceWidth[0], faceHeight[0]))

print("-------------------------------------------------------")

print("Practice 2: Eye Detection")
leftEye = [100, 150]
rightEye = [220, 150]

def calculateDistance(eye1, eye2):
    distance = np.sqrt((eye1[0] - eye2[0])**2 + (eye1[1] - eye2[1])**2)
    return distance

print("Distance:", calculateDistance(leftEye, rightEye))
