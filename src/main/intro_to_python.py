import numpy as np

#1
def printMatrix():  
  matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
  for i in range(3):
        for j in range(3):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
  
  print(*[str(row)[1:-1] for row in matrix], sep='\n')

#2
def printMatrix2():
  matrix2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
  for i in range(3):
        for j in range(3):
            if i == j:
                matrix2[i][j] = 1
            else:
                matrix2[i][j] = 3
  print(*[str(row)[1:-1] for row in matrix2], sep='\n')

#3
def printMatrix3():
  matrix3 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
  for i in range(3):
        for j in range(3):
            if i == j:
                matrix3[i][j] = 1
            else:
                matrix3[i][j] = 3
  matrix3 = np.delete(matrix3, 2, 1)
  print(*[str(row)[1:-1] for row in matrix3], sep='\n')
  
if __name__ == "__main__":
  printMatrix()
  print("\n")
  printMatrix2()
  print("\n")
  printMatrix3()