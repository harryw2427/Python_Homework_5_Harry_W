#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=int(input('Please tell me a number: '))
if a%2==0:
    print('That number is even')
else:
    print('That number is odd')


# In[10]:


Windy=input('Is it Windy today? Please enter True or False: ')
Cold=input('Is it Cold today? Please enter True or False: ')
if (Cold=='True' and Windy=='True'):
    print('I brought my jacket so now I wont get wet!:) ')
elif (Cold=='True' and Windy=='False'):
    print('I guess I should go get my rain jacket. ')
elif (Windy=='True' and Cold=='False'):
    print('I guess I should go get my windproof jacket. ')
elif (Windy=='False' and Cold=='False'):
    print('I do not need a jacket Hooray!')
else:
    print('That is not an option please choose a different answer. ')


# In[ ]:




