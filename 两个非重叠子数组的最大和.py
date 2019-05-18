# 给出非负整数数组 A ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 L 和 M。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）

#思路：先求长为L的最大子序列和，再在其左侧或右侧求M子序列的最大和.
def maxSumTwoNoOverlap(A,L,M):
    '''
    求两个不重叠的指定长度最大子序列和
    in param A:非负整数数组
    in param L:子序列长度
    in param R:子序列长度
    '''
    N = len(A)
    i,j = 0,0
    maxL = 0
    resultM1,resultM2 = [0,0],[0,0]
    while i < N:
        resultL = sum(A[i:i+L])
        print('L最大序列和以及i值',resultL,i)
        if i >= M:
            resultM1 = getMaxSequence(A[:i],M)
            print('M在L前边',A[:i],resultM1)
        if i+L+M <= N:
            resultM2 = getMaxSequence(A[i+L:],M)
            print('M在L后边',A[i+L:],resultM2)
        if i < M and i+L+M > N:
            break
        num_sum = resultL + max(resultM1[0],resultM2[0])
        print('L+M',num_sum)
        if maxL < num_sum:
            maxL = num_sum
        i += 1
        resultM1,resultM2 = [0,0],[0,0]
    return maxL

def getMaxSequence(A,L):
    '''
    求数组A中长度为L，且和最大的子序列
    '''
    max = 0
    first = 0
    for i in range(len(A)):
        result = sum(A[i:i+L])
        if result > max:
            max = result
            #记录下得到max时的i值，可以得出L的最大子序列位置
            first = i
    return max,first

# 输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# 输出：31
# 解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
# [1,0,3] 1 2   -----4

A = [66,94,97,51,41,94,3,62,45,92,23,93,94,6,41,24,95,98,83,11,3,30,49,95,76,38,14,64,62,77,10,76,33,66,52,89,22,37,59,38,73,90,47,38,39,57,38,44,85,82,68,68,0,38,91,35,1,25,15,86,98,90,90,16,30,83,85,4,89,28,18,51,67,91,75,57,96,11,23,57,6,62,69,44,80,26,19,79,39,46,93,74,86,56,50,40,68,34,43,70]
L = 67
M = 18
result = maxSumTwoNoOverlap(A,L,M)
print(result)



class Solution:
# 思路：dp
# a,b分别记录前i项最大值
# 对于位置i, 最大值=前L项+b[i-L] 或者 前M项]+a[i-M] 或者前i-1位置的最大值
# res = max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        a, b = [0] * n, [0] * n  # a是L,b是M
        res = 0
        for i in range(1, n):
            A[i] += A[i - 1]
        for i in range(n):
            a[i] = A[i] if i < L else max(a[i - 1], A[i] - A[i - L])
            b[i] = A[i] if i < M else max(b[i - 1], A[i] - A[i - M])
            res = A[i] if i < L + M else max(res, A[i] - A[i - L] + b[i - L], A[i] - A[i - M] + a[i - M])
        return res

