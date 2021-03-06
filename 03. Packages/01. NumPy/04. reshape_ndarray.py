#reshape ndarray:
d = np.zeros((2, 3))
h = d.reshape((3, 2, 1)) #(3,2,1) shape, three dimension
  '''
  -> [[[0.]
      [0.]]
     [[0.]
      [0.]]
     [[0.]
      [0.]]]
  '''
#we need to keep the total number of elements equal
#if we do not know the number of some dimension, we can use -1 and the api will calculate for us
i = d.reshape((3,-1))
  '''
  -> [[0. 0.]
      [0. 0.]
      [0. 0.]]
  '''
