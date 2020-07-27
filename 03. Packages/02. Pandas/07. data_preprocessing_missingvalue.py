#why care about missing value:
  #information loss
  #wrong prediction
  #sklearn does not support data with missing value
#in pandas, Nah means missing value
#how to deal with it:
  #delete row or column
  #use meadian, mean or mode to represent missing value
  #use a predictive modle to predict what the missing value may be
  #KNN
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create a dataframe using np.nan:
data = {'name': ['A', np.nan, 'C', 'D', 'E', 'F'], 
        'age': [27, np.nan, 11, 12, 54, 16], 
        'gender': ['m', np.nan, 'm', np.nan, 'f', 'f'], 
        'Score1': [10, np.nan, np.nan, 25, 33, 99],
        'Score2': [22, np.nan, np.nan, 42, 20, 78]}
df = pd.DataFrame(data, columns = ['name', 'age', 'gender', 'Score1', 'Score2'])
print(df)
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1  NaN   NaN    NaN     NaN     NaN
    2    C  11.0      m     NaN     NaN
    3    D  12.0    NaN    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#detect missing value:
df.info()
  '''
  -><class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 5 columns):
    name      5 non-null object
    age       5 non-null float64
    gender    4 non-null object
    Score1    4 non-null float64
    Score2    4 non-null float64
    dtypes: float64(3), object(2)
    memory usage: 368.0+ bytes
    #index is 0 to 5 so totally 6 rows, but no column has data more than 5, so missing value exists.
  '''
df.isnull()
  '''
  ->    name    age  gender  Score1  Score2
    0  False  False   False   False   False
    1   True   True    True    True    True
    2  False  False   False    True    True
    3  False  False    True   False   False
    4  False  False   False   False   False
    5  False  False   False   False   False
  '''
df.isnull().sum() #find the number of null in reach column
  '''
  ->name      1
    age       1
    gender    2
    Score1    2
    Score2    2
    dtype: int64
  '''
df.notnull().sum()
  '''
  ->name      5
    age       5
    gender    4 
    Score1    4
    Score2    4
    dtype: int64
  '''
df.isnull().all(axis=1) #check if the row is full of null, axis=1 is for row, axis=0 is column
  '''
  ->0    False
    1     True
    2    False
    3    False
    4    False
    5    False
    dtype: bool
  '''
df.isnull().any(axis=1) #check if there is null in each row
  '''
  ->0    False
    1     True
    2     True
    3     True
    4    False
    5    False
    dtype: bool
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#elimination:
#drop accoding to have nah or not
df.dropna(axis=0,how='all',inplace=True) #this will directly rewrite the original data
df1=df.dropna(axis=0,how='all') #0 for row, 1 for column
df1.reset_index(inplace=True)
print(df1)
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1    C  11.0      m     NaN     NaN
    2    D  12.0    NaN    25.0    42.0
    3    E  54.0      f    33.0    20.0
    4    F  16.0      f    99.0    78.0
  '''

#drop accoding to how much value you want
df2=df.dropna(thresh=4) #drop the row that has less than 4 actual value.
print(df2)
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    3    D  12.0    NaN    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#imputation:
#fill nah with some number
df3=df.fillna(0) #fill all nah with 0
print(df3)
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1    0   0.0      0     0.0     0.0
    2    C  11.0      m     0.0     0.0
    3    D  12.0      0    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''

#fill with number in original data
df.gender.fillna(method='ffill',inplace=True) #fill the nah in column 'gender' with the number before it
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1  NaN   NaN      m     NaN     NaN
    2    C  11.0      m     NaN     NaN
    3    D  12.0      m    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''
df.gender.fillna(method='bfill',inplace=True) #fill the nah in column 'gender' with the number after it
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1  NaN   NaN      m     NaN     NaN
    2    C  11.0      m     NaN     NaN
    3    D  12.0      f    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''
df.fillna(method='bfill',inplace=True) #fill all nah in every column with the number after it
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1    C  11.0      m    25.0    42.0
    2    C  11.0      m    25.0    42.0
    3    D  12.0      f    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''

#fill with statistical number
df.Score1.fillna(df['Score1'].mean(),inplace=True)
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m   10.00    22.0
    1  NaN   NaN    NaN   41.75     NaN
    2    C  11.0      m   41.75     NaN
    3    D  12.0    NaN   25.00    42.0
    4    E  54.0      f   33.00    20.0
    5    F  16.0      f   99.00    78.0 
  '''
df['Score1'].fillna(df['Score1'].mean(),inplace=True) #same with first one
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m   10.00    22.0
    1  NaN   NaN    NaN   41.75     NaN
    2    C  11.0      m   41.75     NaN
    3    D  12.0    NaN   25.00    42.0
    4    E  54.0      f   33.00    20.0
    5    F  16.0      f   99.00    78.0
  '''
df.Score1.fillna(df['Score1'].median(),inplace=True) #fill with median
  '''
  ->  name   age gender  Score1  Score2
    0    A  27.0      m    10.0    22.0
    1  NaN   NaN    NaN    29.0     NaN
    2    C  11.0      m    29.0     NaN
    3    D  12.0    NaN    25.0    42.0
    4    E  54.0      f    33.0    20.0
    5    F  16.0      f    99.0    78.0
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
