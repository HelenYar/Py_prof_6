import json
import unittest
from unittest.mock import patch
import app

documents = []
directories = {}


def setUpModule():

    with open('directories.json', 'r', encoding='utf-8') as dir:
        directories.update(json.load(dir))
    with open('documents.json', 'r', encoding='utf-8') as doc:
        documents.extend(json.load(doc))


@patch('app.directories', directories)
@patch('app.documents', documents)

class TestSecretaryProgram(unittest.TestCase):


    def test_get_doc_owner_name(self):
        self.assertEqual(app.get_doc_owner_name('10006'), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)

    def test_get_doc_shelf(self):
        self.assertEqual(app.get_doc_shelf('10006'), '2')

    def test_move_doc_to_shelf(self):
        self.assertIn(app.move_doc_to_shelf('10006', '3'), directories['3'])

    # def test_delete_doc(self):
    #     self.assertNotIn(app.delete_doc('10006'), documents)



