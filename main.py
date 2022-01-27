"""
Given two arrays of integer as input, create a new merged array. The elements of the second array appear after the first array in the new merged array. Print the new merged array.
Input-> [1,2,3],[4,5,6,7]
Output-> [1,2,3,4,5,6,7]
"""

list_1 = [1,2,3]
len_list_1 = len(list_1)
list_2 = [4,5,6,7]
len_list_2 = len(list_2)
new_list = []
for i in range(0,len_list_1):
  e = list_1[i]
  new_list.append(e)
for j in range(0,len_list_2):
  e1 = list_2[j]
  new_list.append(e1)
print(new_list)
