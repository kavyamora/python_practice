'''
list 
 1.represented in []
 2.mutable data type(change anywhere)
 3.allow duplicates
 4.allow indexing
 '''
#v=[]
# print(type(v))

# v=[1,12,13,14,15,25,'kiran']
# print(type(v))
# print(v[2])
# print(v[-3])
# print(v[0:6:2])
# print(v[2:4:1])
# print(v[2:-4:1])

'''
list types of arguments
   1.append-insert
   2.insert-add
   3.extend-for extending the list
   4.change the name based on index
   5.change the name based on  range
   6.remove-delete the one name from the list
   7.pop-pop also used for delete the one value from list 
   8.sort-used for essending order
   9.reverse-used for decending order
'''
'''
1.append
  syntax=variable_name.append('value_name')
   '''

num = [12, 13, 15, 17, 89, 90]

num.append(50)
num.insert(2, 34)
num.extend(['kiran'])

num[1:2] = ['siva', 'manu']
num[2] = 'anu'

num.remove(12)
num.pop(2)

num.reverse()

print(num)
