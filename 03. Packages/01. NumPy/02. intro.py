#At the core of the NumPy package, is the ndarray object. 
#This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance. 
#In short, ndarray is a good way to process matrix.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#intro code:
lst = [[1, 2, 3], [4, 5, 6]] # 2x3
a = np.array(lst) # create array from lists
print(type(a)) 
  #-> class 'numpy.ndarray'
print(a)
  #-> [[1 2 3]
      [4 5 6]]
print(a[0]) # first row
  #-> [1 2 3] #type: 'numpy.ndarray'
print(a[0][1]) # first row, second column
  #-> 2 #type: 'numpy.int64'
print(a.shape) # 2 x 3
  #-> (2,3)
print(a.ndim) # 2 dimensions
  #-> 2 #a fast way to find number of dimension is to find how many [ the outest matrix has 
print(a.dtype) # data type of the elements of array
  #-> int
print(a.size) # total number of elements in the matrix
  #-> 6
