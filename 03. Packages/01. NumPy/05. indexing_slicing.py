#indexing and slicing:
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)
  '''
  -> [[1,2,3,4]
      [5,6,7,8]
      [9,10,11,12]]
  '''
b = a[:2, 1:3] # 0,1 row and 1,2 column
print(b)
  '''
  -> [[2 3]
      [6 7]]
  '''
print(a[1]) # access a row
  #-> [5 6 7]
print(type(a[1]))
  #-> numpy.ndarray
print(a[:, 1:2]) # access a col, the first part is unavoidable because if only write one part, it is row not column.
  '''
  -> [[ 2]
      [ 6]
      [10]] #numpy.ndarray
  '''
print(a[1, 1]) # access single value
  #-> 6 #numpy.int

# (Advanced)Two ways of accessing the data in the middle row of the array.
r1 = a[0, :] # rank 1 view of the first row
r2 = a[0:1, :] # rank 2 view of the first row 
print(r1, r1.shape)
  #-> [1 2 3 4] (4,) #use index only, we get a shape of one dimension
print(r2, r2.shape)
  #-> [[1 2 3 4]] (1, 4) #use slicing, we get a shape of two dimension
num_col = r1.shape[0]
r1 = r1.reshape(-1, num_col)
print(r1, r1.shape)
  #-> [[1 2 3 4]] (1, 4)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#boolean masking:
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a_idx1 = (a < 5) # return the boolean array that satisfies the conidtion
print(a_idx1)
  '''
  -> [[ True  True  True  True]
      [False False False False]
      [False False False False]]
  '''
a_idx2 = (a >=5) & (a <= 10) # return the boolean array that satisfies the conidtion
print(a_idx2)
  '''
  -> [[False False False False]
      [ True  True  True  True]
      [ True  True False False]]
  '''

print(a[a_idx1]) # return the corresponding array
  #-> [1 2 3 4] #will return number where true appears
print(a[a_idx1].shape)
  #-> (4,)
print(a[a_idx2]) # return the corresponding array
  #-> [ 5  6  7  8  9 10]
print(a[a_idx2].shape)
  #-> (6,)

