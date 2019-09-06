import unittest
from credentials import Credentials

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
        self.new_credentials = Credentials("Nicole","Facebook","Nicky","aline.nicole7@gmail.com","virgo7") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.accountName,"Nicole")
        self.assertEqual(self.new_credentials.siteName,"Facebook")
        self.assertEqual(self.new_credentials.username,"Nicky")
        self.assertEqual(self.new_credentials.email,"aline.nicole7@gmail.com")
        self.assertEqual(self.new_credentials.password,"virgo7")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() #saving the new credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

if __name__ == '__main__':
    unittest.main()
