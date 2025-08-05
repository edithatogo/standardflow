import unittest
import os
import json
from web.app import app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        data = {
            'diagram_type': 'PRISMA',
            'records_identified': '1000',
            'records_after_duplicates_removed': '800',
            'records_screened': '800',
            'records_excluded': '200',
            'full_text_articles_assessed': '600',
            'full_text_articles_excluded': '300',
            'studies_included': '300'
        }
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Diagram', response.data)
        # Clean up the generated files
        os.remove('temp.json')

    def test_checklist_get(self):
        response = self.app.get('/checklist')
        self.assertEqual(response.status_code, 200)

    def test_checklist_post(self):
        data = {
            'checklist_type': 'CONSORT',
            'id-1': '1a',
            'section-1': 'Title and abstract',
            'description-1': 'Identification as a randomised trial in the title',
            'type-1': 'boolean',
            'assessed_for_eligibility': '1000',
            'excluded': '200',
            'randomized': '800',
            'allocated_to_intervention': '400',
            'received_allocated_intervention': '400',
            'did_not_receive_allocated_intervention': '0',
            'lost_to_follow_up': '20',
            'discontinued_intervention': '10',
            'analysed': '370',
            'excluded_from_analysis': '0'
        }
        response = self.app.post('/checklist', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generated Checklist', response.data)
        # Clean up the generated files
        os.remove('temp.json')
        os.remove('web/static/checklist.md')

if __name__ == '__main__':
    unittest.main()
