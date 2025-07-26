def n_queen(n):
    col=set()
    pos=set()
    neg=set()
    result=[]
    board=[["-"]*n for i in range(n)]
    def backtrack(r):
        if r==n:
            copy=[''.join(i) for i in board]
            result.append(copy)
            return 
        for c in range(n):
            if c in col or (r+c) in pos or (r-c) in neg:
                continue
            col.add(c)
            pos.add(r+c)
            neg.add(r-c)
            board[r][c]="Q"
            backtrack(r+1)
            col.remove(c)
            pos.remove(r+c)
            neg.remove(r-c)
            board[r][c]="-"
        
    backtrack(0)
    return result
    
for solution in n_queen(8):
    for row in solution:
        print(row)
    print()