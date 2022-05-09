import unittest
from models import User

class UserTest(unittest.TestCase):
    """
    test class to test the behavior of the user class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_user = Movie(1, 'viona', 'vee@gmail.com', 'vee')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,  User))
        
if __name__ == '__main__':
    unittest.main()