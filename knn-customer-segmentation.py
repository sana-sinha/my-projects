from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# Draws a scatterplot 
def draw_clustered_graph(k, X, clusters, centroids):
  colors = ['r', 'g', 'b', 'y', 'c', 'm']
  fig, ax = plt.subplots()
  for i in range(k):
    xpoints = []
    ypoints = []
    for j in range(len(X)):
      if clusters[j] == i:
        xpoints.append(X[j][0])
        ypoints.append(X[j][1])
    ax.scatter(xpoints, ypoints, s=7, c=colors[i])
  xpoints = []
  ypoints = []
  for c in centroids:
    xpoints.append(c[0])
    ypoints.append(c[1])
  ax.scatter(xpoints, ypoints, marker='*', s=200, c='#050505')
  plt.savefig("clustered_graph.png")

# reads in data from Mall_Customers
dataFrame = pd.read_csv('Mall_Customers.csv')
print(dataFrame.describe()) # .describe() returns summary of all columns in .csv

annualIncome = dataFrame["Annual Income"]
spendingScore = dataFrame["Spending Score"]

# graph 
plt.scatter(annualIncome, spendingScore)
plt.savefig("Before Clustering.png")
plt.clf()

k = 2

# list of data points in graph 
dataPoints = list(zip(annualIncome, spendingScore))
print()
print(dataPoints)

centroids = []

for i in range(k):
  randomIndex = random.randint(0, len(annualIncome)-1)
  x = dataPoints[randomIndex][0]
  y = dataPoints[randomIndex][1]
  
  centroids.append((x, y))
  print(centroids)

oldCentroids = []

for i in range(k):
  oldCentroids.append((0, 0))

# what cluster is set for data point 
clusters = [0]*len(dataPoints)

# euclidean
def distance(pointA, pointB):
  return ((pointB[1] - pointA[1])**2 + (pointB[0] - pointA[0])**2)**0.5

print(distance((2, 3), (3, 5)))

def findCentroid(pointsList):
  xSum = 0 
  ySum = 0
  for points in pointsList:
    xSum += points[0]
    ySum += points[1]
  xAverage = xSum/len(pointsList)
  yAverage = ySum/len(pointsList)
  
  return (xAverage, yAverage)

# assign shortest distance between data point and centroid to that cluster
while centroids != oldCentroids:
  for i in range(len(dataPoints)):
    minDistance = math.inf
    for j in range(len(centroids)):
      myDistance = distance(dataPoints[i], centroids[j])
      if myDistance < minDistance:
        minDistance = myDistance
        clusters[i] = j

  # deepcopy contructs a new object and recursively inserts copies of items in original object
  oldCentroids = deepcopy(centroids)

  for i in range(k):
    pointsList = []
    for j in range(len(dataPoints)):
      if clusters[j] == i:
        pointsList.append(dataPoints[j])
    centroids[i] = findCentroid(pointsList)

# k, X, clusters, centroids
draw_clustered_graph(k, dataPoints, clusters, centroids)

# k nearest neighbors
k2 = 4

# (annual income, spending score)
dataPt = (90, 20)

data = {} # stores data point and distance from unknown

for pt in dataPoints:
  myDistance = distance(pt, dataPt)
  if k2 > len(data):
    data[pt] = myDistance # to append to dictionary
  else:
    neighbor = (0, 0)
    maxDistance = 0
    for pt in data:
      if data[pt] > maxDistance:
        neighbor = pt
        maxDistance = data[pt]
    if maxDistance > myDistance:
      data.pop(neighbor)
      data[pt] = myDistance

neighbors = {}

for pt in data:
  index = dataPoints.index(pt)
  cluster = clusters[index]
  if cluster in neighbors:
    neighbors[cluster] += 1
  else:
    neighbors[cluster] = 1

print("Neighbors")
print(neighbors)

maxPoints = 0

for cluster in neighbors:
  if neighbors[cluster] > maxPoints:
    maxPoints = cluster

print(maxPoints)
