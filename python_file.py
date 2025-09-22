import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1)
print(arr2)

marks=np.array([10,20,30,40])
print("Max marks : ",marks.max())
print("Min marks : ",marks.min())
print("Average marks : ",marks.mean())
print("First three elements :",marks[:3])
print("Standard deviation : ",np.std(marks))