from array import *
value = array('i',[1,-2,3,4,5])
new_array = array(value.typecode,(a for a in value))
for j in range(len(new_array)):
    print(new_array[j])








