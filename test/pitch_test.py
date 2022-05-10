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
        self.new_user = User(1, 'viona', 'vee@gmail.com', 'vee')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,  User))
        
    def setUp(self):
    '''
        Set up method to run before each test cases.
    '''
        self.new_user = User("1","Viona","vee@gmail.com","vee")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.id,"1")
        self.assertEqual(self.new_user.username,"Viona")
        self.assertEqual(self.new_user.email,"Vee@gmail.com")
        self.assertEqual(self.new_user.password,"vee")