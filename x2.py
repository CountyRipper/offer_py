#矩阵转置
from typing import List

def trans_matrix(matrix)-> List[List[int]]:
    row = len(matrix)
    col = len(matrix[0])
    res = []
    for i in range(col):
        res_row=[]
        for j in range(row):
            res_row.append(matrix[j][i])
        res.append(res_row)
    return res
matrix = [[1,2],[3,4],[5,6]]
print(trans_matrix(matrix))