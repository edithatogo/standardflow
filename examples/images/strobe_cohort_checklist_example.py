#!/usr/bin/env python
# coding: utf-8

# # STROBE Cohort Checklist Example
#
# This notebook demonstrates how to generate a STROBE checklist for a cohort study using the `Checklist` class.

# In[1]:


import sys
import json
sys.path.append('../../src')
from checklist import Checklist
from IPython.display import Markdown


# ## Load Data from a JSON file

# In[2]:


with open('../../data/strobe_cohort_checklist.json', 'r') as f:
    data = json.load(f)


# ## Create a Checklist object

# In[3]:


checklist = Checklist(data)


# ## Generate and Display the Checklist

# In[4]:


sections = checklist.to_markdown_by_section()
for section, markdown in sections.items():
    print(f'## {section}')
    display(Markdown(markdown))
