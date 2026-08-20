import pandas as pd
fort=({ "name":["asha","ravi","kiran","meera","vikram"],
        "gender":["F","M","M","F","M"],
        "age":[24,27,"NaN",26,32,],
        "department":["it","hr","finance","hr","it"] })
df=pd.DataFrame(fort)
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.columns)
print(df.shape)
print(df.dtypes)
print(df.isnull())
print(df.isnull().sum())
print(df.columns.tolist())
df['gender']=df['gender'].astype('category')
df['department']=df['department'].astype('category')
print(df)
print(df.dtypes)
