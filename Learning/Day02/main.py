# Step 1 — Exercise 1: Create an array
# Create Learning/Day02/main.py
import numpy as np 

point = np.array([10,20])

print("X:", point[0])
print("Y:", point[1])


# Step 2 — Exercise 2: Multiple facial points
# Create three points:

pointA = [100, 150]
pointB = [200, 250]
pointC = [300, 350]

print("Point A:", pointA[1])
print("Point B:", pointB[1])
print("Point C:", pointC[0])

# Step 3 — Exercise 3: Calculate face width

right_Facce = np.array([100, 200])
left_Face = np.array ([200, 300])

total_Face = np.linalg.norm(right_Facce - left_Face)
print("Total face width:", total_Face)