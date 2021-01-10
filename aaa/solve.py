from collections import deque
def change(d):
    if d==0: #북->서
        return 3
    elif d==1: #동->북
        return 0
    elif d==2: #남->동
        return 1
    elif d==3: #서->남
        return 2
def bfs(y,x,d):
    mapp[y][x]=2
    cnt=1
    dq=deque()
    dq.append([y,x,d])
    while dq:
        chk=0
        y,x,d=dq.popleft()
        for i in range(4):
            cd=change(d)
            cy,cx=y+dy[cd],x+dx[cd]
            if mapp[cy][cx]==1 or mapp[cy][cx]==2:
                chk+=1
                d=cd
                continue
            elif mapp[cy][cx]==0:
                mapp[cy][cx]=2
                cnt+=1
                dq.append([cy,cx,cd])
                break
        if chk==4:
            by,bx=y-dy[d],x-dx[d]
            if mapp[by][bx]==1:
                return cnt
            else:
                dq.append([by,bx,d])
n,m=map(int, input().split())
y,x,d=map(int, input().split())
mapp=[list(map(int, input().split())) for _ in range(n)]
dy,dx=[-1,0,1,0],[0,1,0,-1]#북 동 남 서
print(bfs(y,x,d))
