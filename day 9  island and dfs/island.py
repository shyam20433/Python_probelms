matrix=[
    ['1','1','1'],
    ['0','0','0'],
    ['1','1','1']
]

def island(matrix):
    r=len(matrix)
    c=len(matrix[0])
    count=0
    for i in range(r):
        for j in range(c):
            if matrix[i][j]=="1":

                
                dfs(matrix,i,j,r,c)
                count+=1
    return count

def dfs(matrix,i,j,r,c):
    if i<0 or j<0 or i>=r or j>=c or matrix[i][j]!='1':
        return 
    matrix[i][j]='0'
    dfs(matrix,i+1,j,r,c)
    dfs(matrix,i-1,j,r,c)
    dfs(matrix,i,j+1,r,c)
    dfs(matrix,i,j-1,r,c)

print(island(matrix))