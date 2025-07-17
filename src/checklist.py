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

    def to_markdown(self):
        """
        Generates a Markdown representation of the checklist.
        """
        markdown = f"# {self.data['title']}\n\n"

        current_section = None
        for item in self.data['items']:
            if item['section'] != current_section:
                current_section = item['section']
                markdown += f"## {current_section}\n\n"

            markdown += f"**{item['id']}**: {item['description']}\n\n"

            if item['type'] == 'boolean':
                markdown += f"[ ] Yes\n"
                markdown += f"[ ] No\n"
            elif item['type'] == 'string':
                markdown += f"Response: ________________\n"
            elif item['type'] == 'integer':
                markdown += f"Response: ________________\n"
            elif item['type'] == 'multiple_choice':
                for option in item['options']:
                    markdown += f"[ ] {option}\n"

            markdown += "\n"

        return markdown

    def generate(self, output_filename="checklist.md"):
        """
        Generates the checklist and saves it to a file.

        Args:
            output_filename (str): The name of the output file.
        """
        markdown = self.to_markdown()
        with open(output_filename, 'w') as f:
            f.write(markdown)

        print(f"Checklist saved as {output_filename}")
