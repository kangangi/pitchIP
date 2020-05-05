import unittest
from app.models import Pitch, User, Comment
from app import db

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(content = 'content', user_id = 1, pitch_id =1 )
        self.new_pitch = Pitch(title = "title", description = "Description", upvotes = 1, downvotes = 1, category_id =1, user_id = 1)
        self.new_user = User(username = "diana", email ="diana@gmail.com", bio = "I am awesome", profile_pic_url = "image_url", password = 'diana')
        

    def tearDown(self):
        Comment.query.delete()
        Pitch.query.delete()
        User.query.delete()

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content, 'content')
        self.assertEquals(self.new_commrent.user_id,1 )
        self.assertEquals(self.new_comment.pitch_id,1)

    def test_get_comments(self):
        self.new_comment.save_comment()
        get_comments = Comment.get_comments(1)
        self.assertEqual(len(get_comments) == 1)