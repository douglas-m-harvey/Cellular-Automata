import numpy as np

arr = np.arange(10)
print(arr, "\n")
for n in range(len(arr)):
    smallArr = np.roll(arr.copy(), -(n - 1))[0:3]
    print(smallArr)

# for i in range(len(arr[0])):
#     if i < 10 - 2:
#         print(arr.copy()[0][i:i + 3])
#     if i == 10 - 2:
#         print(np.append(arr.copy()[0][i:i + 3], arr[0][0]))
#     if i == 10 - 1:
#         print(np.append(arr.copy()[0][i:i + 3], arr[0][0:2]))