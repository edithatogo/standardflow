class Checklist:
    def __init__(self, data):
        self.data = data

    def to_markdown(self):
        markdown = ""
        for item in self.data['items']:
            markdown += f"**{item['id']}**: {item['description']}\n\n"
            if item['type'] == 'boolean':
                markdown += "[ ] Yes\n[ ] No\n\n"
        return markdown

    def to_markdown_by_section(self):
        sections = {}
        for item in self.data['items']:
            section = item['section']
            if section not in sections:
                sections[section] = ""
            sections[section] += f"**{item['id']}**: {item['description']}\n\n"
            if item['type'] == 'boolean':
                sections[section] += "[ ] Yes\n[ ] No\n\n"
        return sections

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.to_markdown())
