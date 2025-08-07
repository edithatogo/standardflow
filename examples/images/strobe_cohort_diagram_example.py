#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import json
sys.path.append('../../')
from src.strobe import StrobeDiagram
from IPython.display import Image


# In[ ]:


with open('../../data/strobe_cohort_data.json', 'r') as f:
    data = json.load(f)


# In[ ]:


strobe = StrobeDiagram(data)
strobe.save('examples/images/strobe_cohort_diagram.png')


# In[ ]:


Image(filename='strobe_cohort_diagram.png')
