d = pd.DataFrame({'col1': [1,2,3,4,5,6],'col2': ['1', '2', '3', '4', '5', '6'], 'col3': ['1','2','3',4,5,6]})
#indexing by column name:
df1 = d['col1'] #choose one column with series type
print(df1)
  '''
  ->0    1 #no column name at top
    1    2
    2    3
    3    4
    4    5
    5    6 
    Name: col1, dtype: int64
  '''
print(type(df1))
  #->class 'pandas.core.series.Series'
  
df2 = d[['col1']] #choose one colum with dataframe type
print(df2)
  '''
  ->    col1
    0     1
    1     2
    2     3
    3     4
    4     5
    5     6
  '''
print(type(df2))
  #->class 'pandas.core.frame.DataFrame'
#[] and [[]] will result in different type

df3 = d[['col1','col2']] #choose two columns
print(df3)
  '''
  ->   col1 col2
   0     1    1
   1     2    2
   2     3    3
   3     4    4
   4     5    5
   5     6    6
  '''
print(type(df3))
  #->class 'pandas.core.frame.DataFrame'

df4 = d[0:1][['col1','col2']] #choose first row's two columns
print(df4)
  '''
  ->   col1 col2
   0     1    1
  '''
print(type(df4))
  #->class 'pandas.core.frame.DataFrame'
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#select by position, using iloc:
#select one specific row:
d.iloc[1]
  '''
  ->col1    2
    col2    2
    col3    2
    Name: 1, dtype: object
    #<class 'pandas.core.series.Series'>
  '''
d.iloc[[1]]
  '''
  ->   col1 col2 col3
   1     2    2    2
    #<class 'pandas.core.frame.DataFrame'>
  '''

#select one specifc column:
d.iloc[:,1]
  '''
  ->0    1
    1    2
    2    3
    3    4
    4    5
    5    6
    Name: col2, dtype: object
    #<class 'pandas.core.series.Series'>
  '''

#select row and column:
d.iloc[0:2,0:1] #first two rows and first column
  '''
  ->   col1
    0     1
    1     2
    #<class 'pandas.core.frame.DataFrame'>
  '''

#select non consecutive row and columns:
d.iloc[[0,2,3],[1]]
  '''
  ->  col2
    0    1
    2    3
    3    4
    #<class 'pandas.core.frame.DataFrame'>
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#select by label, using loc:
#difference between iloc and loc is that iloc only support number and the endpoint is not included (just like index in array), but loc can support number and label and the endpoint is included.
#loc is especially useful when only know columns' names
df1 = d.loc[:,'col1'] #all rows' column 1
  '''
  ->0    1
    1    2
    2    3
    3    4
    4    5
    5    6
    Name: col1, dtype: int64
  '''
df2 = d.loc[0:2,'col1':'col2'] #first three rows!!!!! and column1 to col2 (included)
  '''
  ->   col1 col2
    0     1    1
    1     2    2
    2     3    3
  '''
df3 = d.loc[0:2,['col1','col2']] #first three rows and col1 and col2
  '''
  ->   col1 col2
    0     1    1
    1     2    2
    2     3    3
  '''
df4 = d.loc[[0,2],['col1','col2']] #first and third rows and col1 and col2
  '''
  ->   col1 col2
    0     1    1
    2     3    3
  '''
df5 = d.loc[[0,2],'col1':'col2'] #first and third rows, and col1 to col2
  '''
  ->   col1 col2
    0     1    1
    2     3    3
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#boolean indexing:
df1 = d[d['col1']>1]
print(df1)
  '''
  ->   col1 col2 col3
    1     2    2    2
    2     3    3    3
    3     4    4    4
    4     5    5    5
    5     6    6    6
    #the index does not change, it is still what it is before
  '''
df2 = d[(d['col1']>1)&(d['col2'>2])]
print(df2)
  '''
  ->TypeError: '>' not supported between instances of 'str' and 'int' 
    #because the col2 contains string elements not int. 
    #if col2 contains all int, this could work.
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#reset index:
df1 = d[d['col1']>1]
print(df1)
  '''
  ->   col1 col2 col3
    1     2    2    2
    2     3    3    3
    3     4    4    4
    4     5    5    5
    5     6    6    6
  '''
df1 = df1.reset_index(drop=True)
print(df1)
  '''
  ->   col1 col2 col3
    0     2    2    2
    1     3    3    3
    2     4    4    4
    3     5    5    5
    4     6    6    6
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
