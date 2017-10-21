# -*- coding: utf-8 -*-

def Mergesort(arr):
    b = len(arr)
    if b<=1:
        return arr
    arr_c = []
    a = len(arr)//2
    arr_a = Mergesort(arr[:a])
    arr_b = Mergesort(arr[a:])

    while len(arr_c)<b:
		'''
		先判断列表是否有一列表被删除完，
		如果有先赋值后退出
		'''
		if len(arr_a)==0:
            arr_c.extend(arr_b[:])
            break
        if len(arr_b)==0:
            arr_c.extend(arr_a[:])
            break
		#根据大小关系赋值
        if arr_a[0]<arr_b[0]:
            arr_c.append(arr_a.pop(0))
        elif arr_a[0]>arr_b[0]:
            arr_c.append(arr_b.pop(0))
        elif arr_a[0] == arr_b[0]:
            arr_c.append(arr_a.pop(0))
            arr_c.append(arr_b.pop(0))
        else:
            pass
    return arr_c

print(Mergesort([101,1,5,2257,24,75,45,72,457,25,7,17,8,9,8573,3,6,27,257,47,2]))
input()