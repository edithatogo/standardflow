import json
import argparse
from jsonschema import validate
from .prisma import PrismaDiagram
from .consort import ConsortDiagram
from .strobe import StrobeDiagram
from .checklist import Checklist

def generate_artifact(input_path, output_path):
    """
    Generates a diagram or checklist from a JSON file.
    """
    with open(input_path, 'r') as f:
        data = json.load(f)

    if 'diagram_type' in data:
        diagram_type = data['diagram_type']
        if diagram_type == 'PRISMA' or diagram_type == 'PRISMA_2020_UPDATED':
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
        diagram.generate(output_path)

    elif 'checklist_type' in data:
        checklist_type = data['checklist_type']
        schema_path = 'schemas/checklist_schema.json'
        ChecklistClass = Checklist

        with open(schema_path, 'r') as f:
            schema = json.load(f)

        validate(instance=data, schema=schema)

        checklist = ChecklistClass(data)
        checklist.generate(output_path)

    else:
        raise ValueError("The input JSON file must have either a 'diagram_type' or a 'checklist_type' field.")

def main():
    """
    Main function to generate a diagram or checklist from a JSON file.
    """
    parser = argparse.ArgumentParser(description='Generate a diagram or checklist from a JSON file.')
    parser.add_argument('input', type=str, help='Path to the input JSON file.')
    parser.add_argument('-o', '--output', type=str, default='output',
                        help='Output file name. The format is determined by the file extension '
                             '(e.g., .png, .svg, .pdf, .tiff, .eps, .md).')
    args = parser.parse_args()

    generate_artifact(args.input, args.output)


if __name__ == '__main__':
    main()
