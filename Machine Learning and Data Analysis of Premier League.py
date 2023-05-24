#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings
import sklearn as sk
import sklearn.tree as tree
from datetime import date
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')
from IPython.display import Image  
import pydotplus
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
df = pd.read_csv("points_table.csv")
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


# Meaning of each column :
# 
# Season -- Year in which the league was 
# 
# Pos -- Team position in the league
# 
# Team -- Team name
# 
# Pld -- Games played
# 
# W -- Games won
# 
# D -- Games tied
# 
# L -- Games lost
# 
# GF -- Goals for
# 
# GA -- Goals against
# 
# GD -- Goal difference
# 
# Pts -- Points won
# 
# Qualification or relegation -- Qualification to Europe Cups or relegation to Football League First Division

# In[ ]:


df


# In[ ]:


df.head()


# In[ ]:


df.tail()


# # Data Cleaning
# 

# In[ ]:


df.columns = ['Position',
             'Team',
             'GamesPlayed',
             'Win',
             'Draw',
             'Loss',
             'GF',
             'GA','GD',
             'Points',
             'Qual_Reg']


# In[ ]:


# 1) Make Qualification and Relegation less wordy
# 2) Check for Null Values 


# In[ ]:


#1 
#check for unique values in Qualification or relegation column
df['Qual_Reg'].nunique()
df['Qual_Reg'].unique()


# Only want to focus on Champions League, Europa League, and Relegation
# 
# Champions League access for the next season is given to the top 4 teams that season (exceptions may include winning the Europa league that season)
# 
# Since the 2009–10 season, UEFA Cup was rebranded as the UEFA Europa League.
# 
# Since the 2004-2005 season, Football League First Division was rebranded as the Football League Championship
# 

# ## Making 'Qualification or relegation' into a dummy variable

# In[ ]:


# Decrease the nunique number


# In[ ]:


def Qual_Reg_Changes(Qual_Reg_String):
    if Qual_Reg_String.startswith('Qualification for the Champions League'):
        return "Champions League"
    elif 'relegation'in Qual_Reg_String:
        return "Relegation"
    elif 'Relegation'in Qual_Reg_String:
        return "Relegation"
    elif Qual_Reg_String.startswith('Qualification for the Europa League'):
        return "Europa League"
    elif Qual_Reg_String.startswith('Qualification for the UEFA Cup'):
        return "Europa League"
    else:
        return 'N/A'


# In[ ]:


df['Qual_Reg'] = df['Qual_Reg'].apply(Qual_Reg_Changes)


# In[ ]:


df['Qual_Reg'].nunique()
df['Qual_Reg'].unique()


# In[ ]:


#checking for nulls
df.isnull().sum().any()


# In[ ]:


df.head()


# In[ ]:


#add Result Column


# In[ ]:


#df['Result']


# # Insight 1: Does Goals For, Goals Against, and Goal Differential matter?

# In[ ]:


#we can look at the top gf and top ga and compare each with their league positions


# In[ ]:


GF_subsetdf = df[["Position", "Team",'GF','Qual_Reg']]
GF_subsetdf.sort_values(by = 'GF', ascending = False).head(10)


# In[ ]:


GF_subsetdf.sort_values(by = 'GF', ascending = False).tail(10)


# In[ ]:


GF_subsetdf.sort_values(by = 'GF', ascending = False)


# In[ ]:


#Goals Against vs Position


# In[ ]:


GA_subsetdf = df[["Position", "Team",'GA','Qual_Reg']]
GA_subsetdf.sort_values(by = 'GA').head(10)


# In[ ]:


GA_subsetdf.sort_values(by = 'GA').tail(10)


# In[ ]:


GA_subsetdf.sort_values(by = 'GA', ascending = False)


# In[ ]:





# ## Seaborn 

# In[ ]:


#here to help us think
df.corr()


# In[ ]:


#GOals Against
sns.catplot(x = 'GA', y ='Qual_Reg', data = df, kind = 'strip', aspect = 2)


# In[ ]:


sns.catplot(y = 'GA', x ='Position', data = df, kind = 'bar', aspect = 2)


# In[ ]:


sns.catplot(y = 'GA', x ='Position', data = df, kind = 'swarm', aspect = 2)


# In[ ]:


#Goals FOR
sns.catplot(x = 'GF', y ='Qual_Reg',data = df, kind = 'strip', aspect = 2)


# In[ ]:


sns.catplot(y = 'GF', x ='Position', data = df, kind = 'bar', aspect = 2)


# In[ ]:


sns.catplot(y = 'GA', x ='Position', data = df, kind = 'swarm', aspect = 2)


# In[ ]:


#Goal Differential


# In[ ]:


sns.catplot(x = 'GD', y ='Qual_Reg',data = df, kind = 'strip', aspect = 2)


# In[ ]:


sns.catplot(y = 'GD', x ='Position', data = df, kind = 'bar', aspect = 2)


# In[ ]:


sns.catplot(y = 'GA', x ='Position', data = df, kind = 'swarm', aspect = 2)


# In[ ]:


df.corr()


# In[ ]:


sns.regplot(y = 'Draw', x = 'GF' , data = df, scatter = False,lowess =True)


# In[ ]:


sns.regplot(y = 'Draw', x = 'GA' , data = df, scatter = False, lowess = True)


# In[ ]:


sns.regplot(y = 'Draw', x = 'GD' , data = df, scatter = False, lowess = True)


# # ML

# In[ ]:


from sklearn import linear_model


# In[ ]:


Y = df.Position

X = df.drop(columns = 'Position', axis = 1)
X = X.drop(columns = 'Qual_Reg', axis = 1)
X = X.drop(columns = 'Team', axis = 1)


# In[ ]:


dt = tree.DecisionTreeRegressor(max_depth=5)


# In[ ]:


dt.fit(X,Y)


# In[ ]:


import sklearn.tree as tree
from IPython.display import Image  
import pydotplus

dt_feature_names = list(X.columns)
dt_target_names = np.array(Y.unique(),dtype=np.string_) 
tree.export_graphviz(dt, out_file='tree.dot', 
    feature_names=dt_feature_names, class_names=dt_target_names,
    filled=True)  
graph = pydotplus.graph_from_dot_file('tree.dot')
Image(graph.create_png())


# In[ ]:


# Decision Tree Without using Points as a predictor


# In[ ]:


Y = df.Position

X = df.drop(columns = 'Position', axis = 1)
X = X.drop(columns = 'Qual_Reg', axis = 1)
X = X.drop(columns = 'Points', axis = 1)
X = X.drop(columns = 'Team', axis = 1)


# In[ ]:


dt = tree.DecisionTreeRegressor(max_depth=3)


# In[ ]:


dt.fit(X,Y)


# In[ ]:


dt_feature_names = list(X.columns)
dt_target_names = np.array(Y.unique(),dtype=np.string_) 
tree.export_graphviz(dt, out_file='tree.dot', 
    feature_names=dt_feature_names, class_names=dt_target_names,
    filled=True)  
graph = pydotplus.graph_from_dot_file('tree.dot')
Image(graph.create_png())


# In[ ]:


#Decision Tree without using Wins/Losses


# In[ ]:


Y = df.Position

X = df.drop(columns = 'Position', axis = 1)
X = X.drop(columns = 'Qual_Reg', axis = 1)
X = X.drop(columns = 'Points', axis = 1)
X = X.drop(columns = 'Win', axis = 1)
X = X.drop(columns = 'Loss', axis = 1)
X = X.drop(columns = 'Team', axis = 1)


# In[ ]:


dt = tree.DecisionTreeRegressor(max_depth=3)


# In[ ]:


dt.fit(X,Y)


# In[ ]:


dt_feature_names = list(X.columns)
dt_target_names = np.array(Y.unique(),dtype=np.string_) 
tree.export_graphviz(dt, out_file='tree.dot', 
    feature_names=dt_feature_names, class_names=dt_target_names,
    filled=True)  
graph = pydotplus.graph_from_dot_file('tree.dot')
Image(graph.create_png())


# In[ ]:


from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# In[ ]:


acc = accuracy_score(Y, X)


# In[ ]:


df

