import numpy as np


# Step 1: Vectorized Distance Function
# Using NumPy, calculate Euclidean distances between multiple landmark pairs without using explicit Python for loops:
def calculateDistance(point1_array, point2_array):
    """
    Calculate Euclidean distance between paired 3D points.
    point1_array, point2_array: numpy arrays of shape (N,3) or (3,)
    """
    return np.linalg.norm(point1_array - point2_array, axis=-1)

# Step 2: Practice Script — Computing Facial Ratios
# This script creates simulated 3D landmarks for key facial points (forehead left/right, cheekbones left/right, jaw left/right, top of forehead, bottom of chin) and computes their ratios:

# 1. Simulated MediaPipe 3D Landmark Coordinates (X, Y, Z)
landmarks = {
    "forehead_left": np.array([0.2, 0.3, 0.1]),
    "forehead_right": np.array([0.8, 0.3, 0.1]),
    "cheekbone_left": np.array([0.3, 0.6, 0.2]),
    "cheekbone_right": np.array([0.7, 0.6, 0.2]),
    "jaw_left": np.array([0.4, 0.9, 0.3]),
    "jaw_right": np.array([0.6, 0.9, 0.3]),
    "top_of_forehead": np.array([0.5, 0.1, 0.05]),
    "bottom_of_chin": np.array([0.5, 1.0, 0.4])
}
#2 Compute Distances using np.linalg.norm
forehead_width = np.linalg.norm(landmarks["forehead_left"] - landmarks["forehead_right"])
cheekbone_width = np.linalg.norm(landmarks["cheekbone_left"] - landmarks["cheekbone_right"])
jaw_width = np.linalg.norm(landmarks["jaw_left"] - landmarks["jaw_right"])
forehead_to_chin = np.linalg.norm(landmarks["top_of_forehead"] - landmarks["bottom_of_chin"])

#3 Calculate Ratios

ratios = {
    "height_to_width" :  forehead_to_chin / cheekbone_width,
    "jaw_to_forehead" : jaw_width / forehead_width,
    "jaw_to_cheekbone" : jaw_width / cheekbone_width
}

print("=== Facial Measurements ===")
print(f"Forehead Width: {forehead_width:.4f}")
print(f"Cheekbone Width: {cheekbone_width:.4f}")
print(f"Jaw Width: {jaw_width:.4f}")
print(f"Forehead to Chin: {forehead_to_chin:.4f}")

print("--- Facial Ratios ---")


# Array of 3 start points and 3 end points (Shape: 3, 3)
start_points = np.array([
    landmarks["forehead_left"],
    landmarks["cheekbone_left"],
    landmarks["jaw_left"]
])
end_points = np.array([
    landmarks["forehead_right"],
    landmarks["cheekbone_right"],
    landmarks["jaw_right"]
])

# Single vectorized distance call for all pairs simultaneously
widths = np.linalg.norm(start_points - end_points, axis=1)
print("Widths:", widths)