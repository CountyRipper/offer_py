#棋盘最长路径
#设定空盘为0，黑子为-1，白字为1
path = []
max_len = 0
def max_road(matrix)->int:
    row = len(matrix)
    col = len(matrix[0])
    def DFS(x,y):
        global max_len
        #没有越界
        if x<row and x>=0 and y<col and y>=0:
            if matrix[x][y]==1:
                if len(path)> max_len:
                    max_len = len(path)
                for next_x,next_y in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
                    #如果已经在path内，跳过
                    if (next_x,next_y) not in path:
                        path.append((next_x,next_y))
                        DFS(next_x,next_y)
                        path.pop()
            else:
                #如果是黑子或者空盘
                return
        #越界
        else:
            return
    for i in range(row):
        for j in range(col):
            path.append((i,j))
            DFS(i,j)
            path.pop()
    return max_len

matrix=[[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0,-1,-1, 1, 0, 0, 0],
        [0, 0,-1, 1, 1,-1, 0, 1],
        [0, 0,-1, 1, 0, 1, 0, 0],
        [0,-1, 1, 1, 0, 0, 0, 0],
        [0, 0,-1,-1,-1,-1, 1, 0],
        [0,-1, 1, 1, 1,-1, 1, 0],
        [0, 1, 0, 0, 1, 1, 1,-1],
        [0, 0, 0,-1, 1,-1,-1,-1],    
]
print(max_road(matrix))

    
        