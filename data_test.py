import pandas as pd
import numpy as np
from math import sqrt
from collections import Counter

# Load dataset
data = pd.read_csv("data.csv")

# New point to classify
new_point = np.array([20, 35])

# Compute Euclidean distance
def distance(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Choose K
K = 5   # change this to 3,5,7 and observe

distances = []

for i in range(len(data)):
    point = np.array([data.iloc[i,0], data.iloc[i,1]])
    d = distance(new_point, point)
    distances.append((d, data.iloc[i,2]))

# Sort by distance
distances.sort(key=lambda x: x[0])

print("\nAll distances:")
for d in distances:
    print(d)

# Take K nearest neighbors
neighbors = distances[:K]

print(f"\n{K} Nearest neighbors:")
for n in neighbors:
    print(n)

# Majority voting
classes = [n[1] for n in neighbors]
result = Counter(classes).most_common(1)[0][0]

print("\nPredicted Class =", result)
