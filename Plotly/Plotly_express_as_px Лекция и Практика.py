#!/usr/bin/env python
# coding: utf-8

# In[66]:


import plotly.express as px
import numpy as np
import pandas as pd


# In[67]:


fig = px.scatter(x = [0,1,2,3,4], y = [0,1,4,9,16])
# основное условие, чтобы х и у были одной длинны
fig.show()


# In[68]:


# Построение графика на основе датафрейма iris
df = px.data.iris()
df.head()


# In[54]:


fig = px.scatter(data_frame = df, x = 'sepal_width', y = 'sepal_length' )
fig.show()


# In[55]:


get_ipython().system('pip install -U kaleido')


# In[56]:


#!pip install -U kaleido
from plotly.io import write_image


# In[57]:


fig.write_image('fig2.pdf', engine = 'kaleido')


# In[58]:


get_ipython().system('ls')


# In[59]:


# изменение размера графика height-высота и width-ширины этот параметр задает количество пикселей от 10 и более
fig = px.scatter(data_frame = df, x = 'sepal_width', y = 'sepal_length', height = 300, width = 500  )
fig.show()


# ## Практическое задание.
# 
# **Постройте следующие графики:**
# 
# * график на основе датасета iris, где на оси х будут лежать значения sepal_length, на оси y — petal_length (понадобится в следующем уроке).
# * график логарифма y = log x (создавать массив x можно любыми способами, вручную или с помощью numpy, а конструировать y, конечно, лучше с помощью метода np.log).
# 
# Увеличьте и сохраните предыдущий график с логарифмом в формате pdf, проверьте, что он действительно сохранился в нужном формате.

# In[60]:


dff = px.data.iris()
dff.head(3)


# In[61]:


fig_l1 = px.scatter(dff, 'sepal_length', 'petal_length', height = 400, width = 600)
fig_l1.show()


# In[62]:



fig_log = px.scatter(dff, x = 'sepal_length', y = np.log(dff.sepal_length), height = 400, width = 600)
fig_log.show()


# ### Изменение цвета по классам

# In[63]:


# color = 'species'
fig_l1 = px.scatter(dff, 'sepal_length', 'petal_length', height = 400, width = 600, color = 'species')
fig_l1.show()


# ### Изменение размера данных в зависимости от признака

# In[64]:


# size = 'petal_width'
fig_l1 = px.scatter(dff, 'sepal_length', 'petal_length', height = 400, width = 600, color = 'species',                   size = 'petal_width')
fig_l1.show()


# ### Практическое задание.
# 
# **Задание 1.** Чтобы успешно освоить новую библиотеку, нужно научиться пользоваться её документацией. В ней вы всегда найдёте ответы на частые вопросы: как поменять цвет объектов, как добавить названия осей координат и так далее. Поэтому первое задание будет совсем небольшим: изучите документацию к методу scatter из plotly express и добавьте к вашему графику заголовок, например **“Iris flower data”**.
# 
# Должен получиться примерно такой график:

# In[65]:


# size = 'petal_width'
fig_l1 = px.scatter(dff, 'sepal_length', 'petal_length', height = 400, width = 600, color = 'species',                   size = 'petal_width')
fig_l1.update_layout(title= 'Iris flower data')
fig_l1.show()


# ## Задание 2.
# 
# Исследуйте следующие данные: сохраните датасет px.data.gapminder() — в нём содержатся данные о продолжительности жизни и о количестве проживающих в разных странах мира за период с 1952 по 2007 год.
# 
# * отфильтруйте его значения по условию continent = Oceania;
# * постройте scatter-график изменения продолжительности жизни с течением времени;
# * используя параметр color, выделите точки, относящиеся к разным странам, (подсказка: используйте колонку country);
# * исследуйте, как менялась популяция (колонка pop), передав в scatter параметр size.

# In[19]:


data_g = px.data.gapminder()
data_g.head()


# #### отфильтруйте его значения по условию continent = Oceania;

# In[21]:


dff = data_g[data_g.continent == 'Oceania']
dff.head()


# #### постройте scatter-график изменения продолжительности жизни с течением времени;

# In[23]:


fig_dff = px.scatter(dff, 'lifeExp', 'year', height = 400, width = 600)

fig_dff.show()


# #### используя параметр color, выделите точки, относящиеся к разным странам, (подсказка: используйте колонку country)

# In[24]:


fig_dff = px.scatter(dff, 'lifeExp', 'year', height = 400, width = 600, color = 'country')

fig_dff.show()


# #### исследуйте, как менялась популяция (колонка pop), передав в scatter параметр size

# In[32]:


fig_dff = px.scatter(dff, 'lifeExp', 'year', height = 400, width = 600, color = 'country',                    size = 'pop', title = 'данные о продолжительности жизни ')

fig_dff.update_layout(xaxis_title = 'продолжительность жизни', yaxis_title = 'Год')

fig_dff.show()


# In[36]:


dh = pd.read_csv('G:/Data sainse/plotly/11.4 data_house.csv')
dh.head()


# In[37]:


dh.area.unique()


# In[43]:


dh_sample = dh[dh.area.isin(['hammersmith and fulham','kensington and chelsea', 'barking and dagenham',                            'camden'])]
fig_dh = px.line(dh_sample, 'date', 'average_price')

fig_dh.show()


# #### добавив параметр цвета по выбраным регионам отбора, через color

# In[44]:


fig_dh = px.line(dh_sample, 'date', 'average_price', color = 'area')

fig_dh.show()


# #### добавим дополнительные объекты для вывода в визуализации через hover_data

# In[46]:


fig_dh = px.line(dh_sample, 'date', 'average_price', color = 'area', hover_data = ['houses_sold'])
# можно добавить несколько стобцов датафрейма или весь сет целиком dh_sample

fig_dh.show()


# In[ ]:




