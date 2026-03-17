list =['a','c','g','t','y']
print(list[0:4])

#list functions 
#list slicing
print(list[:4])

#add an element in the list 
print(list.append('e'))

#list sorting 
list.sort()

#list sorting in reverse order
list.reverse()
print(list)

#insert element at index
list.insert(5,'r')
print(list)

#remove the first occurence of element 
list.remove('a')
print(list)

#remove the element at an index completely
list.pop(2)
print(list)

#count occurence of an element 
count =list.count('a')
print(count)