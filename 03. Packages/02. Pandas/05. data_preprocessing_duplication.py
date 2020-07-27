df = pd.DataFrame({'col1':['A','A','C','B','A','B','A','C'],'col2':[11,54,67,25,29,44,9,20],'col3':[1,8,2,4,6,7,9,9]})
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#check if a col has duplication:
np.where(df['col1'].duplicated()) #this will return the index that duplicates occurs
  #-> (array([1, 4, 5, 6, 7]),)
print(df.iloc[np.where(df['col1'].duplicated())]) #with duplicates
  '''
  ->  col1  col2  col3
    1    A    54     8
    4    A    29     6
    5    B    44     7
    6    A     9     9
    7    C    20     9
  '''
print(df.iloc[np.where(df['col2'].duplicated())]) #with no duplicates
  '''
  ->Empty DataFrame
    Columns: [col1, col2, col3]
    Index: []
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create duplicate row:
df1 = df
df1.loc[len(df1)] = df1.iloc[0]
print(df1.iloc[[0,-1]])
  '''
  ->  col1  col2  col3
    0    A    11     1
    8    A    11     1
  '''
print(df1.iloc[np.where(df1[['col1','col2','col3']].duplicated())])
  '''
  ->  col1  col2  col3
    8    A    11     1
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#check duplicate row (exact same row):
print(df[df.duplicated()])
  '''
  ->Empty DataFrame
    Columns: [col1, col2, col3]
    Index: []
  '''
df1 = df
df1.loc[len(df1)] = df1.iloc[0]
print(df1[df1.duplicated()])
  '''
  ->  col1  col2  col3
    8    A    11     1
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#remove duplicate:
df2 = df1.drop_duplicates() #this function does not operate on the data, so that we need to point the function to a new variable
print(df2.iloc[[0,-1]])
  '''
  ->  col1  col2  col3
    0    A    11     1
    7    C    20     9
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
