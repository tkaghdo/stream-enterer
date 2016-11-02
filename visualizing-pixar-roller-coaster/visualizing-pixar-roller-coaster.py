
# coding: utf-8

# In[50]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[51]:

pixar_movies = pd.read_csv("PixarMovies.csv")
#display the dataframe in jupyter
pixar_movies


# In[52]:

#number of rows
print(pixar_movies.shape[0])
#number of columns
print(pixar_movies.shape[1])


# In[53]:

print(pixar_movies.head(15))


# In[54]:

#display the data type of each column
print(pixar_movies.dtypes)


# In[55]:

#generate summart of pixar_movies data frame
print(pixar_movies.describe())


# In[56]:

#strip % from the end of Domestic % and International % columns
pixar_movies["Domestic %"] = pixar_movies["Domestic %"].str.rstrip("%")
pixar_movies["International %"] = pixar_movies["International %"].str.rstrip("%")


# In[57]:

#convert Domestic % and International % to float
pixar_movies["Domestic %"] = pixar_movies["Domestic %"].astype(float)
pixar_movies["International %"] = pixar_movies["International %"].astype(float)


# In[58]:

#convert IMDB Score column from 10 point scale to 100
pixar_movies["IMDB Score"] = pixar_movies["IMDB Score"] * 10


# In[59]:

#remove rows with missing data
filterd_pixar = pixar_movies.dropna()


# In[60]:

#set the column Movie as the index for pixar_movies and filterd_pixar
pixar_movies.set_index("Movie", inplace=True)
filterd_pixar.set_index("Movie", inplace=True)


# In[67]:

#create a df for critics review
critics_reviews = pixar_movies[["RT Score","IMDB Score","Metacritic Score"]]


# In[69]:

#plot by critics review
critics_reviews.plot(figsize=(10,6))
plt.show()


# In[70]:

#How are the average ratings from each review site across all the movies distributed?
critics_reviews.plot(kind="box", figsize=(9,5))
plt.show()


# In[71]:

#How has the ratio of where the revenue comes from changed since the first movie? 
revenue_proportions = filterd_pixar[["Domestic %","International %"]]
revenue_proportions.plot(kind="bar", stacked="True")


# In[ ]:



