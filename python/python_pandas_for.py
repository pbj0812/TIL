#!/usr/bin/env python
# coding: utf-8

# In[14]:


#-*- coding: utf-8 -*-


# In[ ]:


# 날짜, 배이름


# In[50]:


import pandas as pd
import numpy as np


# In[51]:
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03']


for ii in range(len(month)):
    for iii in range(len(day)):
        data = pd.read_csv('C:/Users/user/Desktop/항적_해양환경공단(20190123)/2018'+month[ii]+'/Dynamic_2018'+month[ii]+day[iii]+'.csv', header=2, encoding='euc-kr')


        # In[52]:


        ship_name = list(data['MMSI(암호하)'])


        # In[53]:


        ship_name = list(set(ship_name))


        # In[54]:


        ship_name


        # In[58]:


        a = np.zeros(len(ship_name))
        b = np.zeros(len(ship_name))
        c = np.zeros(len(ship_name))
        d = np.zeros(len(ship_name))


        # In[62]:


        e = {'0_ship_name' : ship_name, '3H' : a, '3I' : b, '4E' : c, '4G' : d}


        # In[85]:


        result = pd.DataFrame(data=e)


        # In[64]:


        result


        # In[65]:


        len(data)


        # In[79]:


        for i in range(len(data)):
            if (data['경도'][i] > 128+(1/60*23))&(data['경도'][i] < 128+(1/60*24))         & (data['위도'][i] > 34+(1/60*11))&(data['위도'][i] < 128+(1/60*12)):
                result['3H'][ship_name.index(data['MMSI(암호하)'][i])] = 1
                print('3H')
            elif (data['경도'][i] > 128+(1/60*24))&(data['경도'][i] < 128+(1/60*25))         & (data['위도'][i] > 34+(1/60*11))&(data['위도'][i] < 128+(1/60*12)):
                result['3I'][ship_name.index(data['MMSI(암호하)'][i])] = 1
                print('3I')
            elif (data['경도'][i] > 128+(1/60*20))&(data['경도'][i] < 128+(1/60*21))         & (data['위도'][i] > 34+(1/60*10))&(data['위도'][i] < 128+(1/60*11)):
                result['4E'][ship_name.index(data['MMSI(암호하)'][i])] = 1
                print('4E')
            elif (data['경도'][i] > 128+(1/60*22))&(data['경도'][i] < 128+(1/60*23))         & (data['위도'][i] > 34+(1/60*10))&(data['위도'][i] < 128+(1/60*11)):
                result['4G'][ship_name.index(data['MMSI(암호하)'][i])] = 1
                print('4G')
            else:
                print('nop')


        # In[80]:


        ship_name


        # In[77]:


        ship_name.index(data['MMSI(암호하)'][i])


        # In[81]:


        result


        # In[83]:


        result.to_csv('C:/Users/user/Desktop/항적_해양환경공단(20190123)/2018'+month[ii]+'/result_201801'+month[ii]+day[iii]+'.csv', mode='w')


        # In[ ]:
