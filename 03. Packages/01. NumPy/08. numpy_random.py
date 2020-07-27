#generate random number
print(np.random.rand(2,2)) # Random numbers between [0,1) of shape 2,2
  '''
  -> [[0.94295205 0.11725689]
      [0.85325198 0.83939604]]
  '''
print(np.random.randn(2,2)) # Normal distribution with mean=0 and variance=1 of shape 2,2
  '''
  -> [[ 0.62820658 -0.12022571]
      [-2.00169518 -0.24775009]]
  '''
print(np.random.randint(0, 10, size=[2,2])) # Random integers between [0, 10) of shape 2,2
  '''
  -> [[3 1]
      [0 7]]
  '''
print(np.random.random()) # One random number between [0,1)
  #-> 0.2907313460399378
print(np.random.random(size=[2,2])) # Random numbers between [0,1) of shape 2,2
  '''
  -> [[0.4916531  0.06636227]
      [0.17424549 0.39105589]]
  '''
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)) # Pick 10 items from a given list, with equal probability
  #-> ['o' 'i' 'o' 'a' 'i' 'o' 'e' 'o' 'o' 'o']
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10, p=[0.3, 0.1, 0.1, 0.4, 0.1])) # Pick 10 items from a given list with a predefined probability 'p'
  #-> ['o' 'o' 'a' 'i' 'u' 'o' 'a' 'u' 'o' 'i']
print(np.random.choice(np.arange(100), size=[10,3], replace=True)) # get 10x3 random samples from [0-99] with replacement 
  '''
  -> [[30 76 93]
      [99  1 66]
      [96 88 17]
      [97 16 63]
      [20 60 39]
      [33 65 95]
      [21 45 25]
      [55  8 38]
      [35 91 73]
      [15  3 77]]
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#split data with pandas:
#suppose we have a csv containing 100 data
#transfer the data into DataFrame:
data = pd.read_csv(...)
#create a ndarray that contains all index:
data_idx = np.arange(data.shape[0])
#find the number of train data using 75% as train data:
num_training = int(np.floor(0.75 * data.shape[0])) #np.floor will return the max number that is not larger than target
#based on the num_training, randomly choose index:
data_train_idx = np.random.choice(data_idx, size=num_training, replace=False)
data_test_idx = np.delete(data_idx, data_train_idx)
#pd.iloc[idx] will return element at idx: 
data_train = data.iloc[data_train_idx]
data_test = data.iloc[data_test_idx]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#use np.random.shuffle to split data:
data_idx = np.arange(data.shape[0])
np.random.shuffle(data_idx)
data.index = data_idx
num_training = int(np.floor(0.75 * data.shape[0]))
data_train = data.iloc[:num_training]
data_test = data.iloc[num_training:]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#random seed (random_state)
#random.seed() is a number (or vector) used to initialize a pseudorandom number generator.
#generate the deterministic random data 
np.random.seed(2)
