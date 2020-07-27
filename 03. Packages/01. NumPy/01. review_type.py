#numeric types:
x = 2 #class 'int'
y = 1.5 #class 'float'
-------------------------------------------------------------------------------------------------------------------------------
#boolean (True/False):
t = True
f = False
print(type(t)) # class 'bool' 

print(t or f) # True
print(t and f) # False 

print(not t) # False
print(not f) # True
-------------------------------------------------------------------------------------------------------------------------------
#string:
s1 = 'single quote' # use single quotes
s2= "double quote" # use double quotes 

s3 = s1 + ' and ' + s2 # string concatenation
  #->single quote and double quote
  
'Caplitalize the string: ' + s3.capitalize() # Caplitalize the string (first letter)
'Uppercase the string: ' + s3.upper() # Uppercase the string (all)

s3.count('o') # Count the occurrences of a character
s3.index('te') # The lowest index of the occurrence

s3[1] #indexing

s = "{} is handsome, but {} is not"
print(s.format('Rayman','Jason'))
  #->Rayman is handsome, but Jason is not
s = "{1} is handsome, but {0} is not, {2} is super handsome"
print(s.format('Jason', 'Rayman', 'Mike'))
  #->Rayman is handsome, but Jason is not, Mike is super handsome
s = "{name1} is handsome, but {name2} is not"
print(s.format(name2 = 1, name1 = 'Rayman'))
  #->Rayman is handsome, but 1 is not
-------------------------------------------------------------------------------------------------------------------------------
#list (mutable):
lst1 = [1, 2, 3, 4] # create a list with same data type values
lst2 = ['one', 2, 'three', 4] # create a list with different data type values
lst3 = lst1 + lst2 # list concatenation

lst1.append(5) # append a new element to end of the list
lst1.pop(3) # remove the 4th element of the list

lst1[2] = 100 # indexing & list is mutable
lst1.index('1') # get index
-------------------------------------------------------------------------------------------------------------------------------
#Tuple (immutable):
t = (21, 42) # create a tuple
-------------------------------------------------------------------------------------------------------------------------------
#dictionary:
score_dict = {'A': 90, 'B': 80, 'C': 1, 'D': 59} # create a dictionary
print(score_dict['A']) # get A score
print('B' in score_dict) # check if 'B' in the dictionary

score_dict['E'] = 70 # Add a new key-value pair to the dictionary
score_dict['C'] = 100 # Modify the existing value in the dictionary

score_dict.pop('B') # remove
-------------------------------------------------------------------------------------------------------------------------------
