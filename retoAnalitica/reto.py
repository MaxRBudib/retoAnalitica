#%%
import pandas as pd
import numpy as np 
import seaborn as sns
# %%
df = pd.read_csv("../data/ulabox_orders_with_categories_partials_2017.csv")
df.tail()

# %%
#Descuento contra total de items.
sns.scatterplot(data=df1, x="discount%", y="total_items")
#No parece que haya una relacion importante
# %%
