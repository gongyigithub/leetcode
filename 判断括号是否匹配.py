def judgeK(s):
    '''
    输入字符串s，判断其中的括号是否匹配。空字符串也匹配
    in param s:字符串s，空或者全是括号
    return:bollean
    '''
    # 模拟堆栈是比较好的，用列表代替表示堆栈，后进先出
    stack = []
    if len(s) == 0:
        # 空字符串
        return True
    else:
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if not isMatch(stack.pop(), i):
                	return False
        if len(stack) == 0:
	        return True
	    else:
	    	return False

def isMatch(q1, q2):
    '''
    判断传入的括号1和括号2是否匹配
    in param q1:括号1
    in param q2:括号2
    return:boolean
    '''
    if q1 == '(':
        return q2 == ')'
    elif q1 == '[':
        return q2 == ']'
    elif q1 == '{':
        return q2 == '}'
    else:
        pass



def judge1(s):
	'''
	leetcode上高赞答案。给的s里只有各种括号，必有一对是在一起的，所以用while循环，
	逐对替换
	'''
	while '()' in s or '[]' in s or '{}' in s:
		s = s.replace('()','')
		s = s.replace('[]','')
		s = s.replace('{}','')
	return s == ''
s = '('
re = judge1(s)
print(re)
