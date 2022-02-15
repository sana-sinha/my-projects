from sklearn.cluster import KMeans
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
import numpy as np  

def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    points = []
    for j in range(len(X)):
      if clusters[j] == i:
        points.append(X[j])
    points = np.array(points)
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
  plt.savefig("clustered_graph.png")
  
data = pd.read_csv("disney.csv")
print(data.describe())

dates = data["release_date"]
years = []

for date in dates:
  newDates = date.split("-")
  years.append(int(newDates[0]))

print(years)

inflation = data["inflation_adjusted_gross"]

plt.scatter(years, inflation)
plt.savefig("before_clustering.png")
plt.clf()

k = 3

dataPoints = list(zip(years, inflation))

km = KMeans(n_clusters=k, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)

clusters = km.fit_predict(dataPoints)
centroids = km.fit(dataPoints).cluster_centers_

draw_clustered_graph(k, dataPoints, clusters, centroids)
