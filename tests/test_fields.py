import unittest

from pale.fields import BaseField

class FieldsTests(unittest.TestCase):

    def setUp(self):
        super(FieldsTests, self).setUp()


    def test_instantiate_base_field_without_details(self):
        field = BaseField('user_id',
                          'integer',
                          'This is a test field')
        self.assertEqual(field.name, 'user_id')
        self.assertEqual(field.field_type, 'integer')
        self.assertEqual(field.description, 'This is a test field')
        self.assertIsNone(field.details)

        doc = field.doc_dict()
        self.assertEqual(doc['name'], 'user_id')
        self.assertEqual(doc['type'], 'integer')
        self.assertEqual(doc['description'], 'This is a test field')
        self.assertIsNone(doc['extended_description'])

    def test_instantiate_base_field_with_details(self):
        field = BaseField('user_id',
                          'integer',
                          'This is a test field',
                          'This is where I put special notes about the field')
        self.assertEqual(field.name, 'user_id')
        self.assertEqual(field.field_type, 'integer')
        self.assertEqual(field.description, 'This is a test field')
        self.assertEqual(field.details,
                'This is where I put special notes about the field')

        doc = field.doc_dict()
        self.assertEqual(doc['name'], 'user_id')
        self.assertEqual(doc['type'], 'integer')
        self.assertEqual(doc['description'], 'This is a test field')
        self.assertEqual(doc['extended_description'],
                'This is where I put special notes about the field')

