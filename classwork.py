import pandas as pd
s=pd.Series([250, 300, 150, 400, 350],index=["mon","tue","wed","thu","fri"])
print(s)
print(s["wed"])
print(s.sum())


df=pd.DataFrame({"day":["mon","tue","wed","thu","fri"],"sales":[250,300,150,400,350]})
print(df)
print(max(df["sales"]))
print(min(df["sales"]))