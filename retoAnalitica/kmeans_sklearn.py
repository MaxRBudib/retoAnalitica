# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("../data/ulabox_orders_with_categories_partials_2017.csv")

dfp = df[['Food%', 'Fresh%', 'Drinks%', 'Home%', 'Beauty%', 'Health%', 'Baby%', 'Pets%']]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")

kmeans = KMeans(n_clusters=k).fit(dfp)
#sns.scatterplot(data=dfp, x="total_items", y="Food%", hue=kmeans.labels_)
#plt.show()
# %%
for i in range(k):
    cluster = dfp[kmeans.labels_ == i]
    df_percent = pd.melt(cluster)
    sns.boxplot(data=df_percent,x="variable", y="value" )
    plt.show()


# %%
