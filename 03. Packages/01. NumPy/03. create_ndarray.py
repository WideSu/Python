#different ways to create ndarray:
b = np.arange(0, 10, 2, dtype='float') # create 1d array, start from 0 and stop at 10 (not included) with step = 2.
print(b)
  #-> [0. 2. 4. 6. 8.]
print(b.shape)
  #-> (5,) #tuple

c = np.linspace(1.5, 2.5, 9) # create 1d array with 9 float number, from 1.5 to 2.5 (included).
print(c)
  #-> [1.5 1.625 1.75 1.875 2. 2.125 2.25 2.375 2.5]
print(c.shape)
  #-> (9,)

d = np.zeros((2, 3)) # all zeros
print(d)
  '''
  -> [[0. 0. 0.]
      [0. 0. 0.]]
  '''

e = np.ones((2, 3)) # all ones
print(e)
  '''
  -> [[1. 1. 1.]
      [1. 1. 1.]]
  '''
     
f = np.full((2, 3), 9) # constant matrix, (2,3) shape with number 9
print(f)
  '''
  -> [[9 9 9]
      [9 9 9]]
  '''

g = np.eye(3) # 3 x 3 identity matrix (1 on main diagonal and 0 on other positions)
print(g)
  '''
  -> [[1. 0. 0.]
      [0. 1. 0.]
      [0. 0. 1.]]
  '''
