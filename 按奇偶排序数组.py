# 非负整数数组A，A中一半奇书，一半偶数。对数组进行排序，使得A[i]时奇数时，i也是奇数
# A[i]是偶数时，i也是偶数


def sortArrayByParity(A):
    '''
    将数组按奇偶数排序
    in param A:整数数组A
    return:排序后的数组A
    '''
    N = len(A)
    result = ['']*N
    i, j = 0, 1
    for num in A:
        if num % 2 == 0:
            # 是偶数
            result[i] = num
            i = i + 2
        else:
            # 是奇数
            result[j] = num
            j += 2
    return result


def sortArrayByParity1(A):
    '''
    python高赞解法，利用了zip函数
    '''
    # 先使用列表生成器生成两个列表，分别是偶数和奇数
    ou = [i for i in A if i % 2]
    ji = [i for i in A if not i % 2]
    # 利用zip函数将两个列表ou和ji合并成一个个元组，每个元组中一个偶数一个奇数
    # 再遍历元组列表，将元组列表中的数字一一取出，构成最终列表返回
    return [i for n in zip(ji, ou) for i in n]

# 测试
A = [4, 2, 5, 7]  # output：[4,5,2,7]或者[4,7,2,5]或者[2,5,4,7]或者[2,7,4,5]
s = sortArrayByParity1(A)
print(s)
