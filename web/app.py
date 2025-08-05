from flask import Flask, render_template, request, send_file
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import generate_artifact

from .markdown_filter import markdown_filter

app = Flask(__name__)
app.jinja_env.filters['markdown'] = markdown_filter

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        diagram_type = data.get('diagram_type')
        if diagram_type:
            temp_file = "temp.json"
            with open(temp_file, 'w') as f:
                json.dump(data, f)

            output_file = os.path.join(app.root_path, 'static', 'diagram.png')
            generate_artifact(temp_file, output_file, schema_dir='schemas')
            return render_template('diagram_viewer.html', diagram_file='diagram.png')
    return render_template('index.html')

@app.route('/checklist', methods=['GET', 'POST'])
def checklist():
    if request.method == 'POST':
        data = request.form.to_dict()
        data['diagram_type'] = data.get('checklist_type')
        checklist_type = data.get('checklist_type')
        if checklist_type:
            temp_file = "temp.json"
            with open(temp_file, 'w') as f:
                json.dump(data, f)

            output_file = os.path.join(app.root_path, 'static', 'checklist.md')
            generate_artifact(temp_file, output_file, schema_dir='schemas')
            with open(output_file, 'r') as f:
                checklist_content = f.read()
            sections = {}
            current_section = None
            for line in checklist_content.split('\n'):
                if line.startswith('## '):
                    current_section = line[3:]
                    sections[current_section] = []
                elif current_section:
                    sections[current_section].append(line)
            return render_template('checklist_viewer.html', sections=sections)
    return render_template('checklist.html')

@app.route('/download_checklist')
def download_checklist():
    return send_file(os.path.join(app.root_path, 'static', 'checklist.md'), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
