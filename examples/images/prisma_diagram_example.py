#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.path.append('../../')
import json
from src.prisma import PrismaDiagram
from src.main import generate_artifact


# In[ ]:


with open('../data/prisma_data.json', 'r') as f:
    data = json.load(f)


# In[ ]:


prisma = PrismaDiagram(data)
prisma.save('examples/images/prisma_diagram.png')
