#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

titanic = pd.read_csv('train.csv')

titanic


# In[3]:


titanic.isnull().sum()


# In[ ]:


#1 classe


# In[60]:


titanic_c1 = titanic


# In[62]:


titanic_c1 = titanic_c1.loc[titanic_c1.Pclass==1]


# In[63]:


titanic_c1['Age'].mean()


# In[70]:


#female

titanic_c1_f = titanic_c1


# In[71]:


titanic_c1_f = titanic_c1_f.loc[titanic_c1_f.Sex=='female']

titanic_c1_f.shape


# In[72]:


titanic_c1_f['Age'].mean()


# In[73]:


#male

titanic_c1_m = titanic_c1


# In[74]:


titanic_c1_m = titanic_c1_m.loc[titanic_c1_m.Sex=='male']

titanic_c1_m.shape


# In[75]:


titanic_c1_m['Age'].mean()


# In[ ]:


#2 classe


# In[64]:


titanic_c2 = titanic


# In[65]:


titanic_c2 = titanic_c2.loc[titanic_c2.Pclass==2]


# In[66]:


titanic_c2['Age'].mean()


# In[76]:


#female

titanic_c2_f = titanic_c2


# In[77]:


titanic_c2_f = titanic_c2_f.loc[titanic_c2_f.Sex=='female']

titanic_c2_f.shape


# In[78]:


titanic_c2_f['Age'].mean()


# In[79]:


#male

titanic_c2_m = titanic_c2


# In[80]:


titanic_c2_m = titanic_c2_m.loc[titanic_c2_m.Sex=='male']

titanic_c2_m.shape


# In[81]:


titanic_c2_m['Age'].mean()


# In[ ]:


#3 classe


# In[67]:


titanic_c3 = titanic


# In[68]:


titanic_c3 = titanic_c3.loc[titanic_c3.Pclass==3]


# In[69]:


titanic_c3['Age'].mean()


# In[82]:


#female

titanic_c3_f = titanic_c3


# In[83]:


titanic_c3_f = titanic_c3_f.loc[titanic_c3_f.Sex=='female']

titanic_c3_f.shape


# In[84]:


titanic_c3_f['Age'].mean()


# In[85]:


#male

titanic_c3_m = titanic_c3


# In[86]:


titanic_c3_m = titanic_c3_m.loc[titanic_c3_m.Sex=='male']

titanic_c3_m.shape


# In[87]:


titanic_c3_m['Age'].mean()


# In[ ]:





# In[ ]:


#SOBREVIVENTES


# In[9]:


titanic_sobreviventes = titanic 

titanic_sobreviventes = titanic_sobreviventes.loc[titanic_sobreviventes.Survived==1]

titanic_sobreviventes.shape


# In[21]:


titanic_sobreviventes['Age'].mean()


# In[24]:


#female

titanic_sobreviventes_f = titanic_sobreviventes


# In[32]:


titanic_sobreviventes_f = titanic_sobreviventes_f.loc[titanic_sobreviventes_f.Sex=='female']

titanic_sobreviventes_f.shape


# In[30]:


titanic_sobreviventes_f['Age'].mean()


# In[27]:


#male

titanic_sobreviventes_m = titanic_sobreviventes


# In[33]:


titanic_sobreviventes_m = titanic_sobreviventes_m.loc[titanic_sobreviventes_m.Sex=='male']

titanic_sobreviventes_m.shape


# In[31]:


titanic_sobreviventes_m['Age'].mean()


# In[ ]:





# In[ ]:


#classes


# In[43]:


titanic_sobreviventes_c1 = titanic_sobreviventes


# In[45]:


titanic_sobreviventes_c1 = titanic_sobreviventes_c1.loc[titanic_sobreviventes_c1.Pclass==1]

titanic_sobreviventes_c1.shape


# In[ ]:





# In[47]:


titanic_sobreviventes_c2 = titanic_sobreviventes


# In[48]:


titanic_sobreviventes_c2 = titanic_sobreviventes_c2.loc[titanic_sobreviventes_c2.Pclass==2]

titanic_sobreviventes_c2.shape


# In[ ]:





# In[49]:


titanic_sobreviventes_c3 = titanic_sobreviventes


# In[50]:


titanic_sobreviventes_c3 = titanic_sobreviventes_c3.loc[titanic_sobreviventes_c3.Pclass==3]

titanic_sobreviventes_c3.shape


# In[ ]:





# In[ ]:





# In[ ]:


#NÃO SOBREVIVENTES


# In[10]:


titanic_naosobreviventes = titanic

titanic_naosobreviventes = titanic_naosobreviventes.loc[titanic_naosobreviventes.Survived==0]

titanic_naosobreviventes.shape


# In[22]:


titanic_naosobreviventes['Age'].mean()


# In[35]:


#female

titanic_naosobreviventes_f = titanic_naosobreviventes


# In[37]:


titanic_naosobreviventes_f = titanic_naosobreviventes_f.loc[titanic_naosobreviventes_f.Sex=='female']

titanic_naosobreviventes_f.shape


# In[41]:


titanic_naosobreviventes_f['Age'].mean()


# In[39]:


#male

titanic_naosobreviventes_m = titanic_naosobreviventes


# In[40]:


titanic_naosobreviventes_m = titanic_naosobreviventes_m.loc[titanic_naosobreviventes_m.Sex=='male']

titanic_naosobreviventes_m.shape


# In[42]:


titanic_naosobreviventes_m['Age'].mean()


# In[ ]:





# In[ ]:


#classes


# In[51]:


titanic_naosobreviventes_c1 = titanic_naosobreviventes


# In[53]:


titanic_naosobreviventes_c1 = titanic_naosobreviventes_c1.loc[titanic_naosobreviventes_c1.Pclass==1]

titanic_naosobreviventes_c1.shape


# In[54]:


titanic_naosobreviventes_c2 = titanic_naosobreviventes


# In[56]:


titanic_naosobreviventes_c2 = titanic_naosobreviventes_c2.loc[titanic_naosobreviventes_c2.Pclass==2]

titanic_naosobreviventes_c2.shape


# In[57]:


titanic_naosobreviventes_c3 = titanic_naosobreviventes


# In[59]:


titanic_naosobreviventes_c3 = titanic_naosobreviventes_c3.loc[titanic_naosobreviventes_c3.Pclass==3]

titanic_naosobreviventes_c3.shape


# In[ ]:





# In[ ]:





# In[14]:


titanic2 = titanic


# In[16]:


titanic2['Age'].fillna(titanic2['Age'].median(), inplace=True)


# In[18]:


titanic2['Embarked'].fillna('Port', inplace=True)
                            


# In[ ]:




