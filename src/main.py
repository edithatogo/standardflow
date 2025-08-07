import json
from jsonschema import validate
from src.consort import ConsortDiagram
from src.prisma import PrismaDiagram
from src.strobe import StrobeDiagram
from src.checklist import Checklist

def generate_artifact(input_path, output_path, schema_dir='schemas'):
    """
    Generates an artifact from a JSON file.
    """
    with open(input_path, 'r') as f:
        data = json.load(f)

    diagram_type = data.get('diagram_type')
    if not diagram_type:
        raise ValueError("The 'diagram_type' key is missing from the JSON file.")

    schema_path = f"{schema_dir}/{diagram_type.lower()}_schema.json"
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)

    if diagram_type == "CONSORT":
        diagram = ConsortDiagram(data)
        diagram.save(output_path)
        print(f"CONSORT diagram saved as {output_path}")
    elif diagram_type == "PRISMA":
        diagram = PrismaDiagram(data)
        diagram.save(output_path)
        print(f"PRISMA diagram saved as {output_path}")
    elif diagram_type == "STROBE":
        diagram = StrobeDiagram(data)
        diagram.save(output_path)
        print(f"STROBE diagram saved as {output_path}")
    elif "checklist" in diagram_type.lower():
        checklist = Checklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    else:
        raise ValueError(f"Unknown diagram_type: {diagram_type}")
