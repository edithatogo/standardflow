#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import json
sys.path.append('../../')
from src.prisma import PrismaDiagram
from IPython.display import Image


# In[ ]:


with open('../../data/prisma_2020_updated_data.json', 'r') as f:
    data = json.load(f)


# In[ ]:


prisma = PrismaDiagram(data)
prisma.save('examples/images/prisma_2020_updated_diagram.png')


# In[ ]:


Image(filename='prisma_2020_updated_diagram.png')
