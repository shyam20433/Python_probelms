def permutation(nums):
    def backtrack(path,remaining):
        if not remaining:
            result.append(path)
            return
        for i in range(len(remaining)):
            backtrack(path+[remaining[i]],remaining[:i]+remaining[i+1:])
    result=[]
    backtrack([],nums)
    return result


print(permutation([1,2,3]))