#merge:
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],'B': ['B0', 'B1', 'B2', 'B3'],'C': ['C0', 'C1', 'C2', 'C3'],'D': ['D0', 'D1', 'D2', 'D3']})
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],'B': ['B4', 'B5', 'B6', 'B7'],'C': ['C4', 'C5', 'C6', 'C7'],'D': ['D4', 'D5', 'D6', 'D7']})
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],'B': ['B8', 'B9', 'B10', 'B11'],'C': ['C8', 'C9', 'C10', 'C11'],'D': ['D8', 'D9', 'D10', 'D11']})
df4 = pd.concat([df1,df2,df3])
print(df4)
  '''
  ->     A    B    C    D
    0   A0   B0   C0   D0
    1   A1   B1   C1   D1
    2   A2   B2   C2   D2
    3   A3   B3   C3   D3
    0   A4   B4   C4   D4
    1   A5   B5   C5   D5
    2   A6   B6   C6   D6
    3   A7   B7   C7   D7
    0   A8   B8   C8   D8
    1   A9   B9   C9   D9
    2  A10  B10  C10  D10
    3  A11  B11  C11  D11
    #by default, index will not be reseted.
  '''
df5 = pd.concat([df1,df2,df3],ignore_index = True)
print(df5)
  '''
  ->      A    B    C    D
    0    A0   B0   C0   D0
    1    A1   B1   C1   D1
    2    A2   B2   C2   D2
    3    A3   B3   C3   D3
    4    A4   B4   C4   D4
    5    A5   B5   C5   D5
    6    A6   B6   C6   D6
    7    A7   B7   C7   D7
    8    A8   B8   C8   D8
    9    A9   B9   C9   D9
    10  A10  B10  C10  D10
    11  A11  B11  C11  D11
    #when ignore_index = True, will reset index, and default is False.
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#join (same with sql):
#four types of join: inner(default), outer, left, right
#inner join: connect when both sides have data
#outer join: connect all sides (like union)
#left join: left table's data as base and use right side data to match left side
#right join: use left table to match right table
#example (inner join):
df_right = pd.DataFrame({'year':np.arange(1980,1990),'rain_cn':np.arange(800,810)})
df_left = pd.DataFrame({'water_year':np.arange(1975,1995),'rain':np.arange(900,920),'outflow':np.arange(200,220)})
join_df = pd.merge(df_left,df_right,left_on='water_year',right_on='year',how='inner')
print(join_df)
  '''
  ->   water_year  rain  outflow  year  rain_cn
    0        1980   905      205  1980      800
    1        1981   906      206  1981      801
    2        1982   907      207  1982      802
    3        1983   908      208  1983      803
    4        1984   909      209  1984      804
    5        1985   910      210  1985      805
    6        1986   911      211  1986      806
    7        1987   912      212  1987      807
    8        1988   913      213  1988      808
    9        1989   914      214  1989      809
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#group by:
#split data according to some criteria
df = pd.DataFrame({})
df = pd.DataFrame({'race':['A','A','C','B','A','B','A','C'],'age':[11,54,67,25,29,44,9,20]})
df.groupby('race')['age'].mean() #this means, we split based on race, and for each group, find the mean of column 'age'
print(df.groupby('race')['age'].mean())
  '''
  ->race
    A    25.75
    B    34.50
    C    43.50
    Name: age, dtype: float64
  '''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
