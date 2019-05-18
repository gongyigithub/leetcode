# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
def sortColors(nums):
    '''
    快速排序，1作为基准值
    '''
    left,right = [],[]
    pivot_list = []
    for i in range(len(nums)):
        if nums[i] < 1:
            left.append(nums[i])
        elif nums[i] == 1:
            pivot_list.append(nums[i])
        else:
            right.append(nums[i])
    return left+pivot_list+right

def sortColor(nums):
    '''
    无返回值版本，直接修改nums
    '''
    print(nums)
    N = len(nums)
    j,i = 0,0
    pivot = 1
    index = N-1
    while i < N:
        print('i值，',i,nums[i])
        if nums[i] < pivot and i >= j:
            nums[j],nums[i] = nums[i],nums[j]
            j += 1
            print(nums,j,'小于')
        elif nums[i] > pivot and i <= index:
            nums[i],nums[index] = nums[index],nums[i]
            index -= 1
            print(nums,index,'大于')
        else:
            i += 1

def sortColors2(self, nums):
    '''
    直接比较输出
    '''
    nums[:] = [x for x in nums if x < 1] + [x for x in nums if x == 1] + [x for x in nums if x > 1]


nums = [1,2,0]
a = sortColor(nums)
print(a)
