#%%
import pandas as pd
import numpy as np 
import seaborn as sns
from sklearn.cluster import KMeans
# %%
df = pd.read_csv("../data/ulabox_orders_with_categories_partials_2017.csv")
df.tail()
#%%
#La cantidad total de productos
sns.histplot(data=df, x = "total_items")
#podemos ver que la mayor cantidad de compras fue entre 0 y 50 total_items
#%%
df_percent = df[['Food%', 'Fresh%', 'Drinks%', 'Home%', 'Beauty%', 'Health%', 'Baby%', 'Pets%']].div(df['total_items'], axis=0)
sns.heatmap(df_percent.corr(), annot=True)
#ninguna correlación entre porcentajes
#%%
sns.histplot(data=df, x='hour', hue='weekday', multiple='stack')
#analisis de horas
#%%
sns.violinplot(data=df_percent)
#La mayorìa de las compras fueron variadas, mientras que menos fueron totalmente de una categoría

# %%
#Compras por día
sns.displot(x = 'weekday', data = df)
#Hay más compras en el día 1, y disminuyen hasta el día 6, para
#aumentar de nuevo el día 7
# %%
#Compras por hora
sns.displot(x = 'hour', data = df)
#La mayoría de las compras se hacen a medio día y después de las 10
# %%
