import json
from jsonschema import validate
from src.consort import ConsortDiagram
from src.prisma import PrismaDiagram
from src.strobe import StrobeDiagram
from src.checklist import Checklist
from src.stard import StardChecklist
from src.spirit import SpiritChecklist
from src.prisma_p import PrismaPChecklist
from src.tripod import TripodChecklist
from src.agree import AgreeChecklist
from src.right import RightChecklist
from src.srqr import SrqrChecklist
from src.coreq import CoreqChecklist
from src.arrive import ArriveChecklist
from src.squire import SquireChecklist
from src.cheers import CheersChecklist

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

    diagram_type = data.get('diagram_type')
    if not diagram_type:
        raise ValueError("The 'diagram_type' key is missing from the JSON file.")

    if diagram_type == "CONSORT":
        data = validate_data(data, schema_dir)
        diagram = ConsortDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"CONSORT diagram saved as {output_path}")
    elif diagram_type == "PRISMA":
        data = validate_data(data, schema_dir)
        diagram = PrismaDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"PRISMA diagram saved as {output_path}")
    elif diagram_type == "STROBE":
        data = validate_data(data, schema_dir)
        diagram = StrobeDiagram(data)
        diagram.build_graph()
        diagram.save(output_path)
        print(f"STROBE diagram saved as {output_path}")
    elif diagram_type == "STARD_checklist":
        data = validate_data(data, schema_dir)
        checklist = StardChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "SPIRIT_checklist":
        data = validate_data(data, schema_dir)
        checklist = SpiritChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "PRISMA-P_checklist":
        data = validate_data(data, schema_dir)
        checklist = PrismaPChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "TRIPOD_checklist":
        data = validate_data(data, schema_dir)
        checklist = TripodChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "AGREE_checklist":
        data = validate_data(data, schema_dir)
        checklist = AgreeChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "RIGHT_checklist":
        data = validate_data(data, schema_dir)
        checklist = RightChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "SRQR_checklist":
        data = validate_data(data, schema_dir)
        checklist = SrqrChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "COREQ_checklist":
        data = validate_data(data, schema_dir)
        checklist = CoreqChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "ARRIVE_checklist":
        data = validate_data(data, schema_dir)
        checklist = ArriveChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "SQUIRE_checklist":
        data = validate_data(data, schema_dir)
        checklist = SquireChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif diagram_type == "CHEERS_checklist":
        data = validate_data(data, schema_dir)
        checklist = CheersChecklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    elif "checklist" in diagram_type.lower():
        data = validate_data(data, schema_dir)
        checklist = Checklist(data)
        checklist.save(output_path)
        print(f"{diagram_type} checklist saved as {output_path}")
    else:
        raise ValueError(f"Unknown diagram_type: {diagram_type}")
