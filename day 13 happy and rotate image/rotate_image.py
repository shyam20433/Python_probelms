def rotate_image(a):
    result=[]
    for i in range(len(a)):
        b=[]
        for row in a:
            b.append(row[i])
        result.append(b)
    matrix=[]
    for row in result:
        matrix.append(row[::-1])

    return matrix


print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))


class Solution(object):
    def rotate(self, matrix):
        matrix[:]=[[row[i] for row in matrix[::-1]]for i in range(len(matrix))]
