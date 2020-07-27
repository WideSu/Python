#suppose we have a data on a website
#load:
url = 'https://.........../data.csv'
df_data = pd.read_csv(url, sep=',')
#save to local:
df_data.to_csv('name.csv',index = False)
