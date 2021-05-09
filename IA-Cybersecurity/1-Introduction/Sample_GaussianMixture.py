#!/usr/bin/env python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture


data_df = pd.read_csv("clustering.csv")
data_df.describe()
X_data = data_df.drop("class_1", axis=1)
y_data = data_df["class_1"]

pca = PCA(n_components=2)
pca.fit(X_data)
X_2D = pca.transform(X_data)
data_df['PCA1'] = X_2D[:, 0]
data_df['PCA2'] = X_2D[:, 1]

gm = GaussianMixture(n_components=3, covariance_type='full')
gm.fit(X_data)
y_gm = gm.predict(X_data)
data_df['cluster'] = y_gm
sns.lmplot('PCA1', 'PCA2', data=data_df, col="cluster", fit_reg=False)
plt.show()
