import unittest # Importing the unittest module
from user import User 


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
        self.new_user = User("Nicky","aline.nicole7@gmail.com","virgo7")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Nicky")
        self.assertEqual(self.new_user.email,"aline.nicole7@gmail.com")
        self.assertEqual(self.new_user.password,"virgo7")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

#setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

#other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Aline","nickoline@yahoo.fr","santa7") # new user
        test_user.save_user()
        self.new_user.delete_user() #deleting an user object 
        self.assertEqual(len(User.user_list),1)

#more tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove an user from our user list
            '''
            
    







if __name__ == '__main__':
    unittest.main()


