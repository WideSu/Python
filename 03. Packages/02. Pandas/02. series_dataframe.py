#Series is a one-dimensional labeled array capable of holding any data type. The axis labels are collectively referred to as the index.
#DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create serise from list:
a = pd.Series([1,3,5,6,8])
b = pd.Series(['a','b','c','d'])
print(type(a))
  #-> class 'pandas.core.series.Series'
print(a)
  '''
  -> 0    1
     1    3
     2    5
     3    6
     4    8
     dtype: int64
  '''
print(b)
  '''
  -> 0    a
     1    b
     2    c
     3    d
     dtype: object
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#create DataFrame:
d = pd.DataFrame({'col1': [1,2,3,4,5,6],'col2': ['1', '2', '3', '4', '5', '6'], 'col3': ['1','2','3',4,5,6]})
print(d)
  '''
  ->   col1 col2 col3
   0     1    1    1
   1     2    2    2
   2     3    3    3
   3     4    4    4
   4     5    5    5
   5     6    6    6
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#find data's information:
#basic information:
d.info()
  '''
  -> <class 'pandas.core.frame.DataFrame'>
     RangeIndex: 6 entries, 0 to 5
     Data columns (total 3 columns):
      #   Column  Non-Null Count  Dtype 
     ---  ------  --------------  ----- 
      0   col1    6 non-null      int64 
      1   col2    6 non-null      object
      2   col3    6 non-null      object
     dtypes: int64(1), object(2)
     memory usage: 272.0+ bytes
  '''
#first k row:
d.head(2) #first two rows, the first column is index
  '''
  ->    col1 col2 col3
    0     1    1    1
    1     2    2    2
  '''
#last k row:
d.tail(2) #last two rows
  '''
  ->    col1 col2 col3
    4     5    5    5
    5     6    6    6
  '''
#find data's statistical information:
d.describe()
  '''
  ->            col1
     count  6.000000
     mean   3.500000
     std    1.870829
     min    1.000000
     25%    2.250000
     50%    3.500000
     75%    4.750000
     max    6.000000
  '''
#find index information:
d.index
  #-> RangeIndex(start=0, stop=6, step=1)
#find column name and change names:
d.columns
  #-> Index(['col1', 'col2', 'col3'], dtype='object')
new_name = ['01','02','03']
d.columns = new_name
d.info()
  '''
  -> <class 'pandas.core.frame.DataFrame'>
      RangeIndex: 6 entries, 0 to 5
      Data columns (total 3 columns):
      01    6 non-null int64
      02    6 non-null object
      03    6 non-null object
      dtypes: int64(1), object(2)
      memory usage: 272.0+ bytes
  '''
new_name = ['01','02','03','04']
d.columns = new_name
  #-> ValueError: Length mismatch: Expected axis has 3 elements, new values have 4 elements
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
