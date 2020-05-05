import unittest
from app.models import Category
from app import db

class CategoryModelTest(unittest.TestCase):
    def setUp(self):
        self.new_category = Category(category_name = 'category')

    def test_get_category_name(self):

        self.new_category = Category(category_name = 'category')
        get_id = Category.get_category_name('category')
        self.assertEqual(get_id, 1)