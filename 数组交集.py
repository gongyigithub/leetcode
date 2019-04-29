def interact(nums1,nums1):
	'''
	求两数组交集，忽略重复值
	'''
	result = []
	for i in nums1:
		if i in nums2:
			result.append(i)
	
	return list(set(result))