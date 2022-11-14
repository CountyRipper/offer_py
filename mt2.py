import sys

n1 = sys.stdin.readline()
n, m = n1.split(" ")
n = int(n)
m = int(m)
matrix=[]

for i in range(n):
    n1 = sys.stdin.readline()
    row =[]
    for j in n1.strip():
        row.append(int(j))
    matrix.append(row)


def DFS(x,y,k,maze):
    row = len(maze)
    col = len(maze[0])
    if k==0:
        res.append((x,y))
        return 
    else:
        f =False
        for x1,y1 in [(x+1,y),(x,y+1),(x,y-1),(x-1,y)]:
            if maze[x1,y1] !=maze[x,y] and x<row and x>=0 and y<col and y>=0:
                f = True
                maze[x1,y1] = 1 if maze[x1,y1]==0 else 0
                DFS(x1,y1,k-1,maze)
                maze[x1,y1] = 1 if maze[x1,y1]==0 else 0
        if f==False:
            res.append((x,y)) 
n = input()
n = int(n)   
for i in range(n):
    n1 = sys.stdin.readline()
    x , y ,k=n1.split(" ")
    x = int(x)
    y = int(y)
    k = int(k)
    res=[]
    maze= matrix.copy()
    r = DFS(x,y,k,maze)
    print(r[0])
    
    
    
