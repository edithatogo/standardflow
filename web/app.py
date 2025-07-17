from flask import Flask, render_template, request, send_file
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from main import generate_artifact
import os
import json
import io

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
