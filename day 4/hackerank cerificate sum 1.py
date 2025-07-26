
def count(matrix):
    count1=0
    n=len(matrix)
    m=len(matrix[0])

    for i in range(n):
        for j in range(m):
            is_dominant=True

            directions=[(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(1,0),(0,-1),(-1,0)]
            for ni,nj in directions:
                dr=i+ni
                dj=j+nj
                if 0<=dr<n and 0<=dj<m:
                    if matrix[i][j]<matrix[dr][dj]:
                        is_dominant=False
            if is_dominant:
                count1+=1
    return count1

a=[[11,2,33],
   [4,5,6],
   [27,8,9]]
print(count(a))


