import json

class Checklist:
    """
    A class to generate checklists from a JSON file.
    """
    def __init__(self, data):
        """
        Initializes the Checklist object.

        Args:
            data (dict): A dictionary containing the checklist data.
        """
        self.data = data

    def to_markdown_by_section(self):
        """
        Generates a dictionary of Markdown representations of the checklist, with one entry per section.
        """
        sections = {}
        for item in self.data['items']:
            section = item['section']
            if section not in sections:
                sections[section] = ""

            sections[section] += f"**{item['id']}**: {item['description']}\n\n"

            if item['type'] == 'boolean':
                sections[section] += f"[ ] Yes\n"
                sections[section] += f"[ ] No\n"
            elif item['type'] == 'string':
                sections[section] += f"Response: ________________\n"
            elif item['type'] == 'integer':
                sections[section] += f"Response: ________________\n"
            elif item['type'] == 'multiple_choice':
                for option in item['options']:
                    sections[section] += f"[ ] {option}\n"

            sections[section] += "\n"

        return sections

    def generate(self, output_directory="checklist"):
        """
        Generates the checklist and saves it to a directory of files.

        Args:
            output_directory (str): The name of the output directory.
        """
        import os
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        sections = self.to_markdown_by_section()
        for section, markdown in sections.items():
            filename = os.path.join(output_directory, f"{section.replace(' ', '_')}.md")
            with open(filename, 'w') as f:
                f.write(markdown)

        print(f"Checklist saved to directory {output_directory}")
