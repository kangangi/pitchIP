import unittest
from app.models import Pitch, User, Category
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(title = "title", description = "Description", upvotes = 1, downvotes = 1, category_id =1, user_id = 1)
        self.new_user = User(username = "diana", email ="diana@gmail.com", bio = "I am awesome", profile_pic_url = "image_url", password = 'diana')
        self.new_category = Category(category_name = 'category', id = 1)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        Category.query.delete()

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, 'title')
        self.assertEquals(self.new_pitch.description, 'description')
        self.assertEquals(self.new_pitch.upvotes, 1)
        self.assertEquals(self.new_pitch.downvotes, 1)
        self.assertEquals(self.new_pitch.user_id,1 )
        self.assertEquals(self.new_pitch.category_id,1)

    def test_get_user_pitch(self):
        self.new_pitch.save_pitch()
        get_pitch = Pitch.get_user_pitch(1)
        self.assertEqual(len(get_pitch)== 1)

    def test_get_category_pitch(self):
        self.new_pitch.save_pitch()
        get_pitch = Pitch.get_category_pitch(1)
        self.assertEqual(len(get_pitch) == 1)

    
    