# 第3章.map 和 set 



# 哈希函数和哈希表
# 比如存10个同学的名字，然后利于查找，就用到哈希函数，比如'abc'这个名字，把a,b,c三个字符的asc码求和，然后对总人数10求模，就是取余，就是排名了  
# 计算排名的这个函数，就是哈希函数
# 问题：会有重复，一个排名对多个元素:哈希碰撞
# 拉链法:横向放元素
# 对比list、map、set   map可以理解为字典，集和就是map的key，但不重复
# map/set 都有哈希(搜索的复杂度o1)和树(排好顺序)两种实现形式    若不要求搜索过程有序，则优先用哈希表
# set可以存数字，turple() 
# set如何添加元素  set.add()  如果已经有就覆盖，如果还未有就增加
# set长度  len(set)

# 复杂度怎么会有log:
# [1,2,3,4,5,6,7]  假设我们要找数组中6值的位置，我们假设每次都是做最坏打算的操作，中点为4，最坏我们搜索左边,即1/2 * 7= 3次,剩下4元，我们又分一半,4/2=2是先搜左边4,5,
# 然后分半2/2=1 搜7,最后才是6    7*(1/2)^3=1    n=2^k  注意这里是搜索（二分搜索）不是遍历。排序，查找 一般最坏情况都是NlogN
# 快排序的最坏情况n^2 平均是nlogn  取决于主元选的好不好 


# 题目 242   anagram 字母都一样，但顺序不同的两个词.  cat  tac  atc   判断两个词是否这种情况
# 快排序平均复杂度NlogN
# map计数{letter:出现次数}   因为要遍历字符串On  插入删除查询都O1  这个速度比快排序快

#快排序(二分法)  NlogN
def test(s,t):
	return sorted(s)==sorted(t) #先各自排序，然后判断是否一模一样

	
# map 哈希
def test2(s,t):
	dic1,dic2={},{}
	for item in s:
		dic1[item]=dic1.get(item,0)+1#dict.get(key, default=None)返回指定key的value，如果不存在，则返回默认的0
	for item in t:
		dic2[item]=dic2.get(item,0)+1
	return dic1==dic2
# on复杂度
print(test2('dabc','bacd'))
#分别统计字符出现的次数，然后看两个字典是否相同

# two sum   three sum 用map解决 
# [2,7,11,15]   和9   返回下标[0,1]
# 法一：暴力for循环,On^2
# 法二：set x+y=9转化为y=9-x   On找x,set为9-x(O1)    
#

# 三数之和  
# [-1 0 1 2 -1 -4 ]    a+b+c=sum
# 法一:暴力循环 On^3
# 法二：c=-a-b  遍历a和b，结果放在set，然后再set寻找是否有c  on^2
# 
# 法三：sort find   nlogn   遍历a，找出一个a之后，其他数进行排列，从小到大，b指向头,c指向尾，若a+b+c>sum  减小一点，所以c左移，若<sum，则b右移，增大
# sorted(data, cmp=None, key=None, reverse=False)  
# a=sorted([3,1,5,2,4])
# set 可以装进list[]
# print(a)

# 15题
#法二
def threeSum(nums):
	if len(nums)<3:
		return []
	nums.sort()
	res=set()
	for i,v in enumerate(nums[:-2]):#因为最后两位至少要放bc两个指针
		if i>=1 and v==nums[i-1]: 
			continue
		d={}
		for x in nums[i+1:]:
			if x not in d:
				d[-v-x]=1
			else:
				res.add((v,-v-x,x))#相当于append一个turple
	return map(list,res),res

a,b=threeSum([-1,1,0,4,5,6])
print('方法2',list(a))
print(b)

# 法三
def threeSum2(nums):
	res=[]
	nums.sort()  #先对题目序列排序
	for i in range(len(nums)-2): # 遍历0到倒数第3个
		if i>0 and nums[i]==nums[i-1]: #若i>0  i的值等于前一个，则直接跳下一步
			continue
		l,r=i+1,len(nums)-1 #初始：取左右指针，i的下一个  和末尾的一个
		while l<r:#左指针小于右指针
			s=nums[i]+nums[l]+nums[r] #求和
			if s<0:l+=1 #和小于目标，那就大一点，左边右移
			elif s>0:r-=1
			else:
				res.append([nums[i],nums[l],nums[r]]) #如果和等于目标，则保存这三个数  然后跳过重复元素
				while l<r and nums[l]==nums[l+1]: #左指针小于右 ，左指针的下一个等于他
					l+=1
				while l<r and nums[r]==nums[r-1]:# 右指针与左边一个相同，则左移
					r-=1
				l+=1;r-=1 #左指针右移，右指针左移  就是左边大了一点，右边小了一点   直到左右指针相遇就结束，然后下一个i
	return res
b=threeSum2([-1,1,0,-1,5,6])
print(b)









