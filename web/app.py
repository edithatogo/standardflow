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

        data = {'diagram_type': diagram_type}

        if diagram_type == 'PRISMA':
            data['records_identified'] = int(request.form['records_identified'])
            data['records_after_duplicates_removed'] = int(request.form['records_after_duplicates_removed'])
            data['records_screened'] = int(request.form['records_screened'])
            data['records_excluded'] = int(request.form['records_excluded'])
            data['full_text_articles_assessed'] = int(request.form['full_text_articles_assessed'])
            data['full_text_articles_excluded'] = int(request.form['full_text_articles_excluded'])
            data['studies_included'] = int(request.form['studies_included'])
        elif diagram_type == 'PRISMA_2020_UPDATED':
            data['previous_studies'] = int(request.form['previous_studies'])
            data['new_records_identified'] = int(request.form['new_records_identified'])
            data['new_records_after_duplicates_removed'] = int(request.form['new_records_after_duplicates_removed'])
            data['new_records_screened'] = int(request.form['new_records_screened'])
            data['new_records_excluded'] = int(request.form['new_records_excluded'])
            data['new_full_text_articles_assessed'] = int(request.form['new_full_text_articles_assessed'])
            data['new_full_text_articles_excluded'] = int(request.form['new_full_text_articles_excluded'])
            data['new_studies_included'] = int(request.form['new_studies_included'])
            data['total_studies_included'] = int(request.form['total_studies_included'])
        elif diagram_type == 'CONSORT':
            data['assessed_for_eligibility'] = int(request.form['assessed_for_eligibility'])
            data['excluded'] = int(request.form['excluded'])
            data['randomized'] = int(request.form['randomized'])
            data['allocated_to_intervention'] = int(request.form['allocated_to_intervention'])
            data['received_allocated_intervention'] = int(request.form['received_allocated_intervention'])
            data['did_not_receive_allocated_intervention'] = int(request.form['did_not_receive_allocated_intervention'])
            data['lost_to_follow_up'] = int(request.form['lost_to_follow_up'])
            data['discontinued_intervention'] = int(request.form['discontinued_intervention'])
            data['analysed'] = int(request.form['analysed'])
            data['excluded_from_analysis'] = int(request.form['excluded_from_analysis'])
        elif diagram_type == 'CONSORT_CLUSTER':
            data['clusters_assessed_for_eligibility'] = int(request.form['clusters_assessed_for_eligibility'])
            data['clusters_excluded'] = int(request.form['clusters_excluded'])
            data['clusters_randomized'] = int(request.form['clusters_randomized'])
            data['clusters_allocated_to_intervention'] = int(request.form['clusters_allocated_to_intervention'])
            data['individuals_in_clusters_allocated_to_intervention'] = int(request.form['individuals_in_clusters_allocated_to_intervention'])
            data['clusters_lost_to_follow_up'] = int(request.form['clusters_lost_to_follow_up'])
            data['individuals_lost_to_follow_up'] = int(request.form['individuals_lost_to_follow_up'])
            data['clusters_discontinued_intervention'] = int(request.form['clusters_discontinued_intervention'])
            data['individuals_discontinued_intervention'] = int(request.form['individuals_discontinued_intervention'])
            data['clusters_analysed'] = int(request.form['clusters_analysed'])
            data['individuals_analysed'] = int(request.form['individuals_analysed'])
            data['clusters_excluded_from_analysis'] = int(request.form['clusters_excluded_from_analysis'])
            data['individuals_excluded_from_analysis'] = int(request.form['individuals_excluded_from_analysis'])
        elif diagram_type == 'STROBE':
            data['potentially_eligible'] = int(request.form['potentially_eligible'])
            data['assessed_for_eligibility'] = int(request.form['assessed_for_eligibility'])
            data['excluded_before_study'] = int(request.form['excluded_before_study'])
            data['included_in_study'] = int(request.form['included_in_study'])
            data['lost_to_follow_up'] = int(request.form['lost_to_follow_up'])
            data['incomplete_data'] = int(request.form['incomplete_data'])
            data['analysed'] = int(request.form['analysed'])
        elif diagram_type == 'STROBE_COHORT':
            data['exposed_group_potentially_eligible'] = int(request.form['exposed_group_potentially_eligible'])
            data['exposed_group_assessed_for_eligibility'] = int(request.form['exposed_group_assessed_for_eligibility'])
            data['exposed_group_excluded'] = int(request.form['exposed_group_excluded'])
            data['exposed_group_included'] = int(request.form['exposed_group_included'])
            data['exposed_group_lost_to_follow_up'] = int(request.form['exposed_group_lost_to_follow_up'])
            data['exposed_group_analysed'] = int(request.form['exposed_group_analysed'])
            data['unexposed_group_potentially_eligible'] = int(request.form['unexposed_group_potentially_eligible'])
            data['unexposed_group_assessed_for_eligibility'] = int(request.form['unexposed_group_assessed_for_eligibility'])
            data['unexposed_group_excluded'] = int(request.form['unexposed_group_excluded'])
            data['unexposed_group_included'] = int(request.form['unexposed_group_included'])
            data['unexposed_group_lost_to_follow_up'] = int(request.form['unexposed_group_lost_to_follow_up'])
            data['unexposed_group_analysed'] = int(request.form['unexposed_group_analysed'])

        # Create a temporary file to store the JSON data
        with open('temp.json', 'w') as f:
            json.dump(data, f)

        # Generate the diagram
        output_filename = 'web/diagram.png'
        generate_artifact('temp.json', output_filename)

        # Return the diagram as an image
        return render_template('diagram_viewer.html', diagram_image='diagram.png')

    return render_template('index.html')

import zipfile

zip_buffer = None

@app.route('/checklist', methods=['GET', 'POST'])
def checklist():
    global zip_buffer
    if request.method == 'POST':
        checklist_type = request.form['checklist_type']

        items = []
        item_count = 0
        while f'id-{item_count + 1}' in request.form:
            item_count += 1
            item = {
                'id': request.form[f'id-{item_count}'],
                'section': request.form[f'section-{item_count}'],
                'description': request.form[f'description-{item_count}'],
                'type': request.form[f'type-{item_count}'],
            }
            if item['type'] == 'multiple_choice':
                item['options'] = []
                option_count = 0
                while f'option-{item_count}-{option_count + 1}' in request.form:
                    option_count += 1
                    item['options'].append(request.form[f'option-{item_count}-{option_count}'])
            items.append(item)

        data = {
            'checklist_type': checklist_type,
            'items': items
        }

        # Create a temporary file to store the JSON data
        with open('temp.json', 'w') as f:
            json.dump(data, f)

        # Generate the checklist
        from checklist import Checklist
        with open('temp.json', 'r') as f:
            data = json.load(f)
        checklist = Checklist(data)
        sections = checklist.to_markdown_by_section()

        # Create a zip file with the markdown files
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zf:
            for section, markdown in sections.items():
                filename = f"{section.replace(' ', '_')}.md"
                zf.writestr(filename, markdown)
        zip_buffer.seek(0)

        return render_template('checklist_viewer.html', sections=sections, zip_file='checklist.zip')

    return render_template('checklist.html')

@app.route('/download_checklist')
def download_checklist():
    global zip_buffer
    if zip_buffer:
        return send_file(zip_buffer, as_attachment=True, download_name='checklist.zip', mimetype='application/zip')
    return "No checklist generated yet."

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)
    print("Flask application stopped.")
