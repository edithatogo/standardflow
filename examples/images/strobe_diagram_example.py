#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('../../')
import json
from src.strobe import StrobeDiagram
from src.main import generate_artifact


# In[ ]:


with open('../data/strobe_data.json', 'r') as f:
    data = json.load(f)


# In[ ]:


strobe = StrobeDiagram(data)
strobe.save('examples/images/strobe_diagram.png')
