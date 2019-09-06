import unittest # Importing the unittest module
from user import User 
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    #Items up here....
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Nicky","aline.nicole7@gmail.com","virgo7") #create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Nicky")
        self.assertEqual(self.new_user.email,"aline.nicole7@gmail.com")
        self.assertEqual(self.new_user.password,"virgo7")

if __name__ == '__main__':
    unittest.main()


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #Items up here....

    def setUp(self):
        '''
        Set up method to ru before each test cases.
        '''
        self.new_credentials = Credentials("Nicole","Facebook","Nicky","aline.nicole7@gmail.com","virgo7") #create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.accountName,"Nicole")
        self.assertEqual(self.new_credentials.siteName,"Facebook")
        self.assertEqual(self.new_credentials.username,"Nicky")
        self.assertEqual(self.new_credentials.email,"aline.nicole7@gmail.com")
        self.assertEqual(self.new_credentials.password,"virgo7")

if __name__ == '__main__':
    unittest.main()
