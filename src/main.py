import json
import argparse
from jsonschema import validate
from .prisma import PrismaDiagram
from .consort import ConsortDiagram
from .strobe import StrobeDiagram

def main():
    """
    Main function to generate a diagram from a JSON file.
    """
    parser = argparse.ArgumentParser(description='Generate a diagram from a JSON file.')
    parser.add_argument('input', type=str, help='Path to the input JSON file.')
    parser.add_argument('-o', '--output', type=str, default='diagram.png',
                        help='Output file name. The format is determined by the file extension '
                             '(e.g., .png, .svg, .pdf, .tiff, .eps).')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        data = json.load(f)

    if 'diagram_type' not in data:
        raise ValueError("The input JSON file must have a 'diagram_type' field.")

    diagram_type = data['diagram_type']

    if diagram_type == 'PRISMA':
        schema_path = 'schemas/prisma_schema.json'
        DiagramClass = PrismaDiagram
    elif diagram_type == 'CONSORT':
        schema_path = 'schemas/consort_schema.json'
        DiagramClass = ConsortDiagram
    elif diagram_type == 'STROBE':
        schema_path = 'schemas/strobe_schema.json'
        DiagramClass = StrobeDiagram
    else:
        raise ValueError(f"Unknown diagram type: {diagram_type}")

    with open(schema_path, 'r') as f:
        schema = json.load(f)

    validate(instance=data, schema=schema)

    diagram = DiagramClass(data)
    diagram.generate(args.output)

if __name__ == '__main__':
    main()
