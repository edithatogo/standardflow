import unittest
import io
import os
import zipfile
from web.app import app

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
        os.remove('web/diagram.png')

    def test_checklist_get(self):
        response = self.app.get('/checklist')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Research Artifacts Library', response.data)

    def test_checklist_post(self):
        data = {
            'checklist_type': 'CONSORT',
            'id-1': '1a',
            'section-1': 'Title and abstract',
            'description-1': 'Identification as a randomised trial in the title',
            'type-1': 'boolean',
        }
        response = self.app.post('/checklist', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Title and abstract', response.data)
        download = self.app.get('/download_checklist')
        self.assertEqual(download.status_code, 200)
        self.assertEqual(download.mimetype, 'application/zip')
        self.assertIn('attachment', download.headers['Content-Disposition'])
        self.assertIn('checklist.zip', download.headers['Content-Disposition'])
        with zipfile.ZipFile(io.BytesIO(download.data)) as archive:
            self.assertIn('Title_and_abstract.md', archive.namelist())
            self.assertIn(
                b'Identification as a randomised trial in the title',
                archive.read('Title_and_abstract.md'),
            )
        # Clean up the generated files
        os.remove('temp.json')

if __name__ == '__main__':
    unittest.main()
