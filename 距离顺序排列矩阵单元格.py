# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。

# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。

# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

def allCellsDistOrder(R,C,r0,c0):
    '''
    根据输入矩阵行列和初始坐标，按矩阵内到初始坐标的距离输出矩阵所有的点
    in param R:矩阵行
    in param C:矩阵列
    in param r0:初始坐标行
    in param c0:初始坐标列
    return:列表
    '''
    num = R*C
    List = [[]]*num
    i,j,k = 0,0,0
    for i in range(R):
        for j in range(C):
            List[k] = [i,j]
            k += 1
    re = sorted(List,key=lambda x:abs(x[0] - r0) + \
        abs(x[1] - c0))
    return re

#更简单的生成点列表方法：result = [[i,j] for i in range(R) for j in range(C)]

# 输入：R = 2, C = 3, r0 = 1, c0 = 2
# 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。

R,C,r0,c0 = 2,3,1,2
a = allCellsDistOrder(R,C,r0,c0)
print(a)
