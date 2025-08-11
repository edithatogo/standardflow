import json
from jsonschema import validate
from src.consort import ConsortDiagram
from src.prisma import PrismaDiagram
from src.strobe import StrobeDiagram
from src.checklist import Checklist

def validate_data(data, schema_dir='schemas'):
    """
    Validates the given data against the appropriate schema.
    """
    diagram_type = data.get('diagram_type')
    if not diagram_type:
        raise ValueError("The 'diagram_type' key is missing from the JSON file.")

    schema_path = f"{schema_dir}/{diagram_type.lower()}_schema.json"
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)
    return data

def generate_artifact(input_path, output_path, style_path=None, set_values=None, schema_dir='schemas'):
    """
    Generates an artifact from a JSON file.
    """
    with open(input_path, 'r') as f:
        data = json.load(f)

    if style_path:
        with open(style_path, 'r') as f:
            style_data = json.load(f)
        data['style'] = style_data

    if set_values:
        for item in set_values:
            key, value = item.split('=', 1)
            # try to convert to int or float
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
            data[key] = value

    data = validate_data(data, schema_dir)
    diagram_type = data.get('diagram_type')

    if diagram_type == "CONSORT":
        diagram = ConsortDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"CONSORT diagram saved as {output_path}")
    elif diagram_type == "PRISMA":
        diagram = PrismaDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"PRISMA diagram saved as {output_path}")
    elif diagram_type == "STROBE":
        diagram = StrobeDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"STROBE diagram saved as {output_path}")
    elif "checklist" in diagram_type.lower():
        checklist = Checklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    else:
        raise ValueError(f"Unknown diagram_type: {diagram_type}")
