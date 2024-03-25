#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[ ]:


nltk.download()


# In[ ]:


from nltk.tokenize import sent_tokenize,word_tokenize


# In[ ]:


text="Natural Language processing is an amazing topic"


# In[ ]:


nltk.download('punkt')


# In[ ]:


word_tokenixe(text)


# In[ ]:


nltk.download('stopwords')
from nltk.corpus import stopwords


# In[ ]:


stopwords.words("english")


# In[ ]:


from nltk.stem import WordNetLemmatizer


# In[ ]:


lemma=WordNetLemmatizer()


# In[ ]:


lemma.lemmatize("comes")


# In[ ]:


lemma.lemmatize("better",pose="a")


# In[ ]:




