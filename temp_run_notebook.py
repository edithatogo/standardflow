import sys
sys.path.append('./')
import json
from src.consort import ConsortDiagram

with open('examples/data/consort_data.json', 'r') as f:
    data = json.load(f)

consort = ConsortDiagram(data)
consort.build_graph()
consort.save('examples/images/consort_diagram_example')
