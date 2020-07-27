#create ndarray:
a = np.array([[10, 11, 12], [13, 14, 15]])
  '''
  -> [[10,11,12]
       13,14,15]]
  '''
b = np.arange(1, 7).reshape((2, 3))
  '''
  -> [[1,2,3]
      [4,5,6]]
  '''

# element-wise calculation:
print(a + b)
  '''
  -> [[11,13,15]
      [17,19,21]]
  '''
print(a - b)
  '''
  -> [[9,9,9]
      [9,9,9]]
  '''
print(np.add(a, b))
  '''
  -> [[11,13,15]
      [17,19,21]]
  '''
print(a * b)
  '''
  -> [[10 22 36]
      [52 70 90]] #position to position
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Matrix product:
print(np.dot(a, b.transpose())) # 2x3, 3x2
  '''
  -> [[ 68 167]
      [ 86 212]]
  '''
print(a.T.dot(b)) # 3x2, 2x3. a.T = a.transpose()
  '''
  -> [[ 62  85 108]
      [ 67  92 117]
      [ 72  99 126]]
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#row sum and column sum:
# Axis 0 will sum all the ROWS in each COLUMN
# Axis 1 will sum all the COLUMNS in each ROW
print(np.sum(a, axis = 0)) # the column is fixed, act along row for this column
  #-> [23 25 27]
print(np.sum(a, axis = 1)) # the row    is fixed, act along column for this row
  #-> [33 42]
