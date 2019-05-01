# 给定由一些正数（代表长度）组成的数组A，返回由其中三个长度组成的、
# 面积不为零的三角形的最大周长。如果不能形成任何面积不为零的三角形，返回 0。

# 三角形要求两边之和大于第三边，两边之差小于第三边

# 先排序，之后取末尾三个数字，若n-2 + n-1 < n，则递归n-1。若满足就是最大边长三角形

def largestPerimeter(A):
    '''
    求数组A中能组成的最大周长三角形
    in param A:正整数数组A
    return :最大周长或者0
    '''
    if len(A) == 3:
        if isTriangle(A[0],A[1],A[2]):
            return sum(A)
        else:
            return 0
    else:
        A.sort()
        if isTriangle(A[-1],A[-2],A[-3]):
            return sum(A[-3:])
        else:
            num = A.pop()
            return largestPerimeter(A)

def isTriangle(a,b,c):
    '''
    判断传入的a、b、c能否组成三角形
    '''
    return a+b>c and abs(a-b)<c and a+c>b and abs(a-c)<b \
         and b+c>a and abs(b-c)<a

# 测试用例[3,2,3,4]——>10,[3,6,2,3]——>8
A = [3,7,2,3]
a = largestPerimeter(A)
print(a)
print(largestPerimeter(A))
