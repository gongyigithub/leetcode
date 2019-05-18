# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

# （这里，平面上两点之间的距离是欧几里德距离。）即平方

import heapq
def kClosest(points,K):
    '''
    先求出所有的点到原点的距离，再排序取前K个值
    in param points:坐标列表
    in param K:要输出的点的个数
    return:列表
    '''
    length = sorted(points,key=lambda x:x[0]**2+x[1]**2)
    return length[:K]



# points = [[1,3],[-2,2]], K = 1
# [[-2,2]]

points = [[1,3],[-2,2]]
K = 1
result = kClosest(points,K)
print(result)
