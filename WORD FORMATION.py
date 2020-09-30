#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyenchant


# In[2]:


import enchant


# In[3]:


import itertools


# In[9]:


def yes_or_no_error_handling():
  """The function is used to restrict the input to B or A"""
  while True:
    try:
      answer = input(f'\nSpecify B for British and A for American ')
      if answer.upper() in  ['B','A']:
        return answer.upper()

    except Exception:
      print("You inputed the wrong entry, retry by specifying B or A ")
    else:
      print("You inputed the wrong entry, retry by specifying B or A ")


# In[10]:


def english_selector():
    """ This function gets the users' dialect type(British or American)"""
    british_english = enchant.Dict("en_GB")
    american_english = enchant.Dict("en_US")
    print('Specify your English Dialect')
    language_selector = yes_or_no_error_handling()
    if language_selector=='B':
        selected_lang=british_english
        print(f"\nYou've opted for BRITISH ENGLISH")
    else:
        selected_lang=american_english
        print(f"\nYou've opted for AMERICAN ENGLISH")
    return selected_lang


# In[14]:


def hasNumbers(english):
    """ This function test for non-english word and digit"""
    while True:
        try:
            inputString = input("\nEnter the word ")
            if all(char.isalpha() for char in inputString):
                if english.check(inputString)==True:
                    return inputString.lower()
                else:
                    print(f'{inputString} is not an english word')
        except Exception:
            print("What you inputed is either not an english word or contains digit ")
        else:
            print("What you inputed is either not an english word or contains digit ")


# In[15]:


def english_word():
    "This function gives all possible english word that can be generated from inputed word"
    english=english_selector()
    word=hasNumbers(english)
    english_list=set()
    for i in range(3,len(word)+1):
        permutation=itertools.permutations(word,i)
        for c in permutation:
            if english.check(''.join(c))==True:
                english_list.add(''.join(c))
    print()
    english_list.remove(word)
    print(f'{len(english_list)} different words can be formed from {word}')           
    return english_list
            


# In[16]:


english_word()


# In[ ]:




