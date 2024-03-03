dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
direction_type = ['R', 'L', 'U', 'D']
x, y = 1, 1

n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

for plan in plans:
    i = direction_type.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 < nx <= n and 0 < ny <= n:
        x = nx
        y = ny


print(x, y)