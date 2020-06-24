#set is unordered collection of unique elements.
#set is a special hashtable which contains only keys.

#code:
#create set:
x = set('abc') 
  -> {'a','b','c'}
x = {'a','b','c'}

#add new element:
x.add('') #add can only add one element to set, two or more elements will result in TypeError
x.update({'',''}) #update can add multiple elements to set, but need to have the {} sign

#delete element:
x.remove('') #will have KeyError if the element does not exist
x.discard('') #will not have KeyError if element does not exist
x.pop() #delete one random element, if set is None, return KeyError
x.clear() #remove all elements

#union two sets:
x = {'a','b','c'}
y = {'c','d','e'}
x.union(y) #will return a set with random order that contains all elements in two sets but no duplication
    -> {'a','b','c','d','e'} #may not in this order!!!!
x | y #same function with union()

#difference between two sets:
x = {'a','b','c'}
y = {'c','d','e'}
x.difference(y)
    -> {'a','b'} #the elements that are in x but not in y
y.difference(x)
    -> {'d','e'} #the elements that are in y but not in x

#intersection:
x = {'a','b','c'}
y = {'c','d','e'}
x.intersection(y) #will return the common element
x & y #same with intersection()

#logic operation:
if 'key' in x:
    ......
if 'key' not in x:
    ......
x == y #check whether x == y, and return True or False
x != y #check not equivalent
x <= y #check subset(x is subset of y or not)
x < y #check proper subset, the difference with subset is that if x == y, x<=y return True but x<y return False. x<y is True means x must some but not all elements in y
x >= y #same with <=
x > y #same with <
x - y #the elements in x but not in y
x ^ y #the elements only exist in one set (union - intersection)

#use set to deal with list problem:
#suppose we have two list and want to get the common elements.
#list solution:
list1 = [...]
list2 = [...]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
#set solution:
list1 = [...]
list2 = [...]
set1 = set(list1)
set2 = set(list2)
set1.intersection(set2)
