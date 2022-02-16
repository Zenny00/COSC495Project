#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.io
from matplotlib import pyplot as plt
import pandas as pd
iFarmData = scipy.io.loadmat('iFarmData(2015)_1_28_2019.mat')


# In[2]:


Col0 = NUE_Colombia_GreenCoffee_2015 = ((iFarmData['Nyield_kgkm'][40, 41, 54])/(iFarmData['Nfer_kgkm'][40, 41, 54] + iFarmData['Nman_kgkm'][40, 41, 54] + iFarmData['Nfix_kgkm'][40, 41, 54] + iFarmData['Ndep_kgkm'][40, 41, 54]))
Col1 = NUE_Colombia_GreenCoffee_2010 = ((iFarmData['Nyield_kgkm'][40, 41, 49])/(iFarmData['Nfer_kgkm'][40, 41, 49] + iFarmData['Nman_kgkm'][40, 41, 49] + iFarmData['Nfix_kgkm'][40, 41, 49] + iFarmData['Ndep_kgkm'][40, 41, 49]))
Col2 = NUE_Colombia_GreenCoffee_2005 = ((iFarmData['Nyield_kgkm'][40, 41, 44])/(iFarmData['Nfer_kgkm'][40, 41, 44] + iFarmData['Nman_kgkm'][40, 41, 44] + iFarmData['Nfix_kgkm'][40, 41, 44] + iFarmData['Ndep_kgkm'][40, 41, 44]))
Col3 = NUE_Colombia_GreenCoffee_2000 = ((iFarmData['Nyield_kgkm'][40, 41, 39])/(iFarmData['Nfer_kgkm'][40, 41, 39] + iFarmData['Nman_kgkm'][40, 41, 39] + iFarmData['Nfix_kgkm'][40, 41, 39] + iFarmData['Ndep_kgkm'][40, 41, 39]))
Col4 = NUE_Colombia_GreenCoffee_1995 = ((iFarmData['Nyield_kgkm'][40, 41, 34])/(iFarmData['Nfer_kgkm'][40, 41, 34] + iFarmData['Nman_kgkm'][40, 41, 34] + iFarmData['Nfix_kgkm'][40, 41, 34] + iFarmData['Ndep_kgkm'][40, 41, 34]))
Col5 = NUE_Colombia_GreenCoffee_1990 = ((iFarmData['Nyield_kgkm'][40, 41, 29])/(iFarmData['Nfer_kgkm'][40, 41, 29] + iFarmData['Nman_kgkm'][40, 41, 29] + iFarmData['Nfix_kgkm'][40, 41, 29] + iFarmData['Ndep_kgkm'][40, 41, 29]))
Col6 = NUE_Colombia_GreenCoffee_1985 = ((iFarmData['Nyield_kgkm'][40, 41, 24])/(iFarmData['Nfer_kgkm'][40, 41, 24] + iFarmData['Nman_kgkm'][40, 41, 24] + iFarmData['Nfix_kgkm'][40, 41, 24] + iFarmData['Ndep_kgkm'][40, 41, 24]))
Col7 = NUE_Colombia_GreenCoffee_1980 = ((iFarmData['Nyield_kgkm'][40, 41, 19])/(iFarmData['Nfer_kgkm'][40, 41, 19] + iFarmData['Nman_kgkm'][40, 41, 19] + iFarmData['Nfix_kgkm'][40, 41, 19] + iFarmData['Ndep_kgkm'][40, 41, 19]))
Col8 = NUE_Colombia_GreenCoffee_1975 = ((iFarmData['Nyield_kgkm'][40, 41, 14])/(iFarmData['Nfer_kgkm'][40, 41, 14] + iFarmData['Nman_kgkm'][40, 41, 14] + iFarmData['Nfix_kgkm'][40, 41, 14] + iFarmData['Ndep_kgkm'][40, 41, 14]))
Col9 = NUE_Colombia_GreenCoffee_1970 = ((iFarmData['Nyield_kgkm'][40, 41, 9])/(iFarmData['Nfer_kgkm'][40, 41, 9] + iFarmData['Nman_kgkm'][40, 41, 9] + iFarmData['Nfix_kgkm'][40, 41, 9] + iFarmData['Ndep_kgkm'][40, 41, 9]))
Col10 = NUE_Colombia_GreenCoffee_1965 = ((iFarmData['Nyield_kgkm'][40, 41, 4])/(iFarmData['Nfer_kgkm'][40, 41, 4] + iFarmData['Nman_kgkm'][40, 41, 4] + iFarmData['Nfix_kgkm'][40, 41, 4] + iFarmData['Ndep_kgkm'][40, 41, 4]))
Col11 = NUE_Colombia_GreenCoffee_1960 = ((iFarmData['Nyield_kgkm'][40, 41, 0])/(iFarmData['Nfer_kgkm'][40, 41, 0] + iFarmData['Nman_kgkm'][40, 41, 0] + iFarmData['Nfix_kgkm'][40, 41, 0] + iFarmData['Ndep_kgkm'][40, 41, 0]))

US0 = ((iFarmData['Nyield_kgkm'][206, 41, 54])/(iFarmData['Nfer_kgkm'][206, 41, 54] + iFarmData['Nman_kgkm'][206, 41, 54] + iFarmData['Nfix_kgkm'][206, 41, 54] + iFarmData['Ndep_kgkm'][206, 41, 54]))
US1 = ((iFarmData['Nyield_kgkm'][206, 41, 49])/(iFarmData['Nfer_kgkm'][206, 41, 49] + iFarmData['Nman_kgkm'][206, 41, 49] + iFarmData['Nfix_kgkm'][206, 41, 49] + iFarmData['Ndep_kgkm'][206, 41, 49]))
US2 = ((iFarmData['Nyield_kgkm'][206, 41, 44])/(iFarmData['Nfer_kgkm'][206, 41, 44] + iFarmData['Nman_kgkm'][206, 41, 44] + iFarmData['Nfix_kgkm'][206, 41, 44] + iFarmData['Ndep_kgkm'][206, 41, 44]))
US3 = ((iFarmData['Nyield_kgkm'][206, 41, 39])/(iFarmData['Nfer_kgkm'][206, 41, 39] + iFarmData['Nman_kgkm'][206, 41, 39] + iFarmData['Nfix_kgkm'][206, 41, 39] + iFarmData['Ndep_kgkm'][206, 41, 39]))
US4 = ((iFarmData['Nyield_kgkm'][206, 41, 34])/(iFarmData['Nfer_kgkm'][206, 41, 34] + iFarmData['Nman_kgkm'][206, 41, 34] + iFarmData['Nfix_kgkm'][206, 41, 34] + iFarmData['Ndep_kgkm'][206, 41, 34]))
US5 = ((iFarmData['Nyield_kgkm'][206, 41, 29])/(iFarmData['Nfer_kgkm'][206, 41, 29] + iFarmData['Nman_kgkm'][206, 41, 29] + iFarmData['Nfix_kgkm'][206, 41, 29] + iFarmData['Ndep_kgkm'][206, 41, 29]))
US6 = ((iFarmData['Nyield_kgkm'][206, 41, 24])/(iFarmData['Nfer_kgkm'][206, 41, 24] + iFarmData['Nman_kgkm'][206, 41, 24] + iFarmData['Nfix_kgkm'][206, 41, 24] + iFarmData['Ndep_kgkm'][206, 41, 24]))
US7 = ((iFarmData['Nyield_kgkm'][206, 41, 19])/(iFarmData['Nfer_kgkm'][206, 41, 19] + iFarmData['Nman_kgkm'][206, 41, 19] + iFarmData['Nfix_kgkm'][206, 41, 19] + iFarmData['Ndep_kgkm'][206, 41, 19]))
US8 = ((iFarmData['Nyield_kgkm'][206, 41, 14])/(iFarmData['Nfer_kgkm'][206, 41, 14] + iFarmData['Nman_kgkm'][206, 41, 14] + iFarmData['Nfix_kgkm'][206, 41, 14] + iFarmData['Ndep_kgkm'][206, 41, 14]))
US9 = ((iFarmData['Nyield_kgkm'][206, 41, 9])/(iFarmData['Nfer_kgkm'][206, 41, 9] + iFarmData['Nman_kgkm'][206, 41, 9] + iFarmData['Nfix_kgkm'][206, 41, 9] + iFarmData['Ndep_kgkm'][206, 41, 9]))
US10 = ((iFarmData['Nyield_kgkm'][206, 41, 4])/(iFarmData['Nfer_kgkm'][206, 41, 4] + iFarmData['Nman_kgkm'][206, 41, 4] + iFarmData['Nfix_kgkm'][206, 41, 4] + iFarmData['Ndep_kgkm'][206, 41, 4]))
US11 = ((iFarmData['Nyield_kgkm'][206, 41, 0])/(iFarmData['Nfer_kgkm'][206, 41, 0] + iFarmData['Nman_kgkm'][206, 41, 0] + iFarmData['Nfix_kgkm'][206, 41, 0] + iFarmData['Ndep_kgkm'][206, 41, 0]))


# In[5]:


Years = [1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
Colombia = [Col11, Col10, Col9, Col8, Col7, Col6, Col5, Col4, Col3, Col2, Col1, Col0]
US = [US11, US10, US9, US8, US7, US6, US5, US4, US3, US2, US1, US0]
plt.plot(Years, Colombia)
plt.plot(Years, US)
plt.ylabel("Nitrogen Use Efficiency (NUE)")
plt.title("Nitrogen Use Efficiency in Coffee Production from 1960-2015")
plt.legend(["Colombia", "United States"])


# In[3]:


iFarmData.keys()


# In[15]:


PopCol0 = iFarmData["Popu_FAO"][40, 0]
PopCol1 = iFarmData["Popu_FAO"][40, 4]
PopCol2 = iFarmData["Popu_FAO"][40, 9]
PopCol3 = iFarmData["Popu_FAO"][40, 14]
PopCol4 = iFarmData["Popu_FAO"][40, 19]
PopCol5 = iFarmData["Popu_FAO"][40, 24]
PopCol6 = iFarmData["Popu_FAO"][40, 29]
PopCol7 = iFarmData["Popu_FAO"][40, 34]
PopCol8 = iFarmData["Popu_FAO"][40, 39]
PopCol9 = iFarmData["Popu_FAO"][40, 44]
PopCol10 = iFarmData["Popu_FAO"][40, 49]

PopUS0 = iFarmData["Popu_FAO"][206, 0]
PopUS1 = iFarmData["Popu_FAO"][206, 4]
PopUS2 = iFarmData["Popu_FAO"][206, 9]
PopUS3 = iFarmData["Popu_FAO"][206, 14]
PopUS4 = iFarmData["Popu_FAO"][206, 19]
PopUS5 = iFarmData["Popu_FAO"][206, 24]
PopUS6 = iFarmData["Popu_FAO"][206, 29]
PopUS7 = iFarmData["Popu_FAO"][206, 34]
PopUS8 = iFarmData["Popu_FAO"][206, 39]
PopUS9 = iFarmData["Popu_FAO"][206, 44]
PopUS10 = iFarmData["Popu_FAO"][206, 49]

YieldUS0 = iFarmData["Yield_FAO"][206, 41, 0]
YieldUS1 = iFarmData["Yield_FAO"][206, 41, 4]
YieldUS2 = iFarmData["Yield_FAO"][206, 41, 9]
YieldUS3 = iFarmData["Yield_FAO"][206, 41, 14]
YieldUS4 = iFarmData["Yield_FAO"][206, 41, 19]
YieldUS5 = iFarmData["Yield_FAO"][206, 41, 24]
YieldUS6 = iFarmData["Yield_FAO"][206, 41, 29]
YieldUS7 = iFarmData["Yield_FAO"][206, 41, 34]
YieldUS8 = iFarmData["Yield_FAO"][206, 41, 39]
YieldUS9 = iFarmData["Yield_FAO"][206, 41, 44]
YieldUS10 = iFarmData["Yield_FAO"][206, 41, 49]

YieldCol0 = iFarmData["Yield_FAO"][40, 41, 0]
YieldCol1 = iFarmData["Yield_FAO"][40, 41, 4]
YieldCol2 = iFarmData["Yield_FAO"][40, 41, 9]
YieldCol3 = iFarmData["Yield_FAO"][40, 41, 14]
YieldCol4 = iFarmData["Yield_FAO"][40, 41, 19]
YieldCol5 = iFarmData["Yield_FAO"][40, 41, 24]
YieldCol6 = iFarmData["Yield_FAO"][40, 41, 29]
YieldCol7 = iFarmData["Yield_FAO"][40, 41, 34]
YieldCol8 = iFarmData["Yield_FAO"][40, 41, 39]
YieldCol9 = iFarmData["Yield_FAO"][40, 41, 44]
YieldCol10 = iFarmData["Yield_FAO"][40, 41, 49]


# In[16]:


ColombiaYield = [YieldCol0, YieldCol1, YieldCol2, YieldCol3, YieldCol4, YieldCol5, YieldCol6, YieldCol7, YieldCol8, YieldCol9, YieldCol10]
USYield = [YieldUS0, YieldUS1, YieldUS2, YieldUS3, YieldUS4, YieldUS5, YieldUS6, YieldUS7, YieldUS8, YieldUS9, YieldUS10]
USPop = [PopUS0, PopUS1, PopUS2, PopUS3, PopUS4, PopUS5, PopUS6, PopUS7, PopUS8, PopUS9, PopUS10]
ColPop = [PopCol0, PopCol1, PopCol2, PopCol3, PopCol4, PopCol5, PopCol6, PopCol7, PopCol8, PopCol9, PopCol10]


# In[18]:


Years = [1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010]


# In[21]:


plt.plot(Years, USPop)
plt.plot(Years, ColPop)
plt.ylabel("Population")
plt.title("Population from 1960-2010 in Hundred Million")
plt.legend(["Colombia", "United States"])


# In[23]:


plt.plot(Years, USYield)
plt.plot(Years, ColombiaYield)
plt.ylabel("Yield in Tons")
plt.title("Green Coffee Yield from 1960-2010")
plt.legend(["Colombia", "United States"])


# In[24]:


Years2 = [1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
Colombia = [Col11, Col10, Col9, Col8, Col7, Col6, Col5, Col4, Col3, Col2, Col1, Col0]
US = [US11, US10, US9, US8, US7, US6, US5, US4, US3, US2, US1, US0]
plt.plot(Years2, Colombia)
plt.plot(Years2, US)
plt.ylabel("Nitrogen Use Efficiency (NUE)")
plt.title("Nitrogen Use Efficiency in Coffee Production from 1960-2015")
plt.legend(["Colombia", "United States"])


# In[ ]:




