#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('../../')
import json
from src.consort import ConsortDiagram
from src.main import generate_artifact


# In[ ]:


with open('data/consort_data.json', 'r') as f:
    data = json.load(f)


# In[ ]:


consort = ConsortDiagram(data)
consort.save('examples/images/consort_diagram.png')
