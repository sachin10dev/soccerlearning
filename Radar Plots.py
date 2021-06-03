#!/usr/bin/env python
# coding: utf-8

# In[38]:


import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
categories = ['Goals','Assists','Non-Penalty Goals','xG','xA', 'npxG', 'npxG+A','Shots on target %','Goals/Shots on target']
fig = go.Figure()
#fig.add_trace(go.Scatterpolar(r = [99,54,99,98,98,91,97,87,93], theta = categories, fill = 'toself',name = 'Gundogan'))
fig.add_trace(go.Scatterpolar(r = [98,93,73,98,71,98,89,55,27], theta = categories, fill = 'toself',name = 'Bruno Fernandes'))
fig.add_trace(go.Scatterpolar(r = [99,99,98,99,99,99,99,69,62], theta = categories, fill = 'toself',name = 'Kevin De Bryune'))
#fig.add_trace(go.Scatterpolar(r = [88,86,89,93,94,98,98,67,53], theta = categories, fill = 'toself',name = 'Mason Mount'))
#fig.add_trace(go.Scatterpolar(r = [95,19,97,96,99,24,90,76,85], theta = categories, fill = 'toself',name = 'Tomas Soucek'))
#fig.add_trace(go.Scatterpolar(r = [43,85,52,24,30,95,73,42,49], theta = categories, fill = 'toself',name = 'Jack Grealish'))
fig.show()


# In[80]:


# Libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import itertools as it

# Set data
#reading the excel file into a basedata DataFrame
basedata = pd.read_excel(r'S:\Data\MidComp2020-21.xlsx', converters={'Statistic':str,'Gundogan':int,'Bruno Fernandes':int,'Kevin De Bryune':int,'Mason Mount':int,'Tomas Soucek':int,'Jack Grealish':int,})

#extracting each column in the DataFrame into a separate DF
statistic = pd.DataFrame(basedata, columns=['Statistic'])
bf = pd.DataFrame(basedata, columns=['Bruno Fernandes'])
kdb = pd.DataFrame(basedata, columns=['Kevin De Bryune'])
mm = pd.DataFrame(basedata, columns=['Mason Mount'])
ts = pd.DataFrame(basedata, columns=['Tomas Soucek'])
jg = pd.DataFrame(basedata, columns=['Jack Grealish'])
g = pd.DataFrame(basedata, columns=['Gundogan'])

#Converting the dataframes into list for easier analysis
stats = statistic.values.tolist()
gundo = g.values.tolist()
bruno = bf.values.tolist()
kevin = kdb.values.tolist()
mount = mm.values.tolist()
soucek = ts.values.tolist()
grealish = jg.values.tolist()

#merging the individual lists inside the main list, since the values.tolist() function was reading all dataframe elements
#as separate lists
mergedgundo = list(it.chain.from_iterable(gundo))
mergedbruno = list(it.chain.from_iterable(bruno))
mergedkdb = list(it.chain.from_iterable(kevin))
mergedmount = list(it.chain.from_iterable(mount))
mergedsoucek = list(it.chain.from_iterable(soucek))
mergedgrealish = list(it.chain.from_iterable(grealish))
mergedstats = list(it.chain.from_iterable(stats))

#creating index lists that can be customized based on what stat you want you see in the radar plot
genindices = [0,1,2,7,8,9,10,14,16]
passindices = [28,33,36,41,46,48,72,79,109,113,114,125,126]
gungen = [mergedgundo[index] for index in genindices]
bfengen = [mergedbruno[index] for index in genindices]
sttgen = [mergedstats[index] for index in genindices]

#extracting the necessary values from the base list for each player
gunpass = [mergedgundo[index] for index in passindices]
bfenpass = [mergedbruno[index] for index in passindices]
sttpass = [mergedstats[index] for index in passindices]

#Radar Plot
#Plot for General stats
fig1 = go.Figure()
fig1.add_trace(go.Scatterpolar(r = gungen, theta = sttgen, fill = 'toself',name = 'Gundogan'))
fig1.add_trace(go.Scatterpolar(r = bfengen, theta = sttgen, fill = 'toself',name = 'Bruno Fernandes'))
fig1.show()

#Plot for Passing stats
fig2 = go.Figure()
fig2.add_trace(go.Scatterpolar(r = gunpass, theta = sttpass, fill = 'toself',name = 'Gundogan'))
fig2.add_trace(go.Scatterpolar(r = bfenpass, theta = sttpass, fill = 'toself',name = 'Bruno Fernandes'))
fig2.show()


# In[ ]:




