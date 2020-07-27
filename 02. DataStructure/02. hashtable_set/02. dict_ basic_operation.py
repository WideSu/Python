#basic operations include create, add, delete, update, look up.

#create:
my_dict = {} #create empty dictionary 
my_dict = {'A':'1','B':,'2'}

#look up:
grades = {'A':'A+','B':'A-','C':'F','D':'B'}
grades['A'] => 'A+'
grades['E'] => keyerror
  #how to avoid keyerror:
    #dictionary.get(key,default_val) => if key in dict, return its value, if not in dict, return default value
    grades.get('A','F') => 'A+'
    grades.get('F','F') => 'F'
    #use if to check:
    if 'A' in grades => returns True
    if 'F' in grades => returns False

#add:
grades['F'] = 'F'

#update:
grades['A'] = 'A-' #same syntax with add but the only difference is whether the key exists or not

#delete:
del grades['A'] #no return
grades.pop('A') #pop function deletes and returns value

#get value:
list(grades.values()) #get all values and make them into a list

#get keys:
list(grades.keys()) #get all keys and make them into a list

#get items:
grades.items() #get keys and values [('key','value'),('key','value'),...]

#complexity:
#time O(1)
#space O(n)
