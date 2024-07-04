#그룹별 연산하기

import seaborn as sns
from IPython.display import display
import pandas as pd
import numpy as np


df=sns.load_dataset('penguins')
print(df.head())
print()
print()

df_group=df.groupby(['species'])
print(df_group)
print()
print()

print(df_group.head(2))
print()
print()


#그룹의 칼럼별 평균

print(df_group[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean())
print()
print()

print(df.groupby(['species', 'sex'])[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].mean())
print()
print()


def min_max(x):
    return x.max() - x.min()

print(df.groupby(['species'])['bill_length_mm'].agg(min_max))
print()
print()


print(df.groupby(['species'])[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].agg(['max', 'min']))
print()
print()


print(df.groupby(['species']).agg({'bill_length_mm': ['max', 'min'], 'island': ['count']}))
print()
print()


print(df.groupby(['species'])['bill_length_mm'].transform('mean'))
print()
print()


def z_score(x):
    z = (x - x.mean()) / x.std()
    return(z)


print(df.groupby(['species'])['bill_length_mm'].transform(z_score))
print()
print()


print(df.groupby(['species'])['bill_length_mm'].apply(min))
print()
print()


print(df.groupby(['species'])['bill_length_mm'].apply(z_score))
print()
print()


print(df.groupby(['species'])['bill_length_mm'].mean())
print()
print()


print(df.groupby(['species']).filter(lambda x: x['bill_length_mm'].mean() >= 40))
print()
print()




