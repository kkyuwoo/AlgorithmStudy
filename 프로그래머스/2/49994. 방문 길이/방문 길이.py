def solution(dirs):
    answer = 0
    arr = set()
    x, y = 0, 0
    for i in dirs:
        if i == 'U':
            nx, ny = x, y+1
            if ny <= 5:
                arr.add((x, y, nx, ny))
                arr.add((nx, ny, x, y))
                x, y = nx, ny
        elif i == 'D':
            nx, ny = x, y-1
            if ny >= -5:
                arr.add((nx, ny, x,y))
                arr.add((x, y, nx, ny))
                x, y = nx, ny
        elif i == 'R':
            nx, ny = x+1, y
            if nx <= 5:
                arr.add((nx, ny, x,y))
                arr.add((x, y, nx, ny))
                x, y = nx, ny
        elif i == 'L':
            nx, ny = x-1, y
            if nx >= -5:
                arr.add((nx, ny, x,y))
                arr.add((x, y, nx, ny))
                x, y = nx, ny
    answer = len(arr)/2
    return answer