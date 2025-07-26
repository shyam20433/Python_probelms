def island(matrix):
    n=len(matrix)
    m=len(matrix[0])
    perimeter=0

    for i in range(n):
        for j in range(m):
            if matrix[i][j]=="1":
                perimeter+=4


                direction=[(0,1),(1,0),(0,-1),(-1,0)]

                for ri,rj in direction:
                    nr=i+ri
                    nj=j+rj

                    if 0<=nr<n and 0<=nj<m and matrix[nr][nj]=="1":
                        perimeter-=1
    return perimeter

a=[["1","1","1"],
   ["0","0","1"],
   ["1","0","0"]]
print(island(a))

                    