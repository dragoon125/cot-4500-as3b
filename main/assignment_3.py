import numpy as np

#Question 1
a = np.array([[2, -1, 1], [1, 3, 1], [-1, 5, 4]])
b = np.array([6, 0, -3])
c = np.linalg.solve(a, b);
print(c)
print()

#Question 2

#Question 3
diagonal = np.array([[9, 0, 5, 2, 1], [3, 9, 1, 2, 1], [0, 1, 7, 2, 3], [4, 2, 3, 12, 2], [3, 2, 4, 0, 8]])
bool = True
for i in range(len(diagonal)):
   total = 0
   for j in diagonal[i]:
       if(j != diagonal[i, i]):
           total += abs(j)

   if(diagonal[i, i] < total):
       print("This matrix is NOT diagonally dominante.")
       bool = False
       break;

if(bool == True):
   print("This matrix is diagonally dominante.")
print()

#Question 4
definite = np.array([[2, 2, 1], [2, 3, 0], [1, 0, 2]])
check = True

temp1 = definite[0, 0] * np.linalg.det(definite[1:3, 1:3])
a = definite[1:3, 0:1]
b = definite[1:3, 2:3]
c = np.hstack((a, b))
temp2 = definite[0, 1] * np.linalg.det(c)
temp3 = definite[0, 2] * np.linalg.det(definite[1:3, 0:2])

if(abs(definite[0, 0]) < 0):
    check = True
    print("This is NOT a positive definite")
elif(((definite[0, 0] * definite[1, 1]) - (definite[0, 1] * definite[1, 0]) < 0)):
    check = False
    print("This is NOT a positive definite")
elif((temp1 - temp2 + temp3) < 0):
    check = False
    print("This is NOT a positive definite")
else:
    print("This is a positive definite")
