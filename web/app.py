print("Executing web/app.py...")
from flask import Flask, render_template, request, send_file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import generate_artifact
import os
import json
import io

from markdown_filter import markdown_filter

app = Flask(__name__)
app.jinja_env.filters['markdown'] = markdown_filter

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        diagram_type = request.form['diagram_type']
        json_data = request.form['json_data']

        # Create a temporary file to store the JSON data
        with open('temp.json', 'w') as f:
            f.write(json_data)

        # Generate the diagram
        output_filename = 'web/diagram.png'
        generate_artifact('temp.json', output_filename)

        # Return the diagram as an image
        return send_file('diagram.png', mimetype='image/png')

    return render_template('index.html')

@app.route('/checklist', methods=['GET', 'POST'])
def checklist():
    if request.method == 'POST':
        checklist_type = request.form['checklist_type']
        json_data = request.form['json_data']

        # Create a temporary file to store the JSON data
        with open('temp.json', 'w') as f:
            f.write(json_data)

        # Generate the checklist
        from checklist import Checklist
        with open('temp.json', 'r') as f:
            data = json.load(f)
        checklist = Checklist(data)
        sections = checklist.to_markdown_by_section()

        return render_template('checklist_viewer.html', sections=sections)

    return render_template('checklist.html')

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)
    print("Flask application stopped.")
