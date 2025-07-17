import unittest
import sys
import os
sys.path.append('web')
from app import app

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Research Artifacts Library', response.data)

    def test_index_post(self):
        data = {
            'diagram_type': 'PRISMA',
            'json_data': '''
                {
                    "diagram_type": "PRISMA",
                    "records_identified": 1000,
                    "records_after_duplicates_removed": 800,
                    "records_screened": 800,
                    "records_excluded": 200,
                    "full_text_articles_assessed": 600,
                    "full_text_articles_excluded": 300,
                    "studies_included": 300
                }
            '''
        }
        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/png')
        # Clean up the generated files
        os.remove('temp.json')
        os.remove('web/diagram.png')

if __name__ == '__main__':
    unittest.main()
