def func():
    m = int(input())#节点数
    n = int(input())#源节点
    k = int(input())#连接数
    links = []
    #dis = [float('inf') for _ in range(m)]
    #path = [-1 for _ in range(m)]
    visit = [0 for _ in range(m)]
    matrix = [[float('inf') for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i==j:
                matrix[i][j] = 0
    for i in range(k):
        cur = input().split()
        start = int(cur[0])-1
        target = int(cur[1])-1
        time = int(cur[2])
        links.append([start,target,time])
        #用矩阵存储，只能取最短
        if time<matrix[start][target]:
            matrix[start][target]=time        
    dis = matrix[n-1].copy()
    visit[n-1] = 1
    for i in range(1,m):
        cur_min = n-1
        min = float('inf')
        #如果没有被遍历过，并且存在路径，并且找出最近的那个点
        for j in range(m):    
            if(visit[j]!=1 and dis[j]<min):
                min = dis[j]
                cur_min = j
        #挑出最近的那个，记为遍历过
        
        visit[cur_min] = 1
        #更新在当前选出来的这个最近点之后更新的各路径最短长度
        #更新path数组
        for k in range(m):
            if visit[k]!=1 and matrix[cur_min][k]!=float('inf'):
                new_dis = dis[cur_min]+matrix[cur_min][k]#更新新的路径长度
                if new_dis < dis[k]:
                    dis[k] = new_dis
                    #path[i] = cur
    res = 0
    for i in dis:
        if i==float('inf'):
            res=-1 
            break
        else:
            if res<i:
                res=i
    print(res)
        
if __name__ =="__main__":
    func()                    
    