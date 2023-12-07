"""
Author: Batool Alkaddah 
Time & Date: 10:15 a.m. 2023-12-02
PyCharm
"""

import numpy as np

# Original list
List1 = np.array([15, 7.5, 22.5, 12])

# Create a new list (List2) by shifting the values of List1
shift_value = 5
List2 = List1 + shift_value

# Display the original and shifted lists
print("Original List (List1):", List1)
print("Mean of List1:", np.mean(List1))
print("Standard Deviation of List1:", np.std(List1))

print("\nShifted List (List2):", List2)
print("Mean of List2:", np.mean(List2))
print("Standard Deviation of List2:", np.std(List2))