import numpy as np
import matplotlib.pyplot as plt
import csv
data = np.genfromtxt('RHS-2019-Comparative-Statements-2019-Statement-1.csv',delimiter=',', dtype = float)

a = [row[2] for row in data]
b = [row[3] for row in data]
c = [row[4] for row in data]

datafile = open('RHS-2019-Comparative-Statements-2019-Statement-1.csv', 'r')
myreader = csv.reader(datafile)
k=[]
p=[]
for row in myreader:
  k.append(row[1])
for i in range(1,len(k)-1):
  p.append(k[i])

l=len(a)
abar=[]
bbar=[]
cbar=[]
for i in range(1,l-1):
  abar.append(a[i])
  bbar.append(b[i])
  cbar.append(c[i])

m=[]
h=[]
for i in range(10):
  m.append(abar[i])
  h.append(p[i])


fig = plt.figure(figsize =(100, 20)) 
plt.bar(h, m, color ='maroon',width=0.4)
plt.title("RHS 2019 comaparative statements")
plt.savefig("barplot.png")
plt.show()

