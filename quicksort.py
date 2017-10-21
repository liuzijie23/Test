#!/program files/python36/evn python
# -*- coding:utf-8 -*-

#从Python2.2开始，增加了一个操作符 // ，以执行地板除（整除）：
#除法不管操作数为何种数值类型，总是会舍去小数部分，返回数字序列中比真正的商小的最接近的数字

def quicksort(arr):	#定义函数
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]	#取中间值为基准元素
    left = [x for x in arr if x < pivot]	#取出比pivot小的元素
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)	#递归得出结果
	
print (quicksort([3,6,8,10,1,2,1,2,54,36,36,0,72,7]))