import unittest
from app.models import Category
from app import db

class CategoryModelTest(unittest.TestCase):
    def setUp(self):
        self.new_category = Category(category_name = 'category')
        db.session.add(self.new_category)
        db.session.commit()

        self.assertEquals(self.new_category.category_name, "category")

    def tearDown(self):
        Category.query.delete()
        db.session.commit()  

    def test_get_category_name(self):
        db.session.add(self.new_category)
        db.session.commit()
        get_id = Category.get_category_name('category')
        self.assertEqual(get_id, 1)

