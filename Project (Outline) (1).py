#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In our outline each country is plotted using its yield (measured in kg/km)
#graphed against its NUE (measured as a percentage) with land used farming for each crop (measured in hectares) 
#corresponding to the size of the bubbles. Each crop can be viewed with its NUE for each country, 
#the amount grown, and the amount of land used in the process.
import scipy.io
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sb
import matplotlib.animation as ani
from matplotlib.animation import FuncAnimation
iFarmData = scipy.io.loadmat('iFarmData(2015)_1_28_2019.mat')
from IPython import display
import numpy as np


# In[20]:


country = input("Please enter a name of a country: ")
country2 = input("Please enter the name a second country: ")
crop = input("Please enter the name of a crop: ")


# In[21]:


Years = pd.DataFrame(iFarmData['Yr']).T
Countries = pd.DataFrame(iFarmData['FAOSTAT_CoName_FAO'])
CropNames = pd.DataFrame(iFarmData['FAOSTAT_CrName_FAO'])
#while count < int(numCountries):
#    countryList.append(input("Please input the name of a country: "))
#    count = count + 1

userCountry = Countries[Countries[0] == country].index[0]
userCountry2 = Countries[Countries[0] == country2].index[0]
userCrop = CropNames[CropNames[0] == crop].index[0]
get_ipython().run_line_magic('matplotlib', 'qt')


# In[26]:


xlimit = max(iFarmData['Yield_FAO'][userCountry][userCrop].max() + iFarmData['Yield_FAO'][userCountry][userCrop].max()*0.1, iFarmData['Yield_FAO'][userCountry2][userCrop].max() + iFarmData['Yield_FAO'][userCountry2][userCrop].max()*0.1)
areaMax = iFarmData['AreaH_FAO'][userCountry][userCrop].max()
Area = iFarmData['AreaH_FAO']
Yield = iFarmData['Yield_FAO']
NUE = iFarmData['NUE_3d']

fig = plt.figure()
fig.set_size_inches(25, 8)
plt.xlim(0, xlimit)
plt.ylim(0, 1)
plt.autoscale(False)

x,y,s, x2, y2, s2, x1, y1 = [], [], [], [], [], [], [], []
trendX, trendY, trendX2, trendY2 = [], [], [], []
dataX, dataY, dataX2, dataY2 = [], [], [], []
x1.append(0)
x1.append(max(iFarmData['Yield_FAO'][userCountry][userCrop].max() + iFarmData['Yield_FAO'][userCountry][userCrop].max()*0.1, iFarmData['Yield_FAO'][userCountry2][userCrop].max() + iFarmData['Yield_FAO'][userCountry2][userCrop].max()*0.1))
y1.append(0.7)
y1.append(0.7)

ColorList = []
color = np.random.rand(3,)
legend = ["Target NUE", country + ", " + crop + ": Trendline", country2 + ", " + crop + ": Trendline", country + ", " + crop, country2 + ", " + crop]

plt.plot(x1, y1, 'k:')
plt.text(max(iFarmData['Yield_FAO'][userCountry][userCrop].max() + iFarmData['Yield_FAO'][userCountry][userCrop].max()*0.1, iFarmData['Yield_FAO'][userCountry2][userCrop].max() + iFarmData['Yield_FAO'][userCountry2][userCrop].max()*0.1)*0.01, 0.71, "Target NUE")

i = 0
while i <= 54:
    dataX.append(Yield[userCountry][userCrop][i])
    dataY.append(NUE[userCountry][userCrop][i])
    dataX2.append(Yield[userCountry2][userCrop][i])
    dataY2.append(NUE[userCountry2][userCrop][i])
    i = i + 9
    
#ax = fig.add_subplot(1,1,1)
#plotlim = plt.xlim() + plt.ylim()  
#ax.imshow([[0,0],[1,1]], cmap=plt.cm.Greens, interpolation='bicubic', extent=plotlim)  
#plt.draw()  

def animate(frame):
    x.append(Yield[userCountry][userCrop][frame])
    y.append(NUE[userCountry][userCrop][frame])
    s.append(Area[userCountry][userCrop][frame]/(areaMax)*250)
    x2.append(Yield[userCountry2][userCrop][frame])
    y2.append(NUE[userCountry2][userCrop][frame])
    s2.append(Area[userCountry2][userCrop][frame]/(areaMax)*250)
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.title("Crop Yield, Nitrogen Use Efficiency, Land Used for Crop Growth (Shown by Bubble Size) | From 1960-2015")
    plt.xlabel("Crop Yield in kg/km")
    plt.ylabel("Nitrogen Use Efficiency (NUE)")
    plt.scatter(x, y, s, alpha=0.20, c='r')
    plt.scatter(x2, y2, s2, alpha=0.20, c='b')
    plt.legend(legend)

anim = FuncAnimation(fig, animate, frames=60, interval=200)
plt.plot(dataX, dataY, c='yellow')
plt.plot(dataX2, dataY2, c='tab:green')
#anim.save(r'C:\Users\joshu\Desktop\Top3IndiaAlt.gif', dpi=275


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




