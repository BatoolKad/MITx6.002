"""
Author: Batool Alkaddah 
Time & Date: 2:06 p.m. 2023-12-01
PyCharm
"""
import math
import numpy as np

def  stdDevOfLengths(L):
    """
    :param L: a list of strings
    :return: the standard deviation of the lengths of the strings
    """
    if not L:
      return float('NaN')

    L_num= [len(t) for t in L]
    if sum(L_num) == len(L_num):
        return 0.0

    mean= sum(L_num)/len(L_num)

    variance= sum([(n-mean)**2 for n in L_num])
    std= math.sqrt((variance/len(L_num)))

    return std


# L = ['apples', 'oranges', 'kiwis', 'pineapples']
L1 = [15,7.5,22.5,12]
# std1= np.std(L1)
# L2 = L1 * (std1 / np.std(L1))
#
#
# mean1= np.mean(L1)
# mean2= np.mean(L2)
#
# std1= np.std(L1)
# std2= np.std(L2)
#
# cv1 = np.std(L1)/np.mean(L1)
# cv2 = np.std(L2)/np.mean(L2)
#
# print(round(std1,3), round(std2,3))
#
# print(round(mean1,3), round(mean2,3))
#
# print(round(cv1,3), round(cv2,3))


# Given list
L1 = np.array([15, 7.5, 22.5, 12])

# Set a seed for reproducibility
np.random.seed(30)

# Generate a new list with the same standard deviation as L1
desired_std = np.std(L1)
new_list = np.random.normal(loc=0, scale=desired_std, size=len(L1))

# Print the standard deviations of both lists
print("Original List (L1):", L1)
print("Standard Deviation of L1:", np.std(L1))
print("\nNew List:", new_list)
print("Standard Deviation of New List:", np.std(new_list))


