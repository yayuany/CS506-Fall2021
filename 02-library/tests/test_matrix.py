import pytest
import random
from cs506 import matrix

m1 = [[5,6],[7,8]]
m2 = []
m3 = [[1,2]]
m4 = [[1,1,1],[2,2,2],[3,3,3]]

print(matrix.get_determinant(m1))
if matrix.get_determinant(m1) != -13:
    print("Not Correct!")

print(matrix.get_determinant(m2))
if matrix.get_determinant(m2) != 0:
    print("Not Correct!")

print(matrix.get_determinant(m3))
if matrix.get_determinant(m1) != 1:
    print("Not Correct!")

print(matrix.get_determinant(m4))
if matrix.get_determinant(m4) != 0:
    print("Not Correct!")


