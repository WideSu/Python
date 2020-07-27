#find outlier using seaborn boxplot:
import seaborn as sns
dt=np.concatenate([np.random.normal(0,1,1000),np.random.normal(8,1,10)])
sns.distplot(dt)
  #-> image.1
sns.boxplot(dt)
  #-> image.2
sns.boxplot(dt,orient='v') #orient='v' indicates the direction of graph
  #-> image.3
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#remove outlier using IQR (interquartile range):
def iqr_outlier_rm(data):
  lq,uq=np.percentile(data,[25,75]) #np.percentile directly return two values
  lower_l=lq - 1.5*(uq-lq)
  upper_l=uq + 1.5*(uq-lq)
  return data[(data >=lower_l)&(data<=upper_l)] #masking
  
dt_ws=iqr_outlier_rm(dt)
sns.boxplot(dt_outlier_ws,orient='v')
  #-> image.4
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
