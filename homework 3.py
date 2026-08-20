import pandas as pd
frame=({"emp id":[101,102,103,104,105,106],
        "name":["arun","divya","john","meena","rahul","sara"],
        "company":["tcs","wipro","infosys","tcs","wipro","infosys"],
        "year":[2023,2024,2023,2024,2023,2024],
        "salary":[48000,45000,'NaN',52000,41000,56000],
        "role":["developer","tester","developer","HR","NaN","tester"]})
print(frame)
df=pd.DataFrame(frame)
print(df)
print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull())
print(df.isnull().sum())
df['company']=df['company'].astype('category')
df['role']=df['role'].astype('category')
far=pd.MultiIndex.from_frame(df[['company', 'year']], names=['company', 'year'])
df.set_index(far, inplace=True)
print(df)
df=pd.DataFrame(frame,index=["row 1","row 2","row 3","row 4","row 5","row 6"])
print(df)
print(df.head())