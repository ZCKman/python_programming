import unittest

class MyMatrix:
    matrix = [[int]]
    listNum = 0
    listSize = 0
    def spiralOrder(self, matrix: [[int]]) -> [[int]]:
        finalList = []

        while(True):
            if(len(matrix) != 0):
                # Local Variable Assignment
                i = 0 # Horizontal Index
                j = 0 # Vertical Index
                listSize = len(matrix[0]) - 1
                listNum = len(matrix) - 1
                # First row
                while(i <= listSize):
                    finalList.append(matrix[0][i])
                    i += 1
                i -= 1
                matrix.remove(matrix[0])
                listNum -= 1
                # Last column
                while(j < listNum):
                    finalList.append(matrix[j][listSize])
                    matrix[j].remove(matrix[j][listSize])
                    j += 1
                #i -= 1
                listSize -= 1
                # Bottom row
                print(matrix, i, listSize, listNum)
                while(i >= 0):
                    print("HIT", matrix, finalList, listNum)
                    finalList.append(matrix[listNum][i])
                    matrix[listNum].remove(matrix[listNum][i])
                    i -= 1
                print("HIT2", matrix)
                #matrix.remove(matrix[listNum])
                '''if(len(matrix) != 0):
                    listNum = len(matrix) - 1
                    listSize = len(matrix[listNum]) - 1
                    j = listSize
                    while(j >= 0):
                        finalList.append(matrix[listNum][j])
                        matrix[listNum].remove(matrix[listNum][j])
                        j -= 1
                    matrix.remove(matrix[listNum]) '''
                # First column
                j = 0
                i = listNum - 1
                listNum -= 1
                if(len(matrix) != 0):
                    while(i >= 0 and matrix):
                        finalList.append(matrix[i][0])
                        matrix[i].remove(matrix[i][0])
                        i -= 1
            else:
                print("----------ELSE-----------\n",finalList,"\n|||||||||||||||||||||")
                return finalList

# Testing
obj = MyMatrix()
class TestReverseWords(unittest.TestCase):

    def test_MyString(self):
        self.assertEqual(obj.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(obj.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]), [1,2,3,4,8,12,11,10,9,5,6,7])
        self.assertEqual(obj.spiralOrder([
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]
]), [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12])
        self.assertEqual(obj.spiralOrder([
[1, 2, 3],
[10, 11, 4],
[9, 12, 5],
[8, 7, 6]
]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

if __name__ == '__main__':
    unittest.main()
