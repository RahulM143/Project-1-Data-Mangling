import pandas as pd 
import numpy as np 

df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv') 
df.head(2)
df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv') 
df1.head(2)

"""1. Get the Metadata from the above files"""
df.info()
df1.info()

""" 2. Get the row names from the above files"""
row_names1 = df.index.values
row_names1
row_names2 =df1.index.values
row_names2

"""3. Change the column name from any of the above file. """
df = df.rename (columns = {'Indicator' :'Indicator_id'})
df.head()

""" 4. Change the column name from any of the above file and store the changes made
permanently."""
df1 = df1.rename (columns = {'STATION' :'STATION_ID'})
df1.head()
df1.columns

"""5. Change the names of multiple columns."""
df.columns
df = df.rename (columns = {'PUBLISH STATES' :'Publication Status','WHO region':'WHO Region' })
df.columns

"""6. Arrange values of a particular column in ascending order."""
dfsort = df.sort (columns = 'Year', axis = 0, ascending = True, kind = 'quicksort')
dfsort.head(15)

"""7. Arrange multiple column values in ascending order. """
dfsort1 = df[['Indicator_id', 'Country','Year','WHO Region','Publication Status']] 
dfsort1.sort(ascending = True)

"""8. Make country as the first column of the dataframe."""
cols = df.columns.tolist()
cols
cols = cols[5:6] + cols [:5] + cols[6:]
cols
df2 = df
df2 = df2[cols]
df2.head()

"""9.Get the column array using a variable"""
col_values = df['WHO Region'].values
col_values

""" 10. Get the subset rows 11, 24, 37 """
df.head()
kf = df.iloc [[11,24,37],  ]
kf.head()
""" 11.Get the subset rows excluding 5, 12, 23, and 56 """
jf = df.drop (df.index[[5,12,23,56]])
jf.head(60)

"""Load datasets from CSV"""
users = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv' )
sessions =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv' ) 
products =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv' )
transactions =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv') 
users.head() 
products.head()
sessions.head() 
transactions.head() 

"""12. Join users to transactions, keeping all rows from transactions and only matching rows
from users (left join)"""
tran_users = pd.merge (transactions, users , on ='UserID', how = 'left')
tran_users

"""13. Which transactions have a UserID not in users? """
gf = tran_users.Gender.isnull() 
gt = tran_users[gf] 
gt

"""14. Join users to transactions, keeping only rows from transactions and users that match
via UserID (inner join) """

gf1 = pd.merge (transactions, users , on ='UserID', how = 'inner')
gf1

"""15. Join users to transactions, displaying all matching rows AND all non-matching rows
(full outer join)"""

gf2 = pd.merge (transactions, users , on ='UserID', how = 'outer')
gf2

"""16. Determine which sessions occurred on the same day each user registered """
sess = pd.merge (users,sessions, on ='UserID', how = 'inner')
date = sess.SessionDate == sess.Registered
sess[date]

"""17. Build a dataset with every possible (UserID, ProductID) pair (cross join)"""
uv = pd.DataFrame (users.UserID.values, columns = ['UserID'] )
uv ['Key'] = 0
prodVals = products
pv = pd.DataFrame (products.ProductID.values, columns = ['ProductID'] )
pv['Key'] = 0
dset = pd.merge(uv,pv, on = 'Key').drop ('Key',axis = 1)
dset

"""18. Determine how much quantity of each product was purchased by each user"""
pf = pd.merge (dset ,transactions, how = 'left', left_on = ['UserID', 'ProductID'], right_on= ['UserID', 'ProductID'] )
pf

"""19. For each user, get each possible pair of pair transactions (TransactionID1,
TransacationID2) """

pd.merge(transactions, transactions, on='UserID')

"""20. Join each user to his/her first occuring transaction in the transactions table"""
pd.merge(users, transactions.groupby('UserID').first().reset_index(), how='left', on='UserID')

"""21. Test to see if we can drop columns"""
data = pd.merge (users,transactions, how = 'left')
my_columns = list(data.columns)
my_columns
data.drop ('Cancelled', axis = 1)

"""set threshold to drop NAs"""
list(data.dropna(thresh=int(data.shape[0] * .9), axis=1).columns)

"""missing info"""
missing_info = list(data.columns[data.isnull().any()]) 
missing_info

for col in missing_info:
    num_missing = data[data[col].isnull() == True].shape[0] 
    print('number missing for column {}: {} number'.format(col, num_missing)) 

"""count of missing data"""
for col in missing_info:
    percent_missing = data[data[col].isnull() == True].shape[0] / data.shape[0]
    print('percent missing for column {}: {}'.format(col, np.round (percent_missing,1)))






















