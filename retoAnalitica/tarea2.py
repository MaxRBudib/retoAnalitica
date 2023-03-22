#%%
import pandas as pd
import numpy as np 
import seaborn as sns
# %%
df = pd.read_csv("/workspace/retoAnalitica/data/ulabox_orders_with_categories_partials_2017.csv")
df.tail()
# %%
df.describe()
# %%
df.sample()
# %%
#Categorica y numerica
#continua y discreta 
#ordinal y nominal 