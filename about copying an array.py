from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1
print(arr2)
print(arr1)
print(id(arr1))
print(id(arr2))
"""this type of copying is know as aliasing, here we are not suppose to store the two value"""
###SHOLLOW COPY###
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
print(arr2)
print(arr1)
print(id(arr1))
print(id(arr2))
#  here the address of value is different but they are inter dependent
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
arr1[1]=66
print(arr2)
print(arr1)
print(id(arr1))
print(id(arr2))
"""the id of array is different but if we change the value of one array it carried through another array
if we don't want to carry the changed value to next array we need to use the function called depp copy
so how can we use this function means instead of .view() we use ,copy()"""

arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
arr1[1]=66
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


