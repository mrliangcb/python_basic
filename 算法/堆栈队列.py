#堆栈队列  stack  queue

# 先入后入

#判断()是否合法，左右匹配
#()[]  ([])]不合法
#[先入，遇到]就都出去  [ ( ] 于是都出不去，string已经遍历完了，栈还没出空，所以不匹配
# 每个元素O1，n个元素就是on    空间也是on

# def isValid(self,s):
	# stack=[]
	# paren_map={')':'(',']':'[','}':'{'}  
	# for c in s:
		# if c not in paren_map:# 不在右边，则压入
			# stack.append(c) #压入用append
		# elif not stack or paren_map[c]!=stack.pop() #如果是右边元，但是又不和栈顶匹配，就返回不匹配
			# return Fales
		# return not stack #如果遍历完了，检查一下是否空，空则返回true

a={'a':'b'} #检查b在Key中有出现吗，不是value
print('b' in a) #False
b=[1,2,3]
print(b.pop()) #pop(0)打出栈底
print(b)


#replace"()",""   从小到大匹配然后消除,时间复杂度不好计算



#优先队列
#堆heap  binary search tree二叉搜索树
#二叉堆  头是最小的元素，父节点比儿子节点要小
#大顶堆  与上面相反

#优先队列题目
# 拿到一个stream数据
# 求第几大的元素在第几位
# [4,5,8,2]  k=3
# 方法一：求最大的k个，见到比盒子里面大的，就踢出去，新的进来，盒子内排序。遍历n个，记住最大的那个    N*klogk     概率

# 方法二:小顶堆  min heap  元素个数为k
   # 4
 # 5   8
 # 2比4小，10比4大，4走人，10 进来，再排序
   # 5
# 10     8
# N (1+log2(k) )   概率 若比5小，复杂度1，因为只和顶对比   若比5大，拿进来，然后排序
#我想用二叉树做这个堆，因为k不一定是3，有可能更多    


	





















