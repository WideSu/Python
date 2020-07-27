a = np.array([[10, 11, 12], [13, 14, 15]]) # 2x3
print(a)
  '''
  -> [[10 11 12]
      [13 14 15]]
  '''

a += 1 # add 1 to all the elements # 1
print(a)
  '''
  -> [[11 12 13]
      [14 15 16]]
  '''

a += np.array([-1, -2, -3]) # add [-1, -2, -3] to all columns for each row # 3
print(a)
  '''
  -> [[10 10 10]
      [13 13 13]]
  '''

a += np.array([[-1], [-2]]) # add [[-1], [-2]] to all rows for each column 2x1
print(a)
  '''
  -> [[ 9  9  9]
      [11 11 11]]
  '''
